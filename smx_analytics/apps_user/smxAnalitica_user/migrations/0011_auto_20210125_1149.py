# Generated by Django 2.1.2 on 2021-01-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smxAnalitica_user', '0010_auto_20201207_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/user'),
        ),
    ]
