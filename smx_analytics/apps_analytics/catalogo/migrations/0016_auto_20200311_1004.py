# Generated by Django 2.1.2 on 2020-03-11 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0015_catalogofuentedatos_tipofuente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogomodelos',
            name='componente',
        ),
        migrations.DeleteModel(
            name='catalogoModelos',
        ),
    ]