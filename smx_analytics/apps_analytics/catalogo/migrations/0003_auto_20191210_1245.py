# Generated by Django 2.1.2 on 2019-12-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20191204_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogocomponente',
            name='imagen',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
