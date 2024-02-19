from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Member, Avatar
from django.contrib.auth.models import Group
from django.contrib.admin import AdminSite
from django.http import HttpResponse
import csv
import codecs
import urllib.parse

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
    list_display = ['id', 'avatar_preview', 'username', 'email', 'prefecture', 'is_active', 'is_staff', 'is_superuser', 'created_date']
    readonly_fields = ['avatar_preview']
    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe('<img src="{0}" style="max-height: 50px; max-width: 50px;" />'.format(obj.avatar.avatar.url))
        else:
            return 'No image'
    avatar_preview.short_description = 'プロフィール画像'
    
    actions = ['export_selected_objects']
    field_mappings = {
        'username': 'ニックネーム',
        'email': 'メールアドレス',
        'prefecture': '居住エリア',
        'avatar': 'プロフィール画像',
    }

    def export_selected_objects(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        japanese_filename = "会員データ.csv"
        encoded_filename = urllib.parse.quote(japanese_filename.encode('utf-8'))
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(encoded_filename)
        response.write(codecs.BOM_UTF8)  # Add BOM to ensure CSV opens correctly in Excel
        writer = csv.writer(response, delimiter=',')
        # Write header
        custom_header = [self.field_mappings.get(field.name, field.name) for field in queryset.model._meta.fields]
        custom_header.append('プロフィール画像')  # Add 'プロフィール画像' to the header
        writer.writerow(custom_header)
        # Write data
        for obj in queryset:
            row_data = [getattr(obj, field.name) for field in queryset.model._meta.fields]
            # Append the avatar field value from the associated Avatar model
            avatar_value = obj.avatar.avatar.url if obj.avatar else ''  # Get the avatar URL if available
            row_data.append(avatar_value)
            writer.writerow(row_data)
        return response
    export_selected_objects.short_description = "会員データのダウンロード"

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