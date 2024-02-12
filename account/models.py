from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django_resized import ResizedImageField

class UserManager(BaseUserManager):
    def create_user(self, username, email, avatar=None, password=None, prefecture=''):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            prefecture=prefecture,
            avatar=avatar
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Avatar(models.Model):
    avatar = ResizedImageField(force_format="WEBP", quality=75, upload_to="avatars")
    class Meta:
        verbose_name_plural = "プロフィール画像"

class Member(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True, verbose_name='ニックネーム')
    email = models.EmailField(unique=True, verbose_name='メールアドレス')
    prefecture = models.CharField(max_length=100,blank=True, null=True, verbose_name='居住エリア')
    avatar = models.ForeignKey(
        Avatar, on_delete=models.CASCADE, related_name='avatar_url', blank=True, null=True, verbose_name='プロフィール画像')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    class Meta:
        verbose_name_plural = "会員"
    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.avatar.url
        return None