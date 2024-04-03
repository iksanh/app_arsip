from django.contrib import admin
from django import forms
from .models import PegawaiModel, PegawaiStatusModel


# Register your models here.

# class PegawaiUnitKerjaInline(admin.TabularInline):
#     model = PegawaiUnitKerja
#     extra = 1

class PegawaiAdminForm(forms.ModelForm):
    class Meta:
        model = PegawaiModel
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        sub_unit_kerja = cleaned_data.get('sub_unit_kerja')

        if sub_unit_kerja is not None and sub_unit_kerja == "":
            cleaned_data['sub_unit_kerja'] = None

        return cleaned_data


class PegawaiAdmin(admin.ModelAdmin):
    list_display = ['identitas', 'nama', 'unit_kerja', 'sub_unit_kerja']
    form = PegawaiAdminForm


class PegawaiStatusAdmin(admin.ModelAdmin):
    list_display = ['status', 'keterangan']
    search_fields = ['status', 'keterangan']


admin.site.register(PegawaiModel, PegawaiAdmin)
admin.site.register(PegawaiStatusModel, PegawaiStatusAdmin)
