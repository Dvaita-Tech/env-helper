# Generated by Django 5.0.1 on 2025-02-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment',
            name='volume_path',
        ),
        migrations.AddField(
            model_name='environment',
            name='volume_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
