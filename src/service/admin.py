from django.contrib import admin as django_admin
from .models import Section as SectionModel
from .models import Process as ProcessModel
from .models import Portfolio as PortfolioModel
from .models import TeamMember as TeamMemberModel
from .models import Tab as TabModel
from .models import Service as ServiceModel


class SectionAdmin(django_admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')


class ProcessAdmin(django_admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)


class PortfolioAdmin(django_admin.ModelAdmin):
    list_display = ('title', 'img')
    search_fields = ('title',)
    readonly_fields = ('img',)


class TeamMemberAdmin(django_admin.ModelAdmin):
    list_display = ('position',)
    search_fields = ('position',)


class TabAdmin(django_admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    filter_horizontal = ('sections', 'processes', 'portfolios', 'team')


class ServiceAdmin(django_admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    filter_horizontal = ('tabs',)


# Registering models in admin
django_admin.site.register(SectionModel, SectionAdmin)
django_admin.site.register(ProcessModel, ProcessAdmin)
django_admin.site.register(PortfolioModel, PortfolioAdmin)
django_admin.site.register(TeamMemberModel, TeamMemberAdmin)
django_admin.site.register(TabModel, TabAdmin)
django_admin.site.register(ServiceModel, ServiceAdmin)
