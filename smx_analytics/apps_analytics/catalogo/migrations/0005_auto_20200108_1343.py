# Generated by Django 2.1.2 on 2020-01-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20191211_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogomenu',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]
