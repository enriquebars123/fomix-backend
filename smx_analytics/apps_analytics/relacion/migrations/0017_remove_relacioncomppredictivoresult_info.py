# Generated by Django 2.1.2 on 2020-03-18 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0016_relacioncomppredictivoresult_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relacioncomppredictivoresult',
            name='info',
        ),
    ]
