from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Cat, CatImage, CatImageByAdmin, Character, FavoriteThing, Recommend, Comment, CommentImage

class CatImageInline(admin.TabularInline):
    model = CatImage
    extra = 1

class CatImageByAdminInline(admin.TabularInline):
    model = CatImageByAdmin
    extra = 1

class CatOption(admin.ModelAdmin):
    model = Cat
    list_display = [field.name for field in Cat._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
    filter_horizontal = ('character', 'favorite_things',)
    inlines = [CatImageInline, CatImageByAdminInline]
admin.site.register(Cat, CatOption)

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