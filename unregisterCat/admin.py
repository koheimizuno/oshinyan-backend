from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import UnregisterShop, UnregisterShopImage, CatApply, CatApplyImage, ShopType

class CatApplyImageInline(admin.TabularInline):
    model = CatApplyImage
    extra = 0

class CatApplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_type', 'company_name', 'kanji_name', 'furi_name', 'email', 'shop_type', 'cat_info', 'catapply_with_images']
    def catapply_with_images(self, obj):
        images = obj.catapply_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    catapply_with_images.short_description = 'イメージ'
    inlines = [CatApplyImageInline]
admin.site.register(CatApply, CatApplyAdmin)

class UnregisterShopImageInline(admin.TabularInline):
    model = UnregisterShopImage
    extra = 0

class UnregisterShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop_permission', 'shop_name', 'prefecture', 'city', 'street', 'detail_address', 'email', 'phone', 'cat_info', 'shop_with_images', 'created_date']
    def shop_with_images(self, obj):
        images = obj.shop_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    shop_with_images.short_description = 'UnregisterShop Images'
    inlines = [UnregisterShopImageInline]
admin.site.register(UnregisterShop, UnregisterShopAdmin)

class ShopTypeOption(admin.ModelAdmin):
    list_display = [field.name for field in ShopType._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(ShopType, ShopTypeOption)