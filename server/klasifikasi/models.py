import uuid
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db import connection
from django.contrib import admin
from unit_kerja.models import  SubUnitKerjaModel, UnitKerjaModel

# Model for Klasifikasi Arsip.


# enum tipe klasifikasi
KLASIFIKASI_OPTION = [('FASILITATIF', 'Arsip Fasilitatif'), ('SUBSTANTIF', 'Arsip Subtantif')]
NASIB_AKHIR_OPTION = [('Musnah', 'Musnah'),('Permanen', 'Permanen'),('Masuk berkas perseorangan', 'Masuk berkas perseorangan')]



class KlasifikasiModel(models.Model):
    
    kategory_arsip = models.CharField(max_length=20, choices=KLASIFIKASI_OPTION, default='SUBSTANTIF')
    kode_klasifikasi = models.CharField(max_length=50)
    jenis_arsip = models.CharField(max_length=100, default="")
    keterangan = models.TextField(null=True)
    unit_kerja = models.ForeignKey(UnitKerjaModel, on_delete=models.SET_NULL, null=True)
    sub_unit_kerja = models.ForeignKey(SubUnitKerjaModel, on_delete=models.SET_NULL, null=True)
    waktu_aktif = models.IntegerField(null=True)
    waktu_inaktif = models.IntegerField(null=True)
    nasib_akhir = models.CharField(max_length=100, choices=NASIB_AKHIR_OPTION, default='Musnah')
    
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        if not self.keterangan:
            self.keterangan = ""

        super().save(*args, **kwargs)


    def __str__(self):
        return f'({self.kode_klasifikasi}) {self.jenis_arsip}'

    class Meta:
        db_table = "model_klasifikasi"



