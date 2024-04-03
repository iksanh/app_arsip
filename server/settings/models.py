from django.db import models

# Create your models here.

class SettingsModel(models.Model):
  nama_satker = models.CharField(max_length=200)
  alamat = models.TextField()
  
