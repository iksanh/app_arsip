# Generated by Django 4.2.7 on 2024-04-06 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arsip', '0011_remove_arsipmodel_lokasi_remove_arsipmodel_tempat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arsipmodel',
            name='nomor_box',
        ),
    ]
