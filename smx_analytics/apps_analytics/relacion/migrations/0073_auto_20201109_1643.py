# Generated by Django 2.1.2 on 2020-11-09 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0072_auto_20201103_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 9, 16, 43, 15, 413538)),
        ),
    ]
