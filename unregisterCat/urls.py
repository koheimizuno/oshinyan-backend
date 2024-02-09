from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnregisterShopViewSet, UnregisterShopImageViewSet, CatApplyViewSet, ShopTypeViewSet

router = DefaultRouter()
router.register(r'shop', UnregisterShopViewSet)
router.register(r'shopimage', UnregisterShopImageViewSet)
router.register(r'oshiresister', CatApplyViewSet)
router.register(r'shopcategory', ShopTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]