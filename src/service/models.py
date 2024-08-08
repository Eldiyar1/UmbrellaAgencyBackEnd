from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

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
    title = models.CharField(
        max_length=255,
        verbose_name=_('Название процесса')
    )
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


class Step(BaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Название шага')
    )
    description = models.TextField(
        verbose_name=_('Описание шага')
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Шаг')
        verbose_name_plural = _('Шаги')


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
        verbose_name=_('Портфолио'),
        blank=True,
        null=True
    )
    steps = models.ManyToManyField(
        Step,
        related_name='tab_steps',
        verbose_name=_('Шаги')
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


def validate_gif(value):
    if not value.name.endswith('.gif'):
        raise ValidationError(_('Разрешены только файлы GIF.'))


class Service(BaseModel):
    title = models.CharField(
        _('Заголовок'),
        max_length=120
    )
    short_description_for_banner = models.CharField(
        _('Краткое описание для баннера главной страницы'),
        help_text=_('Макс. символов: 90'),
        max_length=90,
    )
    gif = models.FileField(
        _('Гифка'),
        upload_to='gifs/',
        validators=[validate_gif],
        help_text=_('Загрузите гифку для услуги. Допустимые форматы: .gif'),
    )
    tabs = models.ManyToManyField(
        Tab,
        related_name='service_tabs',
        verbose_name=_('Табы'),
    )

    def __str__(self):
        return f'Заголовок: {self.title}'

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')
