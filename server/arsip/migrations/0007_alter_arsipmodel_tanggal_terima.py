# Generated by Django 4.2.7 on 2024-04-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsip', '0006_arsipmodel_tanggal_terima'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arsipmodel',
            name='tanggal_terima',
            field=models.DateField(blank=True, null=True),
        ),
    ]
