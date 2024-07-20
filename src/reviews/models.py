from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from base.models import BaseModel


class Review(BaseModel):
    avatar = models.ImageField(
        _('Аватар клиента'),
        upload_to='avatar/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpeg', 'jpg', 'png', 'svg'],
                message=_('this avatar extension is not allowed...')
            )
        ]
    )
    fullname = models.CharField(
        _('Полное имя'),
        max_length=120
    )
    position = models.CharField(
        _('Должность'),
        max_length=120
    )
    company_name = models.CharField(
        _('Наименование компании'),
        max_length=120
    )
    star = models.PositiveIntegerField(
        _('Звезд')
    )
    description = models.TextField(
        _('Комментарий')
    )

    def clean(self):
        if self.star > 5:
            raise ValidationError({'star': _('Звезды не могут быть больше 5')})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Имя: {self.fullname}, Оценка: {self.star}, дата создания: {self.created_at}'

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
