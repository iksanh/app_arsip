from django.contrib import admin
from .models import ArsipModel

# Register your models here.


class ArsipAdmin(admin.ModelAdmin):
    list_display = ['uraian']



admin.site.register(ArsipModel, ArsipAdmin)