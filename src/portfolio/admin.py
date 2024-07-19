from django.contrib import admin

from portfolio import models as port_mod


@admin.register(port_mod.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
