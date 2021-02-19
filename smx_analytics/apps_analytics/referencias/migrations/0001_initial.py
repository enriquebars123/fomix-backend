# Generated by Django 2.1.2 on 2019-11-25 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='referenciaEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'referenciaEmpresa',
            },
        ),
        migrations.CreateModel(
            name='referenciaLinea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'referenciaLinea',
            },
        ),
        migrations.CreateModel(
            name='referenciaMaquina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
                ('imagen', models.FileField(upload_to='uploads/')),
                ('linea', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='referencias.referenciaLinea')),
            ],
            options={
                'db_table': 'referenciaMaquina',
            },
        ),
        migrations.CreateModel(
            name='referenciaPlanta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='referencias.referenciaEmpresa')),
            ],
            options={
                'db_table': 'referenciaPlanta',
            },
        ),
        migrations.AddField(
            model_name='referencialinea',
            name='planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='referencias.referenciaPlanta'),
        ),
    ]