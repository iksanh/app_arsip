import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from unit_kerja.models import UnitKerjaModel, SubUnitKerjaModel
from pangkat_golongan.models import PangkatGolonganModel

# Create your models here.

class PegawaiStatusModel(models.Model):
    
    status = models.CharField(max_length=30)
    keterangan = models.CharField(max_length=150, default="", null=True)
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.status}'
    
    class Meta:
        db_table = "model_status_pegawai"


class PegawaiModel(models.Model):
    
    identitas=models.CharField(max_length=50)
    nama=models.CharField(max_length=150)
    status = models.ForeignKey(PegawaiStatusModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    # created_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    unit_kerja = models.ForeignKey(UnitKerjaModel, on_delete=models.CASCADE, default=None, null=True)
    sub_unit_kerja = models.ForeignKey(SubUnitKerjaModel, null=True, blank=True, on_delete=models.CASCADE)
    pangkat_golongan = models.ForeignKey(PangkatGolonganModel, null=True, blank=True, on_delete=models.CASCADE)
    jabatan = models.CharField(max_length=150, null=True, blank=True)
    user_profile = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.nama}'

    def save(self, *args, **kwargs):
        if not self.sub_unit_kerja:
            self.sub_unit_kerja = None

        super().save(*args, **kwargs)

    class Meta:
        db_table = "model_pegawai"


