# Generated by Django 2.1.2 on 2020-02-14 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referencias', '0005_referenciamaquina_componente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referenciamaquina',
            name='linea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referencias.referenciaLinea'),
        ),
    ]
