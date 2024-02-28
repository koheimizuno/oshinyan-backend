from django.db import models
from django.core.validators import FileExtensionValidator
from account.models import Member
from utils.constants import PREFECTURE_CHOICES, ATTENDANCE_CHOICES, CAT_GENDER
from django_resized import ResizedImageField

# Banner Start
class Banner(models.Model):
    image = ResizedImageField(force_format="WEBP", quality=75, upload_to="topbanner", verbose_name='画像')
    url = models.CharField(blank=True)
    class Meta:
        verbose_name_plural = 'TOP上位のバナー'
# Banner End

# Shop Start
class ShopType(models.Model):
    shop_type = models.CharField(max_length=15, verbose_name='店舗種別')
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
    url = models.URLField(blank=True, verbose_name='店舗ホームページ')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = "店舗"
    def __str__(self):
        return self.shop_name

class ShopImage(models.Model):
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='shop_images', verbose_name='店舗')
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="shop")
    class Meta:
        verbose_name_plural = "店舗画像"
    def __int__(self):
        return self.shop
# Shop End

# Cat Start
class Character(models.Model):
    character = models.CharField(max_length=100, verbose_name='性格')
    class Meta:
        verbose_name_plural='性格'
    def __str__(self):
        return self.character
    
class Cat(models.Model):
    is_public = models.BooleanField(default=False, verbose_name='公開')
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='cat', verbose_name='店舗')
    cat_name = models.CharField(max_length=100, verbose_name='猫の名前')
    gender = models.CharField(max_length=6, choices=CAT_GENDER, default='男の子', verbose_name='性別', blank=True, null=True)
    birthday = models.DateField(verbose_name='生年月日', blank=True, null=True)
    character = models.ManyToManyField(Character, verbose_name='性格')
    favorite_things = models.TextField(verbose_name='好きなもの・コト', null=True, blank=True)
    attendance = models.CharField(max_length=20, choices=ATTENDANCE_CHOICES, default='100%います', verbose_name='出没頻度')
    description = models.TextField(verbose_name='猫の説明')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural='看板猫'
    def __str__(self):
        return self.cat_name
    def __int__(self):
        return self.cat_name
    
class CatImage(models.Model):
    cat = models.ForeignKey(
        Cat, on_delete=models.CASCADE, related_name='images')
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="cat/images")
    def __int__(self):
        return f"Image of {self.cat}"
    class Meta:
        verbose_name_plural='看板猫画像'
    
class CatImageByAdmin(models.Model):
    cat = models.ForeignKey(
        Cat, on_delete=models.CASCADE, related_name='admin_images')
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="cat/admin_images")
    def __int__(self):
        return f"Image of {self.cat}"
    class Meta:
        verbose_name_plural='画像'
# Cat Start

# Advertise Start
class Advertise(models.Model):
    is_public = models.BooleanField(default=False, verbose_name='公開')
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='advertise_cat', null=True, blank=True, verbose_name='店舗')
    cat_name = models.CharField(max_length=100, blank=True, verbose_name='猫の名前')
    character = models.ManyToManyField(Character, verbose_name='性格')
    favorite_things = models.TextField(verbose_name='好きなもの・コト', null=True, blank=True)
    attendance = models.CharField(max_length=20, choices=ATTENDANCE_CHOICES, default='毎日', verbose_name='出没頻度')
    description = models.TextField(blank=True, verbose_name='猫の説明')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural='広告看板猫'
    def __str__(self):
        return self.cat_name
    def __int__(self):
        return self.cat_name
    
class AdvertiseImage(models.Model):
    cat = models.ForeignKey(
        Advertise, on_delete=models.CASCADE, related_name='images')
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="advertise/images")
    class Meta:
        verbose_name_plural = '画像'
    
class AdvertiseImageByAdmin(models.Model):
    cat = models.ForeignKey(
        Advertise, on_delete=models.CASCADE, related_name='admin_images')
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="advertise/admin_images")
    def __int__(self):
        return f"Image of {self.cat}"
    class Meta:
        verbose_name_plural='画像'
