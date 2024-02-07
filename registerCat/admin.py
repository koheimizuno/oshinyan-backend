from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Cat, CatImage, CatImageByAdmin, Character, FavoriteThing, Recommend, Comment, CommentImage,AdvertiseImage, Advertise

class CatImageByAdminInline(admin.TabularInline):
    model = CatImageByAdmin
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class CatImageInline(admin.TabularInline):
    model = CatImage
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'shop', 'cat_name', 'display_character', 'display_favoritething', 'attendance', 'formatted_description', 'cat_with_images', 'cat_with_images_admin']
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
    
    inlines = [CatImageInline, CatImageByAdminInline]
admin.site.register(Cat, CatAdmin)

class RecommendOption(admin.ModelAdmin):
    list_display = [field.name for field in Recommend._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Recommend, RecommendOption)

class CharacterOption(admin.ModelAdmin):
    list_display = [field.name for field in Character._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Character, CharacterOption)

class FavoriteThingOption(admin.ModelAdmin):
    list_display = [field.name for field in FavoriteThing._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(FavoriteThing, FavoriteThingOption)

class CommentImageInline(admin.TabularInline):
    model = CommentImage
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
admin.site.register(Comment, CommentAdmin)

class AdvertiseImageInline(admin.TabularInline):
    model = AdvertiseImage
    extra = 1
    # def has_change_permission(self, request, obj=None):
    #     return False

class AdvertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'shop', 'cat_name', 'display_character', 'display_favoritething', 'attendance', 'formatted_description', 'advertise_with_images']
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
        images = obj.advertise_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px; margin : 1px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    advertise_with_images.short_description = 'イメージ'
    
    inlines = [AdvertiseImageInline]
admin.site.register(Advertise, AdvertiseAdmin)