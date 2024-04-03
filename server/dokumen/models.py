from django.db import models

# Create your models here.

class DokumenModel(models.Model):
  nama = models.CharField(max_length=100)
  kode = models.CharField(max_length=50)

  def __str__(self) -> str:
    return f'({self.kode}) {self.nama}'

  class Meta:
    db_table = 'model_dokumen'