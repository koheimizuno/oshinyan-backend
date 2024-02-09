from django.db import models
from utils.constants import PREFECTURE_CHOICES, CLIENT_TYPE_CHOICES, SHOP_TYPE_CHOICES
from registerCat.models import ShopType

class UnregisterShop(models.Model):
    shop_name = models.CharField(max_length=100, verbose_name='店舗名')
    prefecture = models.CharField(max_length=100, choices=PREFECTURE_CHOICES, default='北海道', verbose_name='都道府県')
    city = models.CharField(max_length=100, blank=True, verbose_name='市区町村')
    street = models.CharField(max_length=200, blank=True, verbose_name='番地')
    detail_address = models.CharField(max_length=200, blank=True, verbose_name='建物名・部屋番号')
    email = models.EmailField(verbose_name='メールアドレス（登録者）')
    phone = models.CharField(max_length=20, blank=True, verbose_name='電話番号（登録者）')
    shop_permission = models.BooleanField(default=False, verbose_name='店舗の許諾')
    cat_info = models.TextField(verbose_name='看板猫情報')
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "未登録店舗"

    def __str__(self):
        return self.shop_name

class UnregisterShopImage(models.Model):
    shop = models.ForeignKey(
        UnregisterShop, on_delete=models.CASCADE, related_name='shop_images')
    imgs = models.ImageField(blank=False, upload_to='unregistershop')

    class Meta:
        verbose_name_plural = "画像"

    def __int__(self):
        return self.shop

class CatApply(models.Model):
    client_type = models.CharField(max_length=6, choices=CLIENT_TYPE_CHOICES, default='個人', verbose_name='個人／法人のお客さま')
    company_name = models.CharField(max_length=100, blank=True, verbose_name='会社名・法人名')
    kanji_name = models.CharField(max_length=100, blank=True, verbose_name='氏名（漢字）')
    furi_name = models.CharField(max_length=100, blank=True, verbose_name='氏名（ふりがな）')
    email = models.EmailField(blank=True, verbose_name='メールアドレス')
    shop_type = models.ForeignKey(
        ShopType, on_delete=models.CASCADE, related_name='catapply', verbose_name='場所種別', blank=True)
    cat_info = models.TextField(blank=True, verbose_name='看板猫情報')
    class Meta:
        verbose_name_plural = "推しニャン申請"

class CatApplyImage(models.Model):
    cat = models.ForeignKey(
        CatApply, on_delete=models.CASCADE, related_name='catapply_images')
    imgs = models.ImageField(blank=False, upload_to='catapply')
    class Meta:
        verbose_name_plural = "画像"
