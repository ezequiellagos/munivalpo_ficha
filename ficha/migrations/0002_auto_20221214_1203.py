# Generated by Django 3.2.15 on 2022-12-14 15:03

from django.db import migrations, models
import ficha.models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografiacontexto',
            name='registro_fotografico_1',
            field=models.ImageField(blank=True, default='', upload_to=ficha.models.content_file_name_contexto_1),
        ),
        migrations.AlterField(
            model_name='fotografiacontexto',
            name='registro_fotografico_2',
            field=models.ImageField(blank=True, default='', upload_to=ficha.models.content_file_name_contexto_2),
        ),
        migrations.AlterField(
            model_name='fotografiageneral',
            name='imagen_fotografia',
            field=models.ImageField(blank=True, default='', upload_to=ficha.models.content_file_name_general),
        ),
        migrations.AlterField(
            model_name='planoubicacion',
            name='imagen_plano',
            field=models.ImageField(blank=True, default='', upload_to=ficha.models.content_file_name_plano),
        ),
    ]
