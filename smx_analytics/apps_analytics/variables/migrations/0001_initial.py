# Generated by Django 2.1.2 on 2019-11-25 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('componente', models.CharField(blank=True, max_length=250, null=True)),
                ('fuenteDato', models.CharField(blank=True, max_length=250, null=True)),
                ('variable', models.CharField(blank=True, max_length=250, null=True)),
                ('variableRef', models.CharField(blank=True, max_length=250, null=True)),
                ('tipoDato', models.CharField(blank=True, max_length=250, null=True)),
                ('tipoVarible', models.CharField(blank=True, max_length=250, null=True)),
                ('isActive', models.BooleanField(default=False)),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='referencias.referenciaMaquina')),
            ],
            options={
                'db_table': 'variables',
            },
        ),
    ]
