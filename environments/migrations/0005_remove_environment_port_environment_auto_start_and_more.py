# Generated by Django 5.0.1 on 2025-02-08 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0004_alter_environment_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment',
            name='port',
        ),
        migrations.AddField(
            model_name='environment',
            name='auto_start',
            field=models.BooleanField(default=False, help_text='Start container automatically on system boot'),
        ),
        migrations.AddField(
            model_name='environment',
            name='cpu_limit',
            field=models.CharField(blank=True, help_text='CPU limit (e.g., 0.5, 1.0, 2.0)', max_length=10),
        ),
        migrations.AddField(
            model_name='environment',
            name='env_vars',
            field=models.TextField(blank=True, help_text='Environment variables in KEY=value format, one per line'),
        ),
        migrations.AddField(
            model_name='environment',
            name='memory_limit',
            field=models.CharField(blank=True, help_text='Memory limit (e.g., 512m, 1g, 2g)', max_length=10),
        ),
        migrations.AddField(
            model_name='environment',
            name='ports',
            field=models.CharField(blank=True, help_text='Comma-separated list of port mappings (e.g., "8080:80,3000:3000")', max_length=255),
        ),
        migrations.AddField(
            model_name='environment',
            name='volumes',
            field=models.TextField(blank=True, help_text='One volume mount per line in host_path:container_path format'),
        ),
    ]
