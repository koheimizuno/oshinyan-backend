from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Ambassador, Inquiry, Banner, Advertise

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

class AdvertiseAdmin(admin.ModelAdmin):
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
admin.site.register(Advertise, AdvertiseAdmin)