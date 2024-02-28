from django.db import models
from account.models import Member
from registerCat.models import Comment

CLIENT_TYPE_CHOICES = (
    ('個人','個人'),
    ('法人', '法人'),
)

class Ambassador(models.Model):
    ambassador_name = models.CharField(max_length=100, verbose_name='アンバサダー名')
    full_name = models.CharField(max_length=100, blank=True, verbose_name='氏名')
    prefecture = models.CharField(max_length=100, verbose_name='都道府県')
    city = models.CharField(max_length=100, blank=True, verbose_name='市区町村')
    street = models.CharField(max_length=200, blank=True, verbose_name='番地')
    other_address = models.CharField(max_length=200, blank=True, verbose_name='建物名・部屋番号')
    email = models.EmailField(verbose_name='メールアドレス')
    phone = models.CharField(max_length=20, blank=True, verbose_name='電話番号')
    preferred = models.TextField(verbose_name='ご希望')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'アンバサダー'
    def __str__(self):
        return self.ambassador_name

class Inquiry(models.Model):
    type = models.CharField(max_length=100, verbose_name='問い合わせ種別')
    client_type = models.CharField(max_length=6, choices=CLIENT_TYPE_CHOICES, default='個人', verbose_name='個人／法人のお客さま')
    company_name = models.CharField(max_length=100, verbose_name='会社名・法人名')
    kanji_name = models.CharField(max_length=100, verbose_name='氏名（漢字）')
    furi_name = models.CharField(max_length=100, verbose_name='氏名（ふりがな）')
    phone = models.CharField(max_length=100, verbose_name='電話番号')
    email = models.EmailField(unique=True, verbose_name='メールアドレス')
    detail = models.TextField(verbose_name='お問合わせ内容')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'お問い合わせ'

class Report(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True, verbose_name='会員')
    url = models.CharField(blank=True)
    kanji_name = models.CharField(max_length=100, verbose_name='氏名（漢字）', null=True)
    furi_name = models.CharField(max_length=100, verbose_name='氏名（ふりがな）', null=True)
    phone = models.CharField(max_length=20, verbose_name='電話番号（登録者）', null=True)
    email = models.EmailField(verbose_name='メールアドレス', null=True)
    content = models.TextField(verbose_name='猫の説明', null=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='report', verbose_name='コメント', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='登録日時')
    class Meta:
        verbose_name_plural='通報一覧'