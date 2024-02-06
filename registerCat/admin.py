from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Cat, CatImage, CatImageByAdmin, Character, FavoriteThing, Recommend, Comment, CommentImage

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
    list_display = ['id', 'shop', 'cat_name', 'display_character', 'display_favoritething', 'attendance', 'formatted_description', 'cat_with_images', 'cat_with_images_admin']
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
    list_display = ['id', 'comment', 'user', 'cat', 'comment_with_images']
    def comment_with_images(self, obj):
        images = obj.comment_images.all()
        if images:
            return mark_safe(''.join('<img src="{0}" style="max-width:100px; max-height:100px;">'.format(img.imgs.url) for img in images))
        return 'No Images'
    comment_with_images.short_description = 'Comment Images'
    inlines = [CommentImageInline]
admin.site.register(Comment, CommentAdmin)