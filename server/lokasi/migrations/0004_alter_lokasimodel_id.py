# Generated by Django 4.2.7 on 2023-11-18 22:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi', '0003_alter_lokasimodel_id_alter_lokasimodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokasimodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('02cc8307-2d98-4f95-a2da-a73720a230d7'), editable=False, primary_key=True, serialize=False),
        ),
    ]
