from rest_framework import serializers
from .models import Avatar
from account.models import Member as User
from registerCat.serializers import RecommendSerializer

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = "__all__"

class MemberSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()
    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=False, write_only=True)
    recommend = RecommendSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'prefecture', 'avatar', 'recommend', 'avatar_url')
        extra_kwargs = {'password': {'write_only': True}}
    # validation for exisiting usernames and email addresses.
    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'message': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'message': 'Email Address already exists'})
        return data
    def get_avatar_url(self, user):
        if user.avatar:
            request = self.context.get('request')
            if request is not None:
                avatar_url = user.avatar.avatar.url
                return request.build_absolute_uri(avatar_url)
        return None
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def validate_email(self, value):
       # Check if the email exists in your database
        try:
            user = User.objects.get(email=value)
            print(user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "This email does not exist in our system.")
        return value