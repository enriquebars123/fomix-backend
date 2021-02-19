from __future__      import absolute_import, unicode_literals
import os
from celery           import Celery
from celery.schedules import crontab
from django.conf import settings
from datetime import date
from decouple import config


import asyncio
import datetime


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smx_analytics.settings')
app = Celery('smx_analytics') #Nota 1
app.config_from_object('django.conf:settings', namespace='CELERY') #Nota 2
app.autodiscover_tasks() #Nota 3
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


"""
Descomentar esta task backup_config

Nota: Complementar las tablas que faltan para hacer el backup.

@app.task(bind=True)
def backup_config(self):
    
    ruta = config('PATH_BACKUPS')
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
        os.system('python manage.py dumpdata '+ i +' >' + ruta + i + str(date.today()) + '.yaml')
        print('BACKUP '+ i + ': OK')
"""

app.conf.beat_schedule = {
    'backup_config': {
        'task': 'backup_config',
        #'schedule': crontab(minute=30)
        # Aqui cambiar el tiempo ejecución.
        "schedule": crontab(0, 0, day_of_month="1"),
    },
}


"""
Estos son ejemplos,
app.conf.beat_schedule = {
    'test_celery (100s)': {  #name of the scheduler
        'task': 'test_celery',  # task name which we have created in tasks.py
        'schedule': 2.0,  # set the period of running
        'args': ()  # set the args
    },
    'backup_config (10s)': {  #name of the scheduler
        'task': 'backup_config',  # task name which we have created in tasks.py
        'schedule': 10.0,  # set the period of running
        #"schedule": crontab(0, 0, day_of_month="1"),
        'args': ()  # set the args
    },
    'get_empresa (10s)': {  #name of the scheduler
        'task': 'get_empresa',  # task name which we have created in tasks.py
        'schedule': 3.0,  # set the period of running
        #"schedule": crontab(0, 0, day_of_month="1"),
        'args': ()  # set the args
    },
    'get_empresa (10s)': {  #name of the scheduler
        'task': 'test_celery2',  # task name which we have created in tasks.py
        'schedule': 5.0,  # set the period of running
        #"schedule": crontab(0, 0, day_of_month="1"),
        'args': ()  # set the args
    },
    'backup_config_30': {
        'task': 'test_backup_config',
        #'schedule': crontab(minute=30)
        "schedule": crontab(0, 0, day_of_month="1"),
    },
}
"""
