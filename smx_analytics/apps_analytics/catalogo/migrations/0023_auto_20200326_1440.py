# Generated by Django 2.1.2 on 2020-03-26 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0022_auto_20200326_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogovariable',
            name='componente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.catalogoComponente'),
        ),
    ]
