from django.contrib import admin

from ServiceDesk.models import ApplicationForm


@admin.register(ApplicationForm)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_or_email', 'created_at']
