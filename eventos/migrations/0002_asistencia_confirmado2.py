# Generated by Django 5.0.2 on 2024-02-24 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='confirmado2',
            field=models.BooleanField(default=False),
        ),
    ]
