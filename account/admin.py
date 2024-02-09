from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Member, Avatar

admin.site.site_header = "Oshinyan.love Administration"
admin.site.site_title = "Oshinyan.love"

class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'avatar_preview', 'username', 'email', 'prefecture', 'is_active', 'is_staff', 'is_superuser', 'last_login']
    readonly_fields = ['avatar_preview']
    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe('<img src="{0}" style="max-height: 50px; max-width: 50px;" />'.format(obj.avatar.avatar.url))
        else:
            return 'No image'
    avatar_preview.short_description = 'プロフィール画像'

admin.site.register(Member, MemberAdmin)

class AvatarAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    readonly_fields = ['image_preview']
    def has_change_permission(self, request, obj=None):
        return False
    def image_preview(self, obj):
        if obj.avatar:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.avatar.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(Avatar, AvatarAdmin)