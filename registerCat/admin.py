from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from . import models

# Shop Start
class ShopImageInline(admin.TabularInline):
    model = models.ShopImage
    extra = 0

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'shop_type', 'shop_name', 'prefecture', 'address', 'nearest_station', 'phone', 'business_time', 'rest_day', 'url', 'shop_with_images']
    def shop_with_images(self, obj):
        images = obj.shop_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    shop_with_images.short_description = '店舗画像'
    inlines = [ShopImageInline]
admin.site.register(models.Shop, ShopAdmin)
# Shop End

# Banner Start
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview', 'url']
    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url))
        else:
            return '(No image)'
    image_preview.short_description = '画像'
admin.site.register(models.Banner, BannerAdmin)
# Banner End

# Cat Start
class CharacterOption(admin.ModelAdmin):
    list_display = [field.name for field in models.Character._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(models.Character, CharacterOption)

class CatImageByAdminInline(admin.TabularInline):
    model = models.CatImageByAdmin
    extra = 1

class CatImageInline(admin.TabularInline):
    model = models.CatImage
    extra = 1

class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'shop', 'cat_name', 'display_character', 'favorite_things', 'attendance', 'formatted_description', 'cat_with_images', 'cat_with_images_admin', 'design_test']
    filter_horizontal = ('character',)

    def design_test(self, obj):
        button_html = '<a class="button" href="http://oshinyan.love/test" target="_blank">デザイン確認</a>'
        return mark_safe(button_html)
    design_test.short_description = 'Custom Link Button'

    def display_character(self, obj):
        return ', '.join([character.character for character in obj.character.all()])
    display_character.short_description = '性格'

    def formatted_description(self, obj):
        max_length = 50
        description = obj.description
        if len(description) > max_length:
            return mark_safe(f'{description[:max_length]}...')
        return description
    formatted_description.short_description = '猫の説明'
    
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
# Cat End

# Advertise Start
class AdvertiseImageInline(admin.TabularInline):
    model = models.AdvertiseImage
    extra = 1

class AdvertiseImageByAdminInline(admin.TabularInline):
    model = models.AdvertiseImageByAdmin
    extra = 1

class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'shop', 'cat_name', 'display_character', 'attendance', 'formatted_description', 'advertise_with_images', 'advertise_with_images_admin']
    filter_horizontal = ('character',)
    def display_character(self, obj):
        return ', '.join([character.character for character in obj.character.all()])
    display_character.short_description = 'Character'

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
# Advertise End

# Recommend Start
class RecommendOption(admin.ModelAdmin):
    list_display = [field.name for field in models.Recommend._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(models.Recommend, RecommendOption)
# Recommend End

# Column Start
class ColumnBlogInline(admin.TabularInline):
    model = models.ColumnBlog
    extra = 0

class ColumnAdmin(admin.ModelAdmin):
    list_display = ['id', 'public_date', 'title', 'hero_image_preview', 'cat_name', 'detail_image_preview','created_date', 'display_column_blogs']

    def hero_image_preview(self, obj):
            if obj.hero_image:
                return mark_safe('<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(obj.hero_image.url))
            else:
                return '(No image)'
    hero_image_preview.short_description = '画像'

    def detail_image_preview(self, obj):
            if obj.detail_image:
                return mark_safe('<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(obj.detail_image.url))
            else:
                return '(No image)'
    detail_image_preview.short_description = '詳細画像'

    def display_column_blogs(self, obj):
        column_blogs = obj.blog.all()  # assuming 'blog' is the related_name for ForeignKey in ColumnBlog model
        html = ''
        for column_blog in column_blogs:
            truncated_description = column_blog.description[:50] + ('...' if len(column_blog.description) > 50 else '')
            html += f'<img src="{column_blog.imgs.url}" width="100" height="100">'
            html += f'<p>{column_blog.img_caption}</p>'
            html += f'<p>{truncated_description}</p>'
        return mark_safe(html)
    display_column_blogs.short_description = 'コラムブログ'
    
    inlines = [ColumnBlogInline]
admin.site.register(models.Column, ColumnAdmin)
# Column End

# Comment Start
class CommentImageInline(admin.TabularInline):
    model = models.CommentImage
    extra = 0

class CommentReactionIconInline(admin.TabularInline):
    model = models.CommentReactionIcon
    extra = 0

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'cat', 'formatted_comment', 'comment_with_images', 'comment_reaction_icon']
    def formatted_comment(self, obj):
        max_length = 50
        comment = obj.comment
        if len(comment) > max_length:
            return mark_safe(f'{comment[:max_length]}...')
        return comment
    formatted_comment.short_description = 'コメント説明'
    def comment_with_images(self, obj):
        images = obj.comment_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    comment_with_images.short_description = 'コメント画像'
    def comment_reaction_icon(self, obj):
        images = obj.comment_reaction_icon.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:30px; max-height:30px; margin: 0 5px;">'.format(img.imgs) for img in images))
        return 'No Images'
    comment_reaction_icon.short_description = 'コメント画像'
    inlines = [CommentImageInline, CommentReactionIconInline]
admin.site.register(models.Comment, CommentAdmin)

class ReactionCatIconAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionCatIcon, ReactionCatIconAdmin)

class ReactionFoodIconAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionFoodIcon, ReactionFoodIconAdmin)

class ReactionSeasonIconAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionSeasonIcon, ReactionSeasonIconAdmin)

class ReactionHeartIconAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionHeartIcon, ReactionHeartIconAdmin)

class ReactionWordIconAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionWordIcon, ReactionWordIconAdmin)

class ReactionPartyIconAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview']
    def image_preview(self, obj):
        if obj.imgs:
            return mark_safe('<img src="{0}" style="max-height: 40px; max-width: 40px;" />'.format(obj.imgs.url))
        else:
            return '(No image)'
    image_preview.short_description = 'プロフィール画像'
admin.site.register(models.ReactionPartyIcon, ReactionPartyIconAdmin)
# Comment End

# Notice Start
class NoticeOption(admin.ModelAdmin):
    list_display = [field.name for field in models.Notice._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(models.Notice, NoticeOption)
# Notice End

# Feature Start
class FeatureAdminForm(forms.ModelForm):
    class Meta:
        model = models.Feature
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the 'image' field to display images from CatImage
        self.fields['image'].queryset = models.CatImage.objects.all()

class FeatureOption(admin.ModelAdmin):
    list_display = ['id', 'title', 'prefecture', 'character', 'formatted_description', 'display_image']
    form = FeatureAdminForm
    def formatted_description(self, obj):
        max_length = 50
        description = obj.description
        if len(description) > max_length:
            return mark_safe(f'{description[:max_length]}...')
        return description
    def display_image(self, obj):
        if obj.image:
            return mark_safe('<img src="{0}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.imgs.url))
        else:
            return 'No image'
    display_image.short_description = 'サムネイル画像'
    
admin.site.register(models.Feature, FeatureOption)
# Feature End