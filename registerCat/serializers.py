from rest_framework import serializers
from .models import Recommend, Character, FavoriteThing, CatImage, CatImageByAdmin, Cat

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = "__all__"

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
   
class FavoriteThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteThing
        fields = "__all__"

class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = "__all__"

class CatImageByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImageByAdmin
        fields = "__all__"

class CatSerializer(serializers.ModelSerializer):
    cat_images = CatImageSerializer(read_only=True, many=True)
    cat_admin_images = CatImageByAdminSerializer(read_only=True, many=True)
    recommend = RecommendSerializer(read_only=True, many=True)
    character = CharacterSerializer(many=True, read_only=True)
    favorite_things = FavoriteThingSerializer(many=True, read_only=True)
    class Meta:
        model = Cat
        fields = "__all__"
        depth = 1
    def validate(self, data):
        email = data.get('email')
        if Cat.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'message': 'Email Address already exists'})
        return data
