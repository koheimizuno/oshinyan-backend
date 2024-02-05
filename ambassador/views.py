from django.conf import settings

from .email_templates import ambassador_email

# For Define API Views
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .models import  Ambassador
from .serializers import AmbassadorSerializer

# For ElasticEmail
import ElasticEmail
from ElasticEmail.api import emails_api
from ElasticEmail.model.email_content import EmailContent
from ElasticEmail.model.body_part import BodyPart
from ElasticEmail.model.body_content_type import BodyContentType
from ElasticEmail.model.email_recipient import EmailRecipient
from ElasticEmail.model.email_message_data import EmailMessageData


configuration = ElasticEmail.Configuration()
configuration.api_key['apikey'] = settings.MAIL_API_KEY

def send_email(reciever_email, subject, content):
    with ElasticEmail.ApiClient(configuration) as api_client:
            api_instance = emails_api.EmailsApi(api_client)
            email_message_data = EmailMessageData(
                recipients=[
                    EmailRecipient(
                        email=reciever_email,
                    ),
                ],
                content=EmailContent(
                    body=[
                        BodyPart(
                            content_type=BodyContentType("HTML"),
                            content=content,
                            charset="utf-8",
                        ),
                    ],
                    _from=settings.BACKEND_EMAIL,
                    reply_to=settings.BACKEND_EMAIL,
                    subject=subject,
                ),
            )
            api_instance.emails_post(email_message_data)

class AmbassadorViewSet(viewsets.ModelViewSet):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
    def create(self, request):
        serializer = AmbassadorSerializer(data=request.data)
        if serializer.is_valid():
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

