from django.contrib import admin
from .models import Shop, ShopImage, CatApplication
 
class ShopOption(admin.ModelAdmin):
    list_display = [field.name for field in Shop._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Shop, ShopOption)

class ShopImageOption(admin.ModelAdmin):
    list_display = [field.name for field in ShopImage._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(ShopImage, ShopImageOption)

class CatApplicationOption(admin.ModelAdmin):
    list_display = [field.name for field in CatApplication._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(CatApplication, CatApplicationOption)
