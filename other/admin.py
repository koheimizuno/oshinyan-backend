from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Ambassador, Inquiry, Report
from registerCat.models import Comment

class AmbassadorOption(admin.ModelAdmin):
    list_display = [field.name for field in Ambassador._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Ambassador, AmbassadorOption)

class InquiryOption(admin.ModelAdmin):
    list_display = [field.name for field in Inquiry._meta.get_fields() if not (field.many_to_many or field.one_to_many)]
admin.site.register(Inquiry, InquiryOption)

# Report Start
class ReportOption(admin.ModelAdmin):
    list_display = ('id', 'user', 'url', 'kanji_name', 'furi_name', 'phone', 'email', 'content', 'get_related_comments')
    def get_related_comments(self, obj):
        comments = Comment.objects.filter(report=obj).prefetch_related('comment_images', 'comment_reaction_icon')
        comment_data = ""
        for comment in comments:
            comment_data += f'<p>会員名 : {comment.user}</p>'
            comment_data += f'<p>猫の名前 : {comment.cat}</p>'
            comment_data += f'<p>コメント : {comment.comment}</p>'
            comment_data += '<div style="margin: 10px 0; display: flex; align-items: center; gap: 5px;">'
            for comment_image in comment.comment_images.all():
                comment_data += '<div><img src="{0}" style="max-height: 100px; max-width: 100px;" /></div>'.format(comment_image.imgs.url)
            comment_data += '</div>'
            comment_data += '<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 5px;">'
            for reaction_icon in comment.comment_reaction_icon.all():
                comment_data += '<img src="{0}" style="max-height: 30px; max-width: 30px;" />'.format(reaction_icon.imgs)
            comment_data += '</div>'
        return mark_safe(comment_data)
    get_related_comments.short_description = 'コメントデータ'
admin.site.register(Report, ReportOption)
# Report End