from django.contrib import admin

from reviews import models as review_mod


@admin.register(review_mod.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'company_name', 'star', 'created_at')
