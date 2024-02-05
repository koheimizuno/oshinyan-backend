from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'avatar', views.AvatarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('tokenlogin', views.TokenLoginView.as_view(), name='token_login'),
    path('register', views.UserRegistrationView.as_view(), name='register'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('password_reset', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/confirm/<str:uidb64>/<str:token>/',
         views.ResetPasswordConfirm.as_view(), name='password_reset_confirm'),
]