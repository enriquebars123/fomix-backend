# Generated by Django 2.1.2 on 2020-04-16 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0049_auto_20200416_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 10, 34, 22, 454578)),
        ),
    ]