from django.contrib import admin
from .models import Founder, Vacancy


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'created_at')
    search_fields = ('fullname', 'position')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('fullname', 'position', 'quote', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'url')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)


1735