# Generated by Django 2.1.2 on 2020-04-16 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referencias', '0007_referenciamaqdmcciclo_referenciamaqvarindep'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='referenciaMaqDmcCiclo',
            new_name='referenciaDmcCiclo',
        ),
        migrations.RenameModel(
            old_name='referenciaMaqVarIndep',
            new_name='referenciaVarIndep',
        ),
        migrations.AlterModelTable(
            name='referenciadmcciclo',
            table='referenciaDmcCiclo',
        ),
        migrations.AlterModelTable(
            name='referenciavarindep',
            table='referenciaVarIndep',
        ),
    ]
