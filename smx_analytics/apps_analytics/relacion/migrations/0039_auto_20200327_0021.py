# Generated by Django 2.1.2 on 2020-03-27 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0038_auto_20200326_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 0, 20, 33, 25183)),
        ),
    ]