# Generated by Django 2.1.2 on 2020-02-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_auto_20200204_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogofuentedatos',
            name='urlMaquinas',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]