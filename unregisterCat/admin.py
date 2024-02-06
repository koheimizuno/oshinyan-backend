from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Shop, ShopImage, CatApply, CatApplyImage

class CatApplyImageInline(admin.TabularInline):
    model = CatApplyImage
    extra = 0
    def has_change_permission(self, request, obj=None):
        return False

class CatApplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'catapply_with_images']
    def catapply_with_images(self, obj):
        images = obj.catapply_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    catapply_with_images.short_description = 'イメージ'
    inlines = [CatApplyImageInline]
admin.site.register(CatApply, CatApplyAdmin)

class ShopImageInline(admin.TabularInline):
    model = ShopImage
    extra = 0
    def has_change_permission(self, request, obj=None):
        return False

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop_name', 'shop_with_images']
    def shop_with_images(self, obj):
        images = obj.shop_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    shop_with_images.short_description = 'Shop Images'
    inlines = [ShopImageInline]
admin.site.register(Shop, ShopAdmin)