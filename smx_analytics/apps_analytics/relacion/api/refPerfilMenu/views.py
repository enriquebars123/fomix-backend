# Django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps_analytics.catalogo.models import catalogoMenu
from rest_framework.views import APIView

#from itertools import islice
from apps_analytics.relacion.models import (
    relacionUserPerfil,
    relacionPerfilMenu
)
from apps_analytics.catalogo.models import (
    catalogoMenu,
    catalogoPerfil
)


class DeletePerfilMenu(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            relacionPerfilMenu.objects.filter(id__in=data).delete()
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


class bulkPerfilMenu(APIView):
    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        JSONPM = request.data
        batch_size = 100
        objs = []
        for objcPM in JSONPM:
            objs.append(
                relacionPerfilMenu(
                    perfil=catalogoPerfil.objects.get(pk=objcPM.get('perfil')), 
                    menu=catalogoMenu.objects.get(pk=objcPM.get('menu'))
                )
            )

        relacionPerfilMenu.objects.bulk_create(objs)

     
        if objs:
            r = {
                'success': False,
                'msg': 'excelente'
            }
            return Response(r, status.HTTP_200_OK)
        else:
            r = {
                'success': False,
                'msg': 'Proporcione credenciales correctas'
            }

        return Response(r, status.HTTP_401_UNAUTHORIZED)
