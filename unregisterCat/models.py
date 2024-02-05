from django.db import models

PREFECTURE_CHOICES = (
    ('北海道', '北海道'),
    ('青森県', '青森県'),
    ('岩手県', '岩手県'),
    ('宮城県', '宮城県'),
    ('秋田県', '秋田県'),
    ('山形県', '山形県'),
    ('福島県', '福島県'),
    ('茨城県', '茨城県'),
    ('栃木県', '栃木県'),
    ('群馬県', '群馬県'),
    ('埼玉県', '埼玉県'),
    ('千葉県', '千葉県'),
    ('東京都', '東京都'),
    ('神奈川県', '神奈川県'),
    ('山梨県', '山梨県'),
    ('長野県', '長野県'),
    ('新潟県', '新潟県'),
    ('富山県', '富山県'),
    ('石川県', '石川県'),
    ('福井県', '福井県'),
    ('岐阜県', '岐阜県'),
    ('静岡県', '静岡県'),
    ('愛知県', '愛知県'),
    ('三重県', '三重県'),
    ('滋賀県', '滋賀県'),
    ('京都府', '京都府'),
    ('大阪府', '大阪府'),
    ('兵庫県', '兵庫県'),
    ('奈良県', '奈良県'),
    ('和歌山県', '和歌山県'),
    ('鳥取県', '鳥取県'),
    ('島根県', '島根県'),
    ('岡山県', '岡山県'),
    ('広島県', '広島県'),
    ('山口県', '山口県'),
    ('徳島県', '徳島県'),
    ('香川県', '香川県'),
    ('愛媛県', '愛媛県'),
    ('高知県', '高知県'),
    ('福岡県', '福岡県'),
    ('佐賀県', '佐賀県'),
    ('長崎県', '長崎県'),
    ('熊本県', '熊本県'),
    ('大分県', '大分県'),
    ('宮崎県', '宮崎県'),
    ('鹿児島県', '鹿児島県'),
    ('沖縄県', '沖縄県'),
)

CLIENT_TYPE_CHOICES = (
    ('個人','個人'),
    ('法人', '法人'),
)

SHOP_TYPE_CHOICES = (
    ('カフェ', 'カフェ'),
)

class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    prefecture = models.CharField(max_length=100, choices=PREFECTURE_CHOICES, default='北海道')
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=200, blank=True)
    detail_address = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    shop_permission = models.BooleanField(default=False)
    cat_info = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "未登録店舗"

    def __str__(self):
        return self.shop_name

class ShopImage(models.Model):
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='shop_images')
    imgs = models.ImageField(blank=False, upload_to='uploads/shop_images')

    class Meta:
        verbose_name_plural = "未登録店舗画像"

    def __int__(self):
        return self.shop
    
class CatApplication(models.Model):
    is_public = models.BooleanField(default=False)
    client_type = models.CharField(max_length=6, choices=CLIENT_TYPE_CHOICES, default='個人')
    company_name = models.CharField(max_length=100, blank=True)
    kanji_name = models.CharField(max_length=100, blank=True)
    furi_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    shop_type = models.CharField(max_length=100, choices=SHOP_TYPE_CHOICES, default='カフェ')
    cat_info = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "推しニャン申請"