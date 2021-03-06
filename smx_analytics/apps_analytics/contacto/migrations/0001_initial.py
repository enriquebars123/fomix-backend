# Generated by Django 2.1.2 on 2019-12-03 18:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contactoGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'db_table': 'contactoGrupo',
            },
        ),
        migrations.CreateModel(
            name='contactoNotificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'db_table': 'contactoNotificacion',
            },
        ),
        migrations.AddField(
            model_name='contactogrupo',
            name='notificacion',
            field=models.ManyToManyField(to='contacto.contactoNotificacion'),
        ),
        migrations.AddField(
            model_name='contactogrupo',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
