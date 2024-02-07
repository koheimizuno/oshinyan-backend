from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Ambassador, Inquiry, Banner, AdvertiseImage, Advertise

class AmbassadorOption(admin.ModelAdmin):
    list_display = [field.name for field in Ambassador._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Ambassador, AmbassadorOption)

class InquiryOption(admin.ModelAdmin):
    list_display = [field.name for field in Inquiry._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Inquiry, InquiryOption)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview', 'url']
    readonly_fields = ['image_preview']
    def has_change_permission(self, request, obj=None):
        return False
    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url))
        else:
            return '(No image)'
    image_preview.short_description = 'Image Preview'
admin.site.register(Banner, BannerAdmin)

class AdvertiseImageInline(admin.TabularInline):
    model = AdvertiseImage
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop', 'cat_name', 'display_character', 'display_favoritething', 'attendance', 'formatted_description', 'cat_with_images', 'cat_with_images_admin']
    filter_horizontal = ('character', 'favorite_things',)
    def display_character(self, obj):
        return ', '.join([character.character for character in obj.character.all()])
    display_character.short_description = 'Character'
    
    def display_favoritething(self, obj):
        return ', '.join([favorite_things.favorite_things for favorite_things in obj.favorite_things.all()])
    display_favoritething.short_description = 'Favorite_things'

    def formatted_description(self, obj):
        max_length = 50
        description = obj.description
        if len(description) > max_length:
            return mark_safe(f'{description[:max_length]}...')
        return description

    formatted_description.short_description = 'Description'
    
    def cat_with_images(self, obj):
        images = obj.cat_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px; margin : 1px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    cat_with_images.short_description = 'イメージ'

    def cat_with_images_admin(self, obj):
        images = obj.cat_admin_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px; margin : 1px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    cat_with_images_admin.short_description = 'イメージ'
    
    inlines = [AdvertiseImageInline]
admin.site.register(Advertise, AdvertiseAdmin)