# Generated by Django 4.2.7 on 2024-04-06 07:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sirkulasi', '0036_alter_sirkulasimodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirkulasimodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8d03242b-80d3-4106-a7d8-bb1141d23811'), editable=False, primary_key=True, serialize=False),
        ),
    ]
