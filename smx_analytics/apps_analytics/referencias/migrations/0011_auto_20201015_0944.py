# Generated by Django 2.1.2 on 2020-10-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referencias', '0010_auto_20200423_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referenciadmcciclo',
            name='fechaFin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]