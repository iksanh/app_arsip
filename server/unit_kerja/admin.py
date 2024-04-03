from django.contrib import admin
from .models import UnitKerjaModel, SubUnitKerjaModel


# Register your models here.

class UnitKerjaAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'created_by')
    search_fields = ['name', ]
    # list_filter = ['name', 'created_at', 'created_by']


class SubUnitKerjaAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_kerja']


admin.site.register(UnitKerjaModel, UnitKerjaAdmin)
admin.site.register(SubUnitKerjaModel, SubUnitKerjaAdmin)
