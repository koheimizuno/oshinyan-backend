from django.db import models

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
        verbose_name_plural = '未登録看板猫'

    def __str__(self):
        return self.ambassador_name