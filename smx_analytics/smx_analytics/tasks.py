from __future__ import absolute_import, unicode_literals
from celery     import shared_task
import os


@shared_task(name = "backup_config")
def backup_config():
    ruta_save = "backup/backups_config/"

    # Apps del modelo de Django
    tablas    = [
                'catalogo',
                'contacto',
                'metodo',
                'referencias',
                'regla',
                'relacion',
                'variables',
            ]
    for i in tablas:
        os.system('python manage.py dumpdata '+i+' >' + ruta_save + i +'.yaml')
        print('BACKUP '+ i + ': OK')

    return "ok"