# Advertise Start

# Recommend Start
class Recommend(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='recommend', null=True, blank=True, verbose_name='看板猫')
    advertise = models.ForeignKey(Advertise, on_delete=models.CASCADE, related_name='recommend', null=True, blank=True, verbose_name='広告猫')
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='recommend', null=True, blank=True, verbose_name='会員')
    class Meta:
        verbose_name_plural='推し'
    def __int__(self):
        return self.user
# Recommend End
    
# Column Start
class Column(models.Model):
    public_date = models.DateTimeField(blank=True, null=True, verbose_name='公開日時')
    title = models.TextField(max_length=40, verbose_name='タイトル')
    hero_image = ResizedImageField(force_format="WEBP", quality=75, upload_to="column/hero_images", )
    cat_name = models.CharField(max_length=100, verbose_name='猫の名前')
    detail_image = ResizedImageField(force_format="WEBP", quality=75, upload_to="column/detail_images")
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'コラム'

class ColumnBlog(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='blog', verbose_name='コラム')
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="column/blog_images")
    img_caption = models.TextField(max_length=200, verbose_name='画像キャプション')
    description = models.TextField(verbose_name='猫の説明')
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        verbose_name_plural = 'コラムブログ'
        ordering = ['id']
# Column End

# Comment Start
class Comment(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='comment', null=True, blank=True, verbose_name='看板猫')
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comment', null=True, blank=True, verbose_name='会員')
    comment = models.TextField(blank=True, verbose_name='コメント')
    class Meta:
        verbose_name_plural='コメント'

class CommentImage(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='comment_images', verbose_name='コメント')
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="comment")
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural='コメント画像'

class CommentImageRecommend(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True, verbose_name='会員')
    comment_image = models.ForeignKey(CommentImage, related_name='comment_images_recommend', on_delete=models.CASCADE, null=True, blank=True, verbose_name='コメント画像')
    class Meta:
        verbose_name_plural='コメント画像推し'

class CommentReactionIcon(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_reaction_icon', null=True, blank=True, verbose_name='コメント')
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True, verbose_name='会員')
    imgs = models.URLField()
    class Meta:
        verbose_name_plural = 'コメント アイコン'

class ReactionCatIcon(models.Model):
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="reaction/cat")
    class Meta:
        verbose_name_plural = '絵文字アイコン-猫ちゃん'

class ReactionFoodIcon(models.Model):
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="reaction/food")
    class Meta:
        verbose_name_plural = '絵文字アイコン-フード'

class ReactionHeartIcon(models.Model):
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to="reaction/heart")
    class Meta:
        verbose_name_plural = '絵文字アイコン-気持ち'

class ReactionPartyIcon(models.Model):
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to='reaction/party')
    class Meta:
        verbose_name_plural = '絵文字アイコン-パーティー'

class ReactionSeasonIcon(models.Model):
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to='reaction/season')
    class Meta:
        verbose_name_plural = '絵文字アイコン-季節'

class ReactionWordIcon(models.Model):
    imgs = ResizedImageField(force_format="WEBP", quality=75, upload_to='reaction/word')
    class Meta:
        verbose_name_plural = '絵文字アイコン-メッセージ'
# Comment End

# Notice Start
class Notice(models.Model):
    title = models.TextField(max_length=40, verbose_name='タイトル')
    pdf = models.FileField(upload_to='notice', validators=[FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='PDF', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='登録日時')
    class Meta:
        verbose_name_plural = 'お知らせ'
# Notice End
        
# Feature Start
class Feature(models.Model):
    title = models.CharField(max_length=50, verbose_name='特集タイトル')
    description = models.TextField(max_length=300, verbose_name='特集説明')
    prefecture = models.CharField(max_length=100, choices=PREFECTURE_CHOICES, verbose_name='都道府県', blank=True, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='feature', verbose_name='性格', blank=True,  null=True)
    image = models.ForeignKey(CatImage, on_delete=models.CASCADE, related_name='feature_image', verbose_name='特集画像', null=True)
    class Meta:
        verbose_name_plural = '特集'
# Feature End