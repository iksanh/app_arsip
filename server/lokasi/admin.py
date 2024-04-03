from django.contrib import admin
from .models import LokasiModel, TempatModel

# Register your models here.

class LokasiAdmin(admin.ModelAdmin):
    list_display = ['name']

class TempatAdmin(admin.ModelAdmin):
    list_display = ['nama']

admin.site.register(LokasiModel, LokasiAdmin)
admin.site.register(TempatModel, TempatAdmin)
