# Generated by Django 4.2.7 on 2024-01-11 22:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sirkulasi', '0006_alter_sirkulasimodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirkulasimodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7c3b1fb8-7a6b-4124-b48d-12b92bf01ecd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
