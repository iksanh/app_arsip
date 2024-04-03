import csv
from django.contrib import admin
from .models import KlasifikasiModel

# Register your models here.

class KlasifikasiAdmin(admin.ModelAdmin):
    model = KlasifikasiModel
    list_display = ['kode_klasifikasi', 'kategory_arsip', 'jenis_arsip', 'keterangan', 'created_at']
    list_per_page = 10

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['keterangan'].required = False
        return form

    def import_csv(self, request, queryset):
        if 'file' in request.FILES:
            csv_file = request.FILES['file']
            decode_file = csv_file.read().decode('utf-8').splitlines()

            reader = csv.DictReader(decode_file)

            for row in reader:
                KlasifikasiModel.objects.create(
                    kode_klasifikasi=row['kode_klasifikasi'],
                    nama=row['nama']
                )

            self.message_user(request, "CSV Berhasil di import")
        else:
            self.message_user(request, "No File found")

    import_csv_shor_descritption = "Import Csv"

    actions = ['import_csv']



admin.site.register( KlasifikasiModel, KlasifikasiAdmin,)