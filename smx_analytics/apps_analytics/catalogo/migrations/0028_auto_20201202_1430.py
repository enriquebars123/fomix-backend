# Generated by Django 2.1.2 on 2020-12-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0027_catalogopredictivo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogocomponente',
            name='imagen',
            field=models.ImageField(upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='catalogosimbologia',
            name='icon',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
