# Generated by Django 2.1.2 on 2020-03-18 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0014_auto_20200220_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]
