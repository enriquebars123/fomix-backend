# Generated by Django 2.1.2 on 2020-10-30 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0064_auto_20201015_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 30, 11, 39, 58, 819821)),
        ),
    ]
