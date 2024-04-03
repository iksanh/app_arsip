# Generated by Django 4.2.7 on 2023-11-19 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit_kerja', '0003_subunitkerjamodel'),
        ('pegawai', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pegawaimodel',
            name='sub_unit_kerja',
        ),
        migrations.RemoveField(
            model_name='pegawaimodel',
            name='unit_kerja',
        ),
        migrations.DeleteModel(
            name='PegawaiUnitKerja',
        ),
        migrations.AddField(
            model_name='pegawaimodel',
            name='sub_unit_kerja',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='unit_kerja.subunitkerjamodel'),
        ),
        migrations.AddField(
            model_name='pegawaimodel',
            name='unit_kerja',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='unit_kerja.unitkerjamodel'),
        ),
    ]
