# Generated by Django 2.1.2 on 2020-09-22 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0061_auto_20200906_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 22, 15, 27, 6, 347938)),
        ),
    ]
