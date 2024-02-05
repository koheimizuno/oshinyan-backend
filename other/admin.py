from django.contrib import admin
from .models import Ambassador, Inquiry, Banner, Advertise

class AmbassadorOption(admin.ModelAdmin):
    list_display = [field.name for field in Ambassador._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Ambassador, AmbassadorOption)

class InquiryOption(admin.ModelAdmin):
    list_display = [field.name for field in Inquiry._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Inquiry, InquiryOption)

class BannerOption(admin.ModelAdmin):
    list_display = [field.name for field in Banner._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Banner, BannerOption)

class AdvertiseOption(admin.ModelAdmin):
    list_display = [field.name for field in Advertise._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Advertise, AdvertiseOption)