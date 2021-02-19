""" Utilerias generales de la plataforma """
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.db.models.deletion import ProtectedError
from rest_framework import status


class GeneralViewSetMixin(object):

    def create(self, request, *args, **kwargs):
        #r = request.data.copy()
        serializer = self.get_serializer(data=request.data)
        mhttp_status = None
        respuesta = None
        if serializer.is_valid():
            obj = serializer.save()
            serializer = self.get_serializer(obj)
            #r["id"] = obj.id
            mhttp_status = status.HTTP_201_CREATED
            respuesta = {
                'success': True,
                'msg': 'Registro Creado',
                'data' : serializer.data
            }
        else:
            mhttp_status = status.HTTP_400_BAD_REQUEST
            respuesta = {
                'success': False,
                'msg': '%s' % serializer.errors,
                'result' : []
            }

        return Response(respuesta, mhttp_status)

    def destroy(self, request, *args, **kwargs):
   
        instancia = self.get_object()
        print(instancia)
        mhttp_status = None
        respuesta = None
        try:
            self.perform_destroy(instancia)
            mhttp_status = status.HTTP_202_ACCEPTED
            respuesta = {
                'success': True,
                'msg': 'Registro Eliminado'
            }

        except ProtectedError as error:
            mhttp_status = status.HTTP_400_BAD_REQUEST
            respuesta = {
                'success': False,
                'msg': 'Error al eliminar registro'
            }

        return Response(respuesta, mhttp_status)

    def update(self, request, *args, **kwargs):
        instancia = self.get_object()
        mhttp_status = None
        respuesta = None
        serializer = self.get_serializer(instancia, data=request.data,)
        if serializer.is_valid():
            mhttp_status = status.HTTP_202_ACCEPTED
            self.perform_update(serializer)
            respuesta = {
                'success': True,
                'msg': 'Registro Actualizado',
                'data': serializer.data
            }
        else:
            mhttp_status = status.HTTP_400_BAD_REQUEST
            respuesta = {
                'success': False,
                'msg': '%s' % serializer.errors
            }
        return Response(respuesta, mhttp_status)
