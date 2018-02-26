from hmac import compare_digest
from django.db import models


class APPManager(models.Manager):
    def is_authorized_app(self, client_id, client_secret):
        try:
            app = self.get(client_id=client_id)
        except self.model.DoesNotExist:
            return False
        return compare_digest(app.client_secret, client_secret)
