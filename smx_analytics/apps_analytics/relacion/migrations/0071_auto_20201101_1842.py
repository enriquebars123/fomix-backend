# Generated by Django 2.1.2 on 2020-11-02 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0070_auto_20201101_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 1, 18, 42, 7, 12191)),
        ),
    ]
