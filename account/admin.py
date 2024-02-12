from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Member, Avatar
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from django.contrib.admin import AdminSite

admin.site.site_header = "Oshinyan.love Administration"
admin.site.site_title = "Oshinyan.love"
admin.site.unregister(Group)

class CustomAdminSite(AdminSite):
    def has_module_permission(self, request):
        if request.user.has_perm('auth.view_authtoken'):
            return True
        return False

custom_admin_site = CustomAdminSite(name='customadmin')

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
    def image_preview(self, obj):
        if obj.avatar:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.avatar.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(Avatar, AvatarAdmin)