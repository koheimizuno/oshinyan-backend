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

    def validate_password(self, value):
        # Validate that the password contains at least 6 alphanumeric characters
        if len(value) < 6 or not any(char.isnumeric() for char in value) or not any(char.isalpha() for char in value):
            raise serializers.ValidationError('Password must contain at least 6 alphanumeric characters.')
        return value
    
    # validation for exisiting usernames and email addresses.
    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email Address already exists')
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
        avatar_data = validated_data.get('avatar')
        if avatar_data:
            try:
                instance.avatar = avatar_data
            except Avatar.DoesNotExist:
                raise serializers.ValidationError({'message': 'Invalid avatar ID provided'})
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