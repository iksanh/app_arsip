from datetime import  date
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from klasifikasi.models import KlasifikasiModel

# Create your models here.

class UnitKerjaModel(models.Model):
    name = models.CharField(max_length=150)
    arsip = models.CharField(max_length=20, null=True)
    created_at = models.DateField(default=date.today)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "model_unit_kerja"


class SubUnitKerjaModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(default=date.today)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    unit_kerja = models.ForeignKey(UnitKerjaModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'model_sub_unit_kerja'



# admin.site.register(UnitKerjaModel,)