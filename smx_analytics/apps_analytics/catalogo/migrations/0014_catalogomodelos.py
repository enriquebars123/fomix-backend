# Generated by Django 2.1.2 on 2020-03-05 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0013_auto_20200211_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='catalogoModelos',
            fields=[
                ('componenteExterno', models.CharField(max_length=250, unique=True)),
                ('componente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='catalogo.catalogoComponente')),
            ],
            options={
                'db_table': 'catalogoModelo',
            },
        ),
    ]
