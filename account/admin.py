from django.contrib import admin
from .models import Member, Avatar

admin.site.site_header = "Oshinyan.love Administration"
admin.site.site_title = "Oshinyan.love"

# Register User Model
class UserOption(admin.ModelAdmin):
    def get_list_display(self, request):
        exclude_column = "password"  # Replace with the actual name of the column you want to exclude
        all_columns = [field.name for field in self.model._meta.fields]
        display_columns = [column for column in all_columns if column != exclude_column]
        return display_columns
admin.site.register(Member, UserOption)

# Register Avatar Model
class AvatarOption(admin.ModelAdmin):
    list_display = [field.name for field in Avatar._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Avatar, AvatarOption)