import uuid

from django.db import models
from arsip.models import ArsipModel
from pegawai.models import PegawaiModel
from django.contrib.auth.models import User


# Create your models here.


class SirkulasiModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nomor_arsip = models.ForeignKey(ArsipModel, on_delete=models.CASCADE, null=True)
    peminjam = models.ForeignKey(PegawaiModel, on_delete=models.CASCADE, null=True)
    keperluan = models.TextField()
    tanggal_pinjam = models.DateField(null=True)
    tanggal_harus_kembali = models.DateField(null=True)
    tanggal_kembali = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sirkulasi_created', null=True)
    updated_at = models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sirkulasi_updated', null=True)


    class Meta:
        db_table = 'model_sirkulasi'