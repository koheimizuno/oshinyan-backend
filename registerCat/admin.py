from django.contrib import admin
from .models import Cat, CatImage, CatImageByAdmin, Character, FavoriteThing, Recommend

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
