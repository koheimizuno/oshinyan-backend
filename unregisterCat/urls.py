from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopViewSet, ShopImageViewSet, CatApplicationViewSet

router = DefaultRouter()
router.register(r'shop', ShopViewSet)
router.register(r'shopimage', ShopImageViewSet)
router.register(r'oshiresister', CatApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]