from django.conf import settings

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