# Generated by Django 4.2.7 on 2024-03-05 07:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sirkulasi', '0018_alter_sirkulasimodel_id_alter_sirkulasimodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirkulasimodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ac23c99b-55b2-447f-9eb9-6e386c7123cc'), editable=False, primary_key=True, serialize=False),
        ),
    ]
