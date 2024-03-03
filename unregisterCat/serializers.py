from rest_framework import serializers
from .models import UnregisterShop, UnregisterShopImage, CatApply, ShopType
from registerCat.serializers import CatSerializer

class UnregisterShopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnregisterShopImage
        fields = "__all__"

class UnregisterShopSerializer(serializers.ModelSerializer):
    shop_images = UnregisterShopImageSerializer(read_only=True, many=True)
    cat = CatSerializer(read_only=True, many=True)
    class Meta:
        model = UnregisterShop
        fields = '__all__'
    def validate(self, data):
        email = data.get('email')
        shop_name = data.get('shop_name')
        if UnregisterShop.objects.filter(email=email).exists() and UnregisterShop.objects.filter(shop_name=shop_name).exists():
            raise serializers.ValidationError(
                {'message': 'Already exists'})
        return data
    
class CatApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatApply
        fields = "__all__"
    def validate(self, data):
        email = data.get('email')
        if CatApply.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'message': 'Email Address already exists'})
        return data

class ShopTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopType
        fields = "__all__"