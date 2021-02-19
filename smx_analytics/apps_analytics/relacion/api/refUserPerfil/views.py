from rest_framework.response import Response
from rest_framework import status
from apps_user.smxAnalitica_user.models import user
from apps_analytics.catalogo.models import catalogoPerfil
from rest_framework.views import APIView
from itertools import islice
from apps_analytics.relacion.models import (
    relacionUserPerfil,
)


class DeleteUserPerfil(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            relacionUserPerfil.objects.filter(id__in=data).delete()
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


class bulkUserPerfil(APIView):
    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        JSONUP = request.data
        objs = []
        for objcUP in JSONUP:
            objs.append(
                relacionUserPerfil(
                    user=user.objects.get(pk=objcUP.get('user')),
                    perfil=catalogoPerfil.objects.get(pk=objcUP.get('perfil')), 
                )
            )

        relacionUserPerfil.objects.bulk_create(objs)
        
        if objs:
            r = {
                'success': True,
                'msg': 'excelente'
            }
            return Response(r, status.HTTP_200_OK)
        else:
            r = {
                'success': False,
                'msg': 'error'
            }
            return Response(r, status.HTTP_400_BAD_REQUEST)
