# Generated by Django 4.2.7 on 2023-11-19 07:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0018_alter_mediamodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d3764e8e-ef4d-4875-9849-e20018cdbcb1'), editable=False, primary_key=True, serialize=False),
        ),
    ]
