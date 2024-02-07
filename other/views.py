from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Ambassador, Inquiry, Banner
from .serializers import AmbassadorSerializer, InquirySerializer, BannerSerializer

from utils.send_email import send_email
from utils.email_templates import ambassador_email

class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
    def perform_create(self, serializer):
        ambassador = serializer.save()
        send_email(ambassador.email, "「推しニャン」アンバサダー登録御礼", "<p>" + ambassador.ambassador_name + "様</p>" + ambassador_email)
        send_email(settings.BACKEND_EMAIL, 'アンバサダー登録', 
                   f"""
                        <p>事務局担当者</p>
                        <p>
                            「推しニャン」サイトにアンバサダー登録がありました。
                            下記ご確認ください。
                        </p>
                        <p>日時：{ambassador.last_update}</p>
                        <p>アンバサダー名：{ambassador.ambassador_name}</p>
                        <p>氏名{ambassador.full_name}</p>
                        <p>都道府県：{ambassador.prefecture}</p>
                        <p>メールアドレス：{ambassador.email}</p>
                        <p>電話：{ambassador.phone}</p>
                        <p>希望：{ambassador.preferred}</p>
                    """
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    def perform_create(self, serializer):
        inquiry = serializer.save()
        send_email(inquiry.email, '「推しニャン」サイト　お問い合わせ受理', 
                   f"""
                        <p>{inquiry.kanji_name}様</p>
                        <p>
                            「推しニャン」サイト事務局です。<br/>
                            このたびは、「推しニャン」サイトへのお問い合わせありがとうございます。
                        </p>
                        <p>
                            <span>問い合わせ種別：{inquiry.type}</span><br />
                            <span>個人／法人：{inquiry.client_type}</span><br />
                            <span>会社名：{inquiry.company_name}</span><br />
                            <span>氏名：{inquiry.kanji_name}</span><br />
                            <span>ふりなが：{inquiry.furi_name}</span><br />
                            <span>電話番号：{inquiry.phone}</span><br />
                            <span>メールアドレス：{inquiry.email}</span><br />
                            <span>お問い合わせ内容：{inquiry.detail}</span>
                        </p>
                        <p>いただいた内容は、事務局にて返信内容等を精査させていただき、ご連絡が必要と思われたもののみ別途ご連絡をさせていただきます。</p>
                        <p>
                            「推しニャン」サイト事務局より <br />
                            お問い合わせ先：<a href="mailto:nyan@oshinyan.love">nyan@oshinyan.love</a>
                        </p>
                    """
        )
        send_email(settings.BACKEND_EMAIL, '【問い合わせ対応依頼】', 
                   f"""
                        <p>事務局担当者</p>
                        <p>
                            「推しニャン」サイトに問い合わせが入りました。対応をお願いします。
                        </p>
                        <p>日時：{inquiry.last_update}</p>
                        <p>
                            <span>【受理した内容】</span><br />
                            <span>問い合わせ種別：{inquiry.type}</span><br />
                            <span>個人／法人：{inquiry.client_type}</span><br />
                            <span>会社名：{inquiry.company_name}</span><br />
                            <span>氏名：{inquiry.kanji_name}</span><br />
                            <span>ふりなが：{inquiry.furi_name}</span><br />
                            <span>電話番号：{inquiry.phone}</span><br />
                            <span>メールアドレス：{inquiry.email}</span><br />
                            <span>お問い合わせ内容：{inquiry.detail}</span>
                        </p>
                        <p>以上です。</p>
                    """
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

# class AdvertiseViewSet(viewsets.ModelViewSet):
#     queryset = Advertise.objects.all()
#     serializer_class = AdvertiseSerializer