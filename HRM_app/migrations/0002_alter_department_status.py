# Generated by Django 5.1.1 on 2025-01-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRM_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
