# Generated by Django 5.1.2 on 2024-11-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='rut_visitante',
            field=models.CharField(default='12345678-9', max_length=9),
        ),
    ]
