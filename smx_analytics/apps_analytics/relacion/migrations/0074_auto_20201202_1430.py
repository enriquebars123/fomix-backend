# Generated by Django 2.1.2 on 2020-12-02 20:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0073_auto_20201109_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 14, 30, 19, 608294)),
        ),
    ]
