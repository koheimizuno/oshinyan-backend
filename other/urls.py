from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'ambassador', views.AmbassadorViewSet)
router.register(r'inquiry', views.InquiryViewSet)
router.register(r'banner', views.BannerViewSet)
# router.register(r'advertise', views.AdvertiseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]