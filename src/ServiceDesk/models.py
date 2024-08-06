from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel
from service.models import Service
import re
from django.core.exceptions import ValidationError

class ApplicationForm(BaseModel):
    """ Моделька данных с формы """
    name = models.CharField(
        _('Имя'),
        max_length=120
    )
    number_or_email = models.CharField(
        _('Имя или email'),
        max_length=30
    )
    service = models.ManyToManyField(
        Service,
        verbose_name=_('Какая услуга(-и) интересует клиента'),
        related_name='form_service'
    )
    review = models.TextField(
        _('Комментарий или запрос клиента'))


    def __str__(self) -> str:
        return f'Имя: {self.name}, контакты: {self.number_or_email}, дата: {self.created_at}'

    class Meta:
        verbose_name = _('Данные с формы')
        verbose_name_plural = verbose_name


class Contact(models.Model):
    number = models.CharField(
        _('Номер телефона'),
        max_length=14
    )
    email = models.EmailField(
        _('Почта')
    )
    address = models.CharField(
        _('Адрес'),
        max_length=250
    )
