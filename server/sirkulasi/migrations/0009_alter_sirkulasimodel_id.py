# Generated by Django 4.2.7 on 2024-02-06 06:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sirkulasi', '0008_alter_sirkulasimodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirkulasimodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2f8f22d5-ff77-4e76-ae68-91d49f8a0d04'), editable=False, primary_key=True, serialize=False),
        ),
    ]
