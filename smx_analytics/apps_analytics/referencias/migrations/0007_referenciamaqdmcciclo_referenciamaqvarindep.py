# Generated by Django 2.1.2 on 2020-04-16 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referencias', '0006_auto_20200214_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='referenciaMaqDmcCiclo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dmc', models.CharField(max_length=50)),
                ('fechaIni', models.DateField()),
                ('fechaFin', models.DateField()),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referencias.referenciaMaquina')),
            ],
            options={
                'db_table': 'referenciaMaqDmcCiclo',
            },
        ),
        migrations.CreateModel(
            name='referenciaMaqVarIndep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referencias.referenciaMaquina')),
            ],
            options={
                'db_table': 'referenciaMaqVarIndep',
            },
        ),
    ]
