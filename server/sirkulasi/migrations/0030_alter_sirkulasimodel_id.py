# Generated by Django 4.2.7 on 2024-04-04 10:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sirkulasi', '0029_alter_sirkulasimodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sirkulasimodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('47c52415-7f0e-4ef6-bedd-f58469eb40fa'), editable=False, primary_key=True, serialize=False),
        ),
    ]
