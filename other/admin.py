from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Ambassador, Inquiry

class AmbassadorOption(admin.ModelAdmin):
    list_display = [field.name for field in Ambassador._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Ambassador, AmbassadorOption)

class InquiryOption(admin.ModelAdmin):
    list_display = [field.name for field in Inquiry._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Inquiry, InquiryOption)