# Generated by Django 2.1.2 on 2020-04-06 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0045_auto_20200402_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 10, 39, 43, 407652)),
        ),
    ]
