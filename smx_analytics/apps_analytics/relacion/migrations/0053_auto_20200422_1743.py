# Generated by Django 2.1.2 on 2020-04-22 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0052_auto_20200422_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 17, 43, 41, 944347)),
        ),
    ]
