# Generated by Django 4.2.7 on 2023-11-19 02:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi', '0014_alter_lokasimodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokasimodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8a1318eb-7564-4257-a273-9e7925b76d8b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
