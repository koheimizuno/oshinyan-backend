from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnregisterShopViewSet, UnregisterShopImageViewSet, CatApplyViewSet

router = DefaultRouter()
router.register(r'shop', UnregisterShopViewSet)
router.register(r'shopimage', UnregisterShopImageViewSet)
router.register(r'oshiresister', CatApplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]