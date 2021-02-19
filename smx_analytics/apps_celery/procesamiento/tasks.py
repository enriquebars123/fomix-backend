
import redis
import time
#from __future__ import absolute_import
from celery import task

#redis_client = redis.StrictRedis(host='redis', port=6379, db=0) 
@task(bind=True)
def preProcesamiento_Btn(self):
    task_id = self.request.id
    print(task_id)
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0) 
    print('entre')

    pronostico_task()

    print('time.sleep')
    redis_client.publish(str(task_id), "enntre al canal...")
    print('redis_client')
    redis_client.unsubscribe()
    print('sali') 


