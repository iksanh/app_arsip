from django.db import models

# Create your models here.

class PangkatGolonganModel(models.Model):

  pangkat = models.CharField(max_length=100)
  golongan = models.CharField(max_length=100)

  
  class Meta:
    db_table='model_pangkat_golongan'

  def __str__(self) -> str:
    return f'{self.pangkat} ({self.golongan})'