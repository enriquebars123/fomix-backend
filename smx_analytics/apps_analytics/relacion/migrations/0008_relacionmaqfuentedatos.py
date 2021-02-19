# Generated by Django 2.1.2 on 2020-01-30 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referencias', '0003_auto_20191210_1245'),
        ('catalogo', '0009_auto_20200130_1412'),
        ('relacion', '0007_auto_20200130_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='relacionMaqFuenteDatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referenciaId', models.CharField(blank=True, max_length=50, null=True)),
                ('fuenteDato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogo.catalogoFuenteDatos')),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='referencias.referenciaMaquina')),
            ],
            options={
                'db_table': 'relacionMaqFuenteDatos',
            },
        ),
    ]