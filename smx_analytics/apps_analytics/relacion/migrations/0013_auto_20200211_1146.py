# Generated by Django 2.1.2 on 2020-02-11 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0012_relacioncomppredictivo_maquina'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relacioncomppredictivoresult',
            old_name='componente',
            new_name='codigoPieza',
        ),
    ]
