# Generated by Django 2.1.2 on 2020-04-23 21:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0053_auto_20200422_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='relacionMaqFuenteDatosVarInd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('maqFuenteDato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacion.relacionMaqFuenteDatos')),
            ],
            options={
                'db_table': 'relacionMaqFuenteDatosVarInd',
            },
        ),
        migrations.AlterField(
            model_name='relacioncomppredictivoresult',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 16, 9, 24, 405154)),
        ),
    ]
