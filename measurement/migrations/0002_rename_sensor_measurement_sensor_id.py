# Generated by Django 5.1.1 on 2024-09-28 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor',
            new_name='sensor_id',
        ),
    ]
