# Generated by Django 4.2.7 on 2024-04-06 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi', '0026_alter_tempatmodel_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('tempat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lokasi.tempatmodel')),
            ],
            options={
                'db_table': 'model_box_ordner',
            },
        ),
    ]
