# Generated by Django 2.1.2 on 2020-01-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smxAnalitica_user', '0005_merge_20200117_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]
