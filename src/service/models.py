from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class Section(BaseModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    description = models.TextField(
        _('Описание')
    )

    def __str__(self):
        return f'Заголовок: {self.title}, Описание секции: {self.description}'

    class Meta:
        verbose_name = _('Секция')
        verbose_name_plural = _('Секции')


class Process(BaseModel):
    description = models.TextField(
        _('Описание процесса')
    )

    def __str__(self):
        return f'Описание процесса: {self.description}'

    class Meta:
        verbose_name = _('Процесс')
        verbose_name_plural = _('Процессы')


class Portfolio(BaseModel):
    img = models.ImageField(
        _('Изображение'),
        upload_to='portfolio/'
    )
    title = models.CharField(
        _('Название'),
        max_length=120
    )

    def __str__(self):
        return f'Название: {self.title}'

    class Meta:
        verbose_name = _('Портфолио')
        verbose_name_plural = _('Портфолио')


class TeamMember(BaseModel):
    position = models.CharField(
        _('Позиция'),
        max_length=120
    )

    def __str__(self):
        return f'Позиция: {self.position}'

    class Meta:
        verbose_name = _('Член команды')
        verbose_name_plural = _('Члены команды')


class Tab(BaseModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    sections = models.ManyToManyField(
        Section,
        related_name='tab_sections',
        verbose_name=_('Секции')
    )
    processes = models.ManyToManyField(
        Process,
        related_name='tab_processes',
        verbose_name=_('Процессы')
    )
    portfolios = models.ManyToManyField(
        Portfolio,
        related_name='tab_portfolios',
        verbose_name=_('Портфолио')
    )
    team = models.ManyToManyField(
        TeamMember,
        related_name='tab_team',
        verbose_name=_('Команда')
    )

    def __str__(self):
        return f'Заголовок: {self.title}'

    class Meta:
        verbose_name = _('Таб')
        verbose_name_plural = _('Табы')


class Service(BaseModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    tabs = models.ManyToManyField(
        Tab,
        related_name='service_tabs',
        verbose_name=_('Табы')
    )

    def __str__(self):
        return f'Заголовок: {self.title}'

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')
