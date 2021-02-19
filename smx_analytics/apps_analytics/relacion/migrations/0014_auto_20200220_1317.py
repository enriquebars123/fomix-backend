# Generated by Django 2.1.2 on 2020-02-20 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0013_auto_20200211_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacionmaqfuentedatos',
            name='fuenteDatos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogo.catalogoFuenteDatos'),
        ),
        migrations.AlterField(
            model_name='relacionmaqfuentedatos',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='referencias.referenciaMaquina'),
        ),
    ]
