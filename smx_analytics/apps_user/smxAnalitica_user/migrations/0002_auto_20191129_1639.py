# Generated by Django 2.1.2 on 2019-11-29 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smxAnalitica_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
