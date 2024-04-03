import uuid

from django.db import models
from django.contrib.auth.models import User
from unit_kerja.models import UnitKerjaModel
from klasifikasi.models import KlasifikasiModel
from media.models import MediaModel
from lokasi.models import LokasiModel, TempatModel
from dokumen.models import DokumenModel


# Create your models here.


class ArsipModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    no_arsip = models.CharField(max_length=200)
    jenis_dokumen = models.ForeignKey(DokumenModel, on_delete=models.CASCADE, default=None, null=True)
    pencipta = models.ForeignKey(UnitKerjaModel, on_delete=models.CASCADE, related_name='arsip_pencipta')
    kode_klasifikasi = models.ForeignKey(KlasifikasiModel, on_delete=models.CASCADE)
    pengelola = models.ForeignKey(UnitKerjaModel, on_delete=models.CASCADE, related_name='arsip_pengelola')
    tanggal_dokumen = models.DateField()
    uraian = models.TextField()
    keterangan = models.CharField(max_length=100)
    media = models.ForeignKey(MediaModel, on_delete=models.CASCADE)
    lokasi = models.ForeignKey(LokasiModel, on_delete=models.CASCADE)
    tempat = models.ForeignKey(TempatModel, on_delete=models.CASCADE)
    nomor_box = models.CharField(max_length=100)
    tujuan_surat = models.CharField(max_length=255, null=True)
    asal_surat = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to='uploads/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arsip_created')
    created_at = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arsip_updated')
    update_at = models.DateTimeField()


    def __str__(self):
        return  f'{self.no_arsip}'





