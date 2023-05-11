from django.contrib import admin
from . import models
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = (models.Video)

admin.site.register(models.Video)