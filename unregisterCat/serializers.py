from rest_framework import serializers
from .models import Shop, ShopImage, CatApplication

class ShopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopImage
        fields = "__all__"

class ShopSerializer(serializers.ModelSerializer):
    shop_images = ShopImageSerializer(read_only=True, many=True)
    # cat = CatSerializer(read_only=True, many=True)
    class Meta:
        model = Shop
        fields = '__all__'
    def validate(self, data):
        email = data.get('email')
        shop_name = data.get('shop_name')
        if Shop.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'message': 'Email Address already exists'})
        if Shop.objects.filter(shop_name=shop_name).exists():
            raise serializers.ValidationError(
                {'message': 'Shop Name already exists'})
        return data
    
class CatApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatApplication
        fields = "__all__"