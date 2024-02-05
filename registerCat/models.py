from django.db import models
from account.models import Member
from unregisterCat.models import Shop

CLIENT_TYPE_CHOICES = (
    ('個人','個人'),
    ('法人', '法人'),
)

SHOP_TYPE_CHOICES = (
    ('カフェ', 'カフェ'),
)

ATTENDANCE_CHOICES = (
    ('毎日','毎日'),
    ('二日', '二日'),
    ('三日', '三日'),
    ('四日', '四日'),
)

class Character(models.Model):
    character = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='性格'
    def __str__(self):
        return self.character
    
class FavoriteThing(models.Model):
    favorite_things = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='好きなもの・コト'
    def __str__(self):
        return self.favorite_things
    
class Cat(models.Model):
    is_public = models.BooleanField(default=False)
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='cat', null=True, blank=True)
    cat_name = models.CharField(max_length=100, blank=True)
    character = models.ManyToManyField(Character)
    favorite_things = models.ManyToManyField(FavoriteThing)
    attendance = models.CharField(max_length=6, choices=ATTENDANCE_CHOICES, default='毎日')
    comment = models.TextField(blank=True)
    description = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='看板猫'
    def __str__(self):
        return self.cat_name
    def __int__(self):
        return self.cat_name
    
class CatImage(models.Model):
    cat = models.ForeignKey(
        Cat, on_delete=models.CASCADE, related_name='cat_images')
    imgs = models.ImageField(blank=False, upload_to='uploads/cat_images')
    def __int__(self):
        return f"Image of {self.cat.name}"
    
class CatImageByAdmin(models.Model):
    cat = models.ForeignKey(
        Cat, on_delete=models.CASCADE, related_name='cat_admin_images')
    imgs = models.ImageField(blank=False, upload_to='uploads/cat_admin_images')
    def __int__(self):
        return f"Image of {self.cat.name}"

class Recommend(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='recommend', null=True, blank=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='recommend', null=True, blank=True)
    class Meta:
        verbose_name_plural='推し'
    def __int__(self):
        return self.user_id