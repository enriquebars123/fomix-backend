# Django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apps_analytics.relacion.models import relacionPredFuenteDatos 
from smx_analytics.celery import *

class DeletePredFueteDatos(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            relacionPredFuenteDatos.objects.filter(id__in=data).delete()
            result = {
                'success': True,
                'msg': 'Datos Eliminados correctamente...'
            }
            return Response(result, status.HTTP_200_OK)
        except:
            result = {
                'success': False,
                'msg': 'Ha ocurrido un error'
            }
            return Response(result, status.HTTP_400_BAD_REQUEST)