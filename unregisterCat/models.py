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
    shop_type = models.CharField(max_length=100, choices=SHOP_TYPE_CHOICES, default='カフェ', verbose_name='場所種別')
    cat_info = models.TextField(blank=True, verbose_name='看板猫情報')
    class Meta:
        verbose_name_plural = "推しニャン申請"

class CatApplyImage(models.Model):
    cat = models.ForeignKey(
        CatApply, on_delete=models.CASCADE, related_name='catapply_images')
    imgs = models.ImageField(blank=False, upload_to='catapply')
    class Meta:
        verbose_name_plural = "画像"