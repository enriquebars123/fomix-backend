# Generated by Django 2.1.2 on 2020-02-11 20:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0012_remove_catalogocomponente_maquina'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogofuentedatos',
            old_name='valor',
            new_name='filtro',
        ),
        migrations.RenameField(
            model_name='catalogofuentedatos',
            old_name='url',
            new_name='urlCatalogo',
        ),
        migrations.RenameField(
            model_name='catalogofuentedatos',
            old_name='urlMaquinas',
            new_name='urlRegistro',
        ),
        migrations.RemoveField(
            model_name='catalogofuentedatos',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='catalogofuentedatos',
            name='limite',
        ),
        migrations.RemoveField(
            model_name='catalogofuentedatos',
            name='nombreVar',
        ),
        migrations.RemoveField(
            model_name='catalogofuentedatos',
            name='ralacionMaquina',
        ),
        migrations.AddField(
            model_name='catalogofuentedatos',
            name='estructura',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='catalogofuentedatos',
            name='paginacion',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='catalogofuentedatos',
            name='urlValComRel',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
