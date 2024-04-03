from django.contrib import admin
from .models import MediaModel

# Register your models here.


class MediaAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(MediaModel, MediaAdmin,)