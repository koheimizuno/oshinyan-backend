from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmbassadorViewSet

router = DefaultRouter()

urlpatterns = [
    path('', AmbassadorViewSet.as_view({'get': 'list', 'post': 'create'}), name='ambassador-list'),
]