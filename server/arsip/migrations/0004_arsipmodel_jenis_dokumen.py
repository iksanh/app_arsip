# Generated by Django 4.2.7 on 2024-01-11 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dokumen', '0001_initial'),
        ('arsip', '0003_alter_arsipmodel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='arsipmodel',
            name='jenis_dokumen',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dokumen.dokumenmodel'),
        ),
    ]
