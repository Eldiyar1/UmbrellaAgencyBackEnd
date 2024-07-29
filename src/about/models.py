from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class Founder(BaseModel):
    fullname = models.CharField(
        _('ФИО'),
        max_length=120
    )
    position = models.CharField(
        _('Должность'),
        max_length=120
    )
    quote = models.CharField(
        _('Цитата'),
        max_length=120,
        blank=True,
        null=True
    )
    image = models.ImageField(
        _('Фотография'),
        upload_to='founders/',
        blank=True,
        null=True
    )
    url = models.URLField(
        _('Ссылка на вакансию')
    )

    def __str__(self):
        return (f'ФИО: {self.fullname}, '
                f'должность: {self.position}, '
                f'дата создания: {self.created_at}')

    class Meta:
        verbose_name = _('Основатель')
        verbose_name_plural = _('Основатели')


class Vacancy(BaseModel):
    title = models.CharField(
        _('Должность'),
        max_length=120
    )
    description = models.TextField(
        _('Описание вакансии')
    )

    def __str__(self) -> str:
        return f'Позиция: {self.title}, дата создания: {self.created_at}'

    class Meta:
        verbose_name = _('Вакансия')
        verbose_name_plural = _('Вакансии')

