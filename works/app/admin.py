from django.contrib import admin

from . import models

@admin.register(models.Client)

class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        ]

@admin.register(models.Work)

class WorkAdmin(admin.ModelAdmin):
    list_display = [
        'link','work_type',
        ]

@admin.register(models.Artist)

class ArtistAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        ]




# Register your models here.
