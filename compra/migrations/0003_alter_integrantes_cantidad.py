# Generated by Django 4.2.2 on 2023-10-30 21:54

import compra.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_alter_proyecto_aprendiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantes',
            name='cantidad',
            field=models.IntegerField(validators=[compra.models.validate_positive], verbose_name='cantidad'),
        ),
    ]