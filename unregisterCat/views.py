from django.conf import settings

# For Define API Views
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import  UnregisterShop, UnregisterShopImage, CatApply, CatApplyImage, ShopType
from .serializers import UnregisterShopSerializer, UnregisterShopImageSerializer, CatApplySerializer, ShopTypeSerializer

from utils.send_email import send_email
from utils.email_templates import cat_register_email

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
                # shop_data.shop_type = ShopType.objects.get(id=shop_type_id)
                item = shop_data.save()
                for image in images:
                    UnregisterShopImage.objects.create(shop_id=item.id, imgs=image)
                
                send_email(shop_data.data['email'], "看板猫！発見御礼にゃ！", "<p>" + shop_data.data['shop_name'] + "様</p>" + cat_register_email)
                send_email(settings.BACKEND_EMAIL, '看板猫　登録依頼にゃ！',
                           f"""
                                <p>事務局担当者</p>
                                <p>
                                    「推しニャン」サイトに看板猫発見の依頼がありました。<br/>
                                    下記ご確認ください。
                                </p>
                                <p>日時：{shop_data.data['created_date']}</p>
                                <p>
                                    <span>店舗名：{shop_data.data['shop_name']}</span><br />
                                    <span>住所：{shop_data.data['prefecture'], shop_data.data['city'], shop_data['street'], shop_data.data['detail_address']}</span><br />
                                    <span>メールアドレス：{shop_data.data['email']}</span><br />
                                    <span>電話：{shop_data.data['phone']}</span><br />
                                    <span>店舗許諾：{shop_data.data['shop_permission']}</span><br />
                                    <span>看板猫情報：{shop_data.data['cat_info']}</span>
                                </p>
                                <p>以上です。</p>
                            """
                        )
                
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