# Generated by Django 2.1.2 on 2020-03-27 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0039_auto_20200327_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 0, 21, 41, 516720)),
        ),
    ]
