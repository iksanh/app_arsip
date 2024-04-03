import uuid
from django.db import models


# Create your models here.

class MediaModel(models.Model):
    
    name = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'model_media'


