from django.contrib import admin
from .models import SirkulasiModel

# Register your models here.

@admin.register(SirkulasiModel)
class SirkulasiAdmin(admin.ModelAdmin):
    pass