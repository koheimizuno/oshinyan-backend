from rest_framework import serializers
from . import models

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recommend
        fields = "__all__"

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Character
        fields = "__all__"
   
class FavoriteThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteThing
        fields = "__all__"

class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CatImage
        fields = "__all__"

class CatImageByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CatImageByAdmin
        fields = "__all__"

class CatSerializer(serializers.ModelSerializer):
    images = CatImageSerializer(read_only=True, many=True)
    admin_images = CatImageByAdminSerializer(read_only=True, many=True)
    recommend = RecommendSerializer(read_only=True, many=True)
    character = CharacterSerializer(many=True, read_only=True)
    favorite_things = FavoriteThingSerializer(many=True, read_only=True)
    class Meta:
        model = models.Cat
        fields = "__all__"
        depth = 1
    def validate(self, data):
        email = data.get('email')
        if models.Cat.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'message': 'Email Address already exists'})
        return data

class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentImage
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    comment_images = CommentImageSerializer(read_only=True, many=True)
    class Meta:
        model = models.Comment
        fields='__all__'

class CommentImageRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentImageRecommend
        fields = "__all__"

class CommentListSerializer(serializers.ModelSerializer):
    comment_images = CommentImageSerializer(read_only=True, many=True)
    class Meta:
        model = models.Comment
        fields='__all__'
        # exclude = ['cat']
        depth = 2

class AdvertiseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertiseImage
        fields = "__all__"

class AdvertiseImageByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertiseImageByAdmin
        fields = "__all__"

class AdvertiseSerializer(serializers.ModelSerializer):
    images = CatImageSerializer(read_only=True, many=True)
    admin_images = AdvertiseImageByAdminSerializer(read_only=True, many=True)
    recommend = RecommendSerializer(read_only=True, many=True, required=False)
    character = CharacterSerializer(many=True, read_only=True)
    favorite_things = FavoriteThingSerializer(many=True, read_only=True)
    class Meta:
        model = models.Advertise
        fields = "__all__"
        depth = 1
    def validate(self, data):
        email = data.get('email')
        if models.Advertise.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'message': 'Email Address already exists'})
        return data
    
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = "__all__"

class ColumnBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ColumnBlog
        fields = "__all__"

class ColumnSerializer(serializers.ModelSerializer):
    blog = ColumnBlogSerializer(read_only=True, many=True)
    class Meta:
        model = models.Column
        fields = "__all__"

class ShopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShopImage
        fields = "__all__"

class ShopSerializer(serializers.ModelSerializer):
    shop_images = ShopImageSerializer(read_only=True, many=True)
    cat = CatSerializer(read_only=True, many=True)
    class Meta:
        model = models.Shop
        fields = '__all__'
        depth = 1
    def validate(self, data):
        email = data.get('email')
        shop_name = data.get('shop_name')
        if models.Shop.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'message': 'Email Address already exists'})
        if models.Shop.objects.filter(shop_name=shop_name).exists():
            raise serializers.ValidationError(
                {'message': 'Shop Name already exists'})
        return data
    
class ShopTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShopType
        fields = "__all__"
    def validate(self, attrs):
        shop_type = attrs.get('shop_type')
        if models.ShopType.objects.filter(shop_type=shop_type).exists():
            raise serializers.ValidationError("shop_type field is required.")
        return attrs

class ReactionCatIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReactionCatIcon
        fields = "__all__"

class ReactionFoodIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReactionFoodIcon
        fields = "__all__"

class ReactionWordIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReactionWordIcon
        fields = "__all__"

class ReactionHeartIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReactionHeartIcon
        fields = "__all__"

class ReactionSeasonIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReactionSeasonIcon
        fields = "__all__"

class ReactionPartyIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReactionPartyIcon
        fields = "__all__"

class CommentReactionIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentReactionIcon
        fields = "__all__"