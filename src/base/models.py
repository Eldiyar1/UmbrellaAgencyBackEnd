from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        _('Создано в: '),
        auto_now_add=True
    )

    class Meta:
        abstract = True

