from django.db import models
from account.models import Member
from utils.constants import PREFECTURE_CHOICES, ATTENDANCE_CHOICES

class ShopType(models.Model):
    shop_type = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "店舗カテゴリ"
    def __str__(self):
        return self.shop_type

class Shop(models.Model):
    shop_name = models.CharField(max_length=100, verbose_name='店舗名')
    shop_type = models.ForeignKey(
        ShopType, on_delete=models.CASCADE, related_name='shop', verbose_name='店舗カテゴリ')
    prefecture = models.CharField(max_length=100, choices=PREFECTURE_CHOICES, default='北海道', verbose_name='都道府県')
    address = models.CharField(verbose_name='住所')
    nearest_station = models.CharField(verbose_name='最寄り駅')
    phone = models.CharField(max_length=20, verbose_name='電話番号（登録者）')
    business_time = models.CharField(verbose_name='営業時間')
    rest_day = models.CharField(verbose_name='定休日')
    url = models.URLField(verbose_name='店舗ホームページ')
    last_update = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "店舗"
    def __str__(self):
        return self.shop_name

class ShopImage(models.Model):
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='shop_images')
    imgs = models.ImageField(upload_to='unregistershop')
    class Meta:
        verbose_name_plural = "画像"
    def __int__(self):
        return self.shop

class Character(models.Model):
    character = models.CharField(max_length=100, verbose_name='性格')
    class Meta:
        verbose_name_plural='性格'
    def __str__(self):
        return self.character
    
class FavoriteThing(models.Model):
    favorite_things = models.CharField(max_length=100, verbose_name='好きなもの・コト')
    class Meta:
        verbose_name_plural='好きなもの・コト'
    def __str__(self):
        return self.favorite_things
    
class Cat(models.Model):
    is_public = models.BooleanField(default=False, verbose_name='公開')
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='cat', verbose_name='店舗')
    cat_name = models.CharField(max_length=100, verbose_name='猫の名前')
    character = models.ManyToManyField(Character, verbose_name='性格')
    favorite_things = models.ManyToManyField(FavoriteThing, verbose_name='好きなもの・コト')
    attendance = models.CharField(max_length=6, choices=ATTENDANCE_CHOICES, default='毎日', verbose_name='出没頻度')
    description = models.TextField(verbose_name='猫の説明')
    last_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='看板猫'
    def __str__(self):
        return self.cat_name
    def __int__(self):
        return self.cat_name
    
class CatImage(models.Model):
    cat = models.ForeignKey(
        Cat, on_delete=models.CASCADE, related_name='images')
    imgs = models.ImageField(upload_to='cat/images')
    def __int__(self):
        return f"Image of {self.cat}"
    class Meta:
        verbose_name_plural='看板猫画像'
    
class CatImageByAdmin(models.Model):
    cat = models.ForeignKey(
        Cat, on_delete=models.CASCADE, related_name='admin_images')
    imgs = models.ImageField(upload_to='cat/admin_images')
    def __int__(self):
        return f"Image of {self.cat}"
    class Meta:
        verbose_name_plural='画像'
    
class Advertise(models.Model):
    is_public = models.BooleanField(default=False, verbose_name='公開')
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='advertise_cat', null=True, blank=True, verbose_name='店舗')
    cat_name = models.CharField(max_length=100, blank=True, verbose_name='猫の名前')
    character = models.ManyToManyField(Character, verbose_name='性格')
    favorite_things = models.ManyToManyField(FavoriteThing, verbose_name='好きなもの・コト')
    attendance = models.CharField(max_length=6, choices=ATTENDANCE_CHOICES, default='毎日', verbose_name='出没頻度')
    description = models.TextField(blank=True, verbose_name='猫の説明')
    last_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='広告看板猫'
    def __str__(self):
        return self.cat_name
    def __int__(self):
        return self.cat_name
    
class AdvertiseImage(models.Model):
    cat = models.ForeignKey(
        Advertise, on_delete=models.CASCADE, related_name='images')
    imgs = models.ImageField(upload_to='advertise/images')
    class Meta:
        verbose_name_plural = '画像'
    
class AdvertiseImageByAdmin(models.Model):
    cat = models.ForeignKey(
        Advertise, on_delete=models.CASCADE, related_name='admin_images')
    imgs = models.ImageField(upload_to='advertise/admin_images')
    def __int__(self):
        return f"Image of {self.cat}"
    class Meta:
        verbose_name_plural='画像'

class Recommend(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='recommend', null=True, blank=True, verbose_name='看板猫')
    advertise = models.ForeignKey(Advertise, on_delete=models.CASCADE, related_name='recommend', null=True, blank=True, verbose_name='広告猫')
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='recommend', null=True, blank=True, verbose_name='会員')
    class Meta:
        verbose_name_plural='推し'
    def __int__(self):
        return self.user
    
class Comment(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='comment', null=True, blank=True, verbose_name='看板猫')
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comment', null=True, blank=True, verbose_name='会員')
    comment = models.TextField(blank=True, verbose_name='コメント')
    class Meta:
        verbose_name_plural='コメント'

class CommentImage(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='comment_images')
    imgs = models.ImageField(upload_to='comment')
    class Meta:
        verbose_name_plural='画像'

class Banner(models.Model):
    image = models.ImageField(upload_to='topbanner', verbose_name='画像')
    url = models.CharField(blank=True)
    class Meta:
        verbose_name_plural = 'TOP上位のバナー'

from django.utils import timezone


class Column(models.Model):
    is_public = models.BooleanField(default=False, verbose_name='公開')
    title = models.CharField()
    hero_image = models.ImageField(upload_to='column/hero_images')
    cat_name = models.CharField(max_length=100)
    detail_image = models.ImageField(upload_to='column/detail_images')
    subtitle = models.CharField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'コラム'

class ColumnBlog(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='blog')
    imgs = models.ImageField(upload_to='column/blog_images')
    img_caption = models.CharField()
    description = models.TextField()
    class Meta:
        verbose_name_plural = 'コラムブログ'

class ReactionCatImage(models.Model):
    imgs = models.ImageField(upload_to='reaction/cat')
    class Meta:
        verbose_name_plural = '絵文字アイコン-猫ちゃん'

class ReactionFoodImage(models.Model):
    imgs = models.ImageField(upload_to='reaction/food')
    class Meta:
        verbose_name_plural = '絵文字アイコン-フード'

class ReactionHeartImage(models.Model):
    imgs = models.ImageField(upload_to='reaction/heart')
    class Meta:
        verbose_name_plural = '絵文字アイコン-気持ち'

class ReactionPartyImage(models.Model):
    imgs = models.ImageField(upload_to='reaction/party')
    class Meta:
        verbose_name_plural = '絵文字アイコン-パーティー'

class ReactionSeasonImage(models.Model):
    imgs = models.ImageField(upload_to='reaction/season')
    class Meta:
        verbose_name_plural = '絵文字アイコン-季節'

class ReactionWordImage(models.Model):
    imgs = models.ImageField(upload_to='reaction/word')
    class Meta:
        verbose_name_plural = '絵文字アイコン-メッセージ'