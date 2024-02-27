from django.conf import settings

# For Define API Views
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import  UnregisterShop, UnregisterShopImage, CatApply, CatApplyImage, ShopType
from .serializers import UnregisterShopSerializer, UnregisterShopImageSerializer, CatApplySerializer, ShopTypeSerializer

from utils.functions import send_email
from utils.email_templates import unregister_shop_email, unregister_shop_admin_email

class UnregisterShopViewSet(viewsets.ModelViewSet):
    queryset = UnregisterShop.objects.all()
    serializer_class = UnregisterShopSerializer
    def create(self, request, *args, **kwargs):
        shop_data = self.get_serializer(data=request.data)
        # shop_type_id = self.request.data.pop('shop_type', None)
        images = request.FILES.getlist('imgs')
        shop_name = request.data.get('shop_name')
        if shop_data.is_valid():
            if not UnregisterShop.objects.filter(shop_name=shop_name).exists():
                item = shop_data.save()
                for image in images:
                    UnregisterShopImage.objects.create(shop_id=item.id, imgs=image)
                send_email(shop_data.data['email'], "看板猫！発見御礼にゃ！", unregister_shop_email.format(shop_data.data['shop_name']))
                send_email(settings.BACKEND_EMAIL, '看板猫　登録依頼にゃ！', unregister_shop_admin_email.format(shop_data.data['created_date'], shop_data.data['shop_name'], \
                                shop_data.data['email'], shop_data.data['phone'], shop_data.data['shop_permission'], shop_data.data['cat_info']))
                
                return Response(shop_data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': shop_data.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class UnregisterShopImageViewSet(viewsets.ModelViewSet):
    queryset = UnregisterShopImage.objects.all()
    serializer_class = UnregisterShopImageSerializer

class CatApplyViewSet(viewsets.ModelViewSet):
    queryset = CatApply.objects.all()
    serializer_class = CatApplySerializer
    def create(self, request, *args, **kwargs):
        catapply_data = self.get_serializer(data=request.data)
        images = request.FILES.getlist('imgs')
        if catapply_data.is_valid():
            item = catapply_data.save()
            for image in images:
                CatApplyImage.objects.create(cat_id=item.id, imgs=image)
            return Response(catapply_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': catapply_data.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class ShopTypeViewSet(viewsets.ModelViewSet):
    queryset = ShopType.objects.all()
    serializer_class = ShopTypeSerializer