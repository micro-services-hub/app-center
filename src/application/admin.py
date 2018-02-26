from django.contrib import admin
from application import models


@admin.register(models.APP)
class APPAdmin(admin.ModelAdmin):
    pass
