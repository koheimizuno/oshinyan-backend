from django.db import models

CLIENT_TYPE_CHOICES = (
    ('個人','個人'),
    ('法人', '法人'),
)

class Ambassador(models.Model):
    ambassador_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, blank=True)
    prefecture = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=200, blank=True)
    other_address = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    preferred = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'アンバサダー'

    def __str__(self):
        return self.ambassador_name

class Inquiry(models.Model):
    type = models.CharField(max_length=100)
    client_type = models.CharField(max_length=6, choices=CLIENT_TYPE_CHOICES, default='個人')
    company_name = models.CharField(max_length=100)
    kanji_name = models.CharField(max_length=100)
    furi_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    detail = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'お問い合わせ'