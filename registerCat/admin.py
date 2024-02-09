from django.core.exceptions import ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

class CatImageByAdminInline(admin.TabularInline):
    model = models.CatImageByAdmin
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class CatImageInline(admin.TabularInline):
    model = models.CatImage
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'shop', 'cat_name', 'display_character', 'display_favoritething', 'attendance', 'formatted_description', 'cat_with_images', 'cat_with_images_admin']
    filter_horizontal = ('character', 'favorite_things',)
    def display_character(self, obj):
        return ', '.join([character.character for character in obj.character.all()])
    display_character.short_description = '性格'
    
    def display_favoritething(self, obj):
        return ', '.join([favorite_things.favorite_things for favorite_things in obj.favorite_things.all()])
    display_favoritething.short_description = '好きなもの・コト'

    def formatted_description(self, obj):
        max_length = 50
        description = obj.description
        if len(description) > max_length:
            return mark_safe(f'{description[:max_length]}...')
        return description

    formatted_description.short_description = 'Description'
    
    def cat_with_images(self, obj):
        images = obj.images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px; margin : 1px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    cat_with_images.short_description = '画像'

    def cat_with_images_admin(self, obj):
        images = obj.admin_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px; margin : 1px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    cat_with_images_admin.short_description = '画像'
    
    inlines = [CatImageInline, CatImageByAdminInline]
admin.site.register(models.Cat, CatAdmin)

class RecommendOption(admin.ModelAdmin):
    list_display = [field.name for field in models.Recommend._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(models.Recommend, RecommendOption)

class CharacterOption(admin.ModelAdmin):
    list_display = [field.name for field in models.Character._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(models.Character, CharacterOption)

class FavoriteThingOption(admin.ModelAdmin):
    list_display = [field.name for field in models.FavoriteThing._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(models.FavoriteThing, FavoriteThingOption)

class CommentImageInline(admin.TabularInline):
    model = models.CommentImage
    extra = 0
    def has_change_permission(self, request, obj=None):
        return False

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cat', 'formatted_comment', 'comment_with_images']
    def formatted_comment(self, obj):
        max_length = 50
        comment = obj.comment
        if len(comment) > max_length:
            return mark_safe(f'{comment[:max_length]}...')
        return comment

    formatted_comment.short_description = 'Description'
    def comment_with_images(self, obj):
        images = obj.comment_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    comment_with_images.short_description = 'Comment Images'
    inlines = [CommentImageInline]
admin.site.register(models.Comment, CommentAdmin)

class AdvertiseImageInline(admin.TabularInline):
    model = models.AdvertiseImage
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class AdvertiseImageByAdminInline(admin.TabularInline):
    model = models.AdvertiseImageByAdmin
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'shop', 'cat_name', 'display_character', 'display_favoritething', 'attendance', 'formatted_description', 'advertise_with_images', 'advertise_with_images_admin']
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
    
    def advertise_with_images(self, obj):
        images = obj.images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px; margin : 1px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    advertise_with_images.short_description = '画像'

    def advertise_with_images_admin(self, obj):
        images = obj.admin_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px; margin : 1px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    advertise_with_images_admin.short_description = '画像'
    
    inlines = [AdvertiseImageInline, AdvertiseImageByAdminInline]
admin.site.register(models.Advertise, AdvertiseAdmin)

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
admin.site.register(models.Banner, BannerAdmin)

class ColumnBlogInline(admin.TabularInline):
    model = models.ColumnBlog
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class ColumnAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'title', 'hero_image_preview', 'cat_name', 'detail_image_preview', 'subtitle', 'formatted_description', 'display_column_blogs']
    def formatted_description(self, obj):
        max_length = 50
        description = obj.description
        if len(description) > max_length:
            return mark_safe(f'{description[:max_length]}...')
        return description
    formatted_description.short_description = 'Description'

    def hero_image_preview(self, obj):
            if obj.hero_image:
                return mark_safe('<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(obj.hero_image.url))
            else:
                return '(No image)'
    hero_image_preview.short_description = 'Image Preview'

    def detail_image_preview(self, obj):
            if obj.detail_image:
                return mark_safe('<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(obj.detail_image.url))
            else:
                return '(No image)'
    detail_image_preview.short_description = 'Image Preview'
    
    def display_column_blogs(self, obj):
        column_blogs = obj.blog.all()  # assuming 'blog' is the related_name for ForeignKey in ColumnBlog model
        html = ''
        for column_blog in column_blogs:
            truncated_description = column_blog.description[:50] + ('...' if len(column_blog.description) > 50 else '')
            html += f'<img src="{column_blog.imgs.url}" width="100" height="100">'
            html += f'<p>{column_blog.img_caption}</p>'
            html += f'<p>{truncated_description}</p>'
        return mark_safe(html)
    display_column_blogs.short_description = 'Column Blogs'
    
    inlines = [ColumnBlogInline]
admin.site.register(models.Column, ColumnAdmin)

class ColumnBlogOption(admin.ModelAdmin):
    list_display = [field.name for field in models.ColumnBlog._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(models.ColumnBlog, ColumnBlogOption)

class ShopImageInline(admin.TabularInline):
    model = models.ShopImage
    extra = 0
    def has_change_permission(self, request, obj=None):
        return False

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop_name', 'prefecture', 'address', 'nearest_station', 'phone', 'business_time', 'rest_day', 'url', 'shop_with_images', 'last_update']
    def shop_with_images(self, obj):
        images = obj.shop_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    shop_with_images.short_description = 'Shop Images'
    inlines = [ShopImageInline]
admin.site.register(models.Shop, ShopAdmin)

class ReactionCatImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    readonly_fields = ['image_preview']
    def has_change_permission(self, request, obj=None):
        return False
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionCatImage, ReactionCatImageAdmin)

class ReactionFoodImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    readonly_fields = ['image_preview']
    def has_change_permission(self, request, obj=None):
        return False
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionFoodImage, ReactionFoodImageAdmin)

class ReactionSeasonImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    readonly_fields = ['image_preview']
    def has_change_permission(self, request, obj=None):
        return False
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionSeasonImage, ReactionSeasonImageAdmin)

class ReactionHeartImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    readonly_fields = ['image_preview']
    def has_change_permission(self, request, obj=None):
        return False
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionHeartImage, ReactionHeartImageAdmin)

class ReactionWordImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    readonly_fields = ['image_preview']
    def has_change_permission(self, request, obj=None):
        return False
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionWordImage, ReactionWordImageAdmin)

class ReactionPartyImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    readonly_fields = ['image_preview']
    def has_change_permission(self, request, obj=None):
        return False
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionPartyImage, ReactionPartyImageAdmin)