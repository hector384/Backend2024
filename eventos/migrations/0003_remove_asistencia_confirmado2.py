# Generated by Django 5.0.2 on 2024-02-24 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_asistencia_confirmado2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='confirmado2',
        ),
    ]
