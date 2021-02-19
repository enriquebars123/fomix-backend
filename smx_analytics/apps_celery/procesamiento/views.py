
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import redis
from apps_celery.procesamiento.tasks import preProcesamiento_Btn


from smx_analytics.celery import *

class preProcesamiento(APIView):
    def post(self, request, *args, **kwargs):
        # connect with redis server as Alice
        task = preProcesamiento_Btn.delay()
        result = {
            "sucess": True,
            "id_task": task.id
        }
        return Response(result, status.HTTP_200_OK)
