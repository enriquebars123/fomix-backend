# Generated by Django 2.1.2 on 2020-03-27 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_auto_20200327_0021'),
        ('catalogo', '0023_auto_20200326_1440'),
        ('regla', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regla',
            old_name='inferior',
            new_name='lcl',
        ),
        migrations.RenameField(
            model_name='regla',
            old_name='superior',
            new_name='lsl',
        ),
        migrations.RemoveField(
            model_name='regla',
            name='componente',
        ),
        migrations.RemoveField(
            model_name='regla',
            name='nombre',
        ),
        migrations.AddField(
            model_name='regla',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contacto.contactoDepartamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regla',
            name='ext',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='regla',
            name='nombreCrador',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regla',
            name='nominal',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regla',
            name='notificacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contacto.contactoNotificacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regla',
            name='ucl',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regla',
            name='usl',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regla',
            name='variable',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalogo.catalogoVariable'),
            preserve_default=False,
        ),
    ]
