from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Ambassador, Inquiry, Report
from .serializers import AmbassadorSerializer, InquirySerializer, ReportSerializer

from utils.functions import send_email
from utils.email_templates import ambassador_email, ambassador_admin_email, inquiry_email, inquiry_admin_email, report_email

class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
    def perform_create(self, serializer):
        ambassador = serializer.save()
        send_email(ambassador.email, "「推しニャン」アンバサダー登録御礼", ambassador_email.format(ambassador.ambassador_name))
        send_email(settings.BACKEND_EMAIL, 'アンバサダー登録', ambassador_admin_email.format(ambassador.created_date, ambassador.ambassador_name, \
                           ambassador.full_name, ambassador.prefecture, ambassador.email, ambassador.phone, ambassador.preferred ))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    def perform_create(self, serializer):
        inquiry = serializer.save()
        send_email(inquiry.email, '「推しニャン」サイト　お問い合わせ受理', inquiry_email.format(inquiry.kanji_name, inquiry.type, \
                        inquiry.client_type, inquiry.company_name, inquiry.kanji_name, inquiry.furi_name, inquiry.phone, \
                        inquiry.email, inquiry.detail))
        send_email(settings.BACKEND_EMAIL, '【問い合わせ対応依頼】', inquiry_admin_email.format(inquiry.created_date, inquiry.type, \
                            inquiry.client_type, inquiry.company_name, inquiry.kanji_name, inquiry.furi_name, inquiry.phone, \
                            inquiry.email, inquiry.detail ))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# Report Start
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    def create(self, request, *args, **kwargs):
        report_data = self.get_serializer(data=request.data)
        user = self.request.user
        if report_data.is_valid():
            report_data.save()
            send_email(settings.BACKEND_EMAIL, '通報ボタン報告', report_email.format(report_data.data['created_date'], \
                    user.username, report_data.data['url'], report_data.data['kanji_name'], report_data.data['furi_name'], \
                    report_data.data['phone'], report_data.data['email'], report_data.data['content'] ))
            return Response(report_data.data, status=status.HTTP_200_OK)
        else:
            return Response({'errors': report_data.errors}, status=status.HTTP_400_BAD_REQUEST)
# Report End