# Generated by Django 2.1.2 on 2020-03-24 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0016_auto_20200311_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='catalogoSimbologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('icon', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'db_table': 'catalogoSimbologia',
            },
        ),
        migrations.CreateModel(
            name='catalogoVarDependiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, unique=True)),
                ('nominal', models.FloatField()),
                ('usl', models.FloatField()),
                ('lsl', models.FloatField()),
                ('ucl', models.FloatField()),
                ('lcl', models.FloatField()),
                ('componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.catalogoComponente')),
                ('simbologia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.catalogoSimbologia')),
            ],
            options={
                'db_table': 'catalogoVarDependiente',
            },
        ),
    ]