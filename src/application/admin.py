from django.contrib import admin
from application import models


@admin.register(models.APP)
class APPAdmin(admin.ModelAdmin):
    list_display = ['name', 'client_id']
    list_display_links = ('client_id',)
