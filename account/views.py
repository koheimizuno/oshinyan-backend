from django.conf import settings
from utils.functions import send_email
from utils.email_templates import register_email, password_reset_email

# For Define API Views
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from account.models import Member, Avatar
from .serializers import MemberSerializer, PasswordResetSerializer, AvatarSerializer

# For User Authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

# For PasswordRest
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import AllowAny
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

class UserViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    
class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Hash the password
        hashed_password = make_password(serializer.validated_data['password'])
        serializer.validated_data['password'] = hashed_password
        self.perform_create(serializer)
        user = serializer.instance
        send_email(user.email, "「推しニャン」サイト　会員登録お礼", register_email.format(user.username))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_user = Member.objects.get(email=request.data.get('email'))
        request.data['username'] = login_user.username
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id, 'user_name': user.username})

class TokenLoginView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        user_info = {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'avatar': AvatarSerializer(user.avatar, context={'request': request}).data if user.avatar else None
        }
        return Response(user_info)

class LogOutView(APIView):
    authentication_classes((TokenAuthentication))
    permission_class = [IsAuthenticated]
    def post(self, request):
        token = request.data['token']
        if token is not None:
            token = Token.objects.get(key=token)
            token.delete()
            return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

class ResetPasswordView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = Member.objects.get(email=email)

        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = default_token_generator.make_token(user)
        send_email(user.email, "パスワードリセット", password_reset_email.format(settings.FRONT_URL, uid, token))
        return Response(status=status.HTTP_200_OK)

class ResetPasswordConfirm(generics.CreateAPIView):
    def post(self, request, uidb64, token):
        try:
            user_id = urlsafe_base64_decode(uidb64).decode()
            user = Member.objects.get(id=user_id)
            if default_token_generator.check_token(user, token):
                new_password = request.data.get('new_password')
                user.set_password(new_password)
                user.save()
                return Response(data='パスワードのリセットに成功しました。', status=status.HTTP_200_OK)
            else:
                return Response(data='無効なトークン', status=status.HTTP_400_BAD_REQUEST)
        except Member.DoesNotExist:
            return Response(data='ユーザーが見つかりません。', status=status.HTTP_400_BAD_REQUEST)