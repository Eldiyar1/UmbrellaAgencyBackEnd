from django.db import models

from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

from base.models import BaseModel


class Portfolio(BaseModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    price = models.CharField(
        _('Сделанная прибыль'),
        max_length=120
    )
    image = models.ImageField(
        upload_to='images/portfolio/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'png', 'jpeg']
            )
        ]
    )
    link = models.URLField(
        _('Ссылка'),
        max_length=200,
        help_text=_('Ссылка на проект или ресурс.')
    )

    def __str__(self):
        return f'Заголовок: {self.title}, прибыль: {self.price}, создано в: {self.created_at}'

    class Meta:
        verbose_name = _('Портфолио')
        verbose_name_plural = verbose_name
