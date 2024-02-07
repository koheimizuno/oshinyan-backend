from django.db import models
from unregisterCat.models import Shop
from registerCat.models import Character, FavoriteThing

CLIENT_TYPE_CHOICES = (
    ('個人','個人'),
    ('法人', '法人'),
)

class Ambassador(models.Model):
    ambassador_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, blank=True)
    prefecture = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=200, blank=True)
    other_address = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    preferred = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'アンバサダー'

    def __str__(self):
        return self.ambassador_name

class Inquiry(models.Model):
    type = models.CharField(max_length=100)
    client_type = models.CharField(max_length=6, choices=CLIENT_TYPE_CHOICES, default='個人')
    company_name = models.CharField(max_length=100)
    kanji_name = models.CharField(max_length=100)
    furi_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    detail = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'お問い合わせ'

class Banner(models.Model):
    image = models.ImageField(blank=False, upload_to='uploads/banner_images')
    url = models.CharField(blank=True)
    class Meta:
        verbose_name_plural = 'TOP上位のバナー'

ATTENDANCE_CHOICES = (
    ('毎日','毎日'),
    ('二日', '二日'),
    ('三日', '三日'),
    ('四日', '四日'),
)

class Advertise(models.Model):
    is_public = models.BooleanField(default=False)
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='advertise_cat', null=True, blank=True)
    cat_name = models.CharField(max_length=100, blank=True)
    character = models.ManyToManyField(Character)
    favorite_things = models.ManyToManyField(FavoriteThing)
    attendance = models.CharField(max_length=6, choices=ATTENDANCE_CHOICES, default='毎日')
    description = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='広告看板猫'
    def __str__(self):
        return self.cat_name
    def __int__(self):
        return self.cat_name
    
class AdvertiseImage(models.Model):
    cat = models.ForeignKey(
        Advertise, on_delete=models.CASCADE, related_name='advertise_images')
    imgs = models.ImageField(blank=False, upload_to='uploads/advertise_images')
    class Meta:
        verbose_name_plural = 'TOP中頃の広告'