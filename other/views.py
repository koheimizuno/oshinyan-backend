from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Ambassador, Inquiry
from .serializers import AmbassadorSerializer, InquirySerializer

from utils.functions import send_email
from utils.email_templates import ambassador_email, ambassador_admin_email, inquiry_email, inquiry_admin_email

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