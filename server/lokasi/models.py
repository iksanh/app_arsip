import uuid
from django.db import models


# Create your models here.

class LokasiModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'model_lokasi'


class TempatModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=200)
    lokasi = models.ForeignKey(LokasiModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nama}'
    
    class Meta:
        db_table = 'model_tempat'
