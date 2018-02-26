from django.db import models
from django.conf import settings
from application import managers


class APP(models.Model):
    name = models.CharField(verbose_name="name", max_length=255, blank=True, null=True)
    client_id = models.CharField(verbose_name="client_id", unique=True, max_length=127)
    client_secret = models.CharField(verbose_name="client_secret", max_length=255)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    objects = managers.APPManager()

    def __str__(self):
        return "{}".format(self.client_id)


