# Generated by Django 2.1.2 on 2020-03-24 23:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0028_auto_20200324_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 17, 38, 21, 44189)),
        ),
    ]
