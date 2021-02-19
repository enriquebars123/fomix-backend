"""Views de usuarios"""


# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
#from django.shortcuts import get_object_or_404
from rest_framework import status
from decouple import config
import uuid
from smx_analytics.libraryBusiness.libUtility import *


# serializer
from apps_user.smxAnalitica_user.api.serializers import (
    UserAreaSerializers,
    UserSerializers
)

from apps_analytics.catalogo.api.serializers import (
    PerfilSerializers
)

# Models
from apps_user.smxAnalitica_user.models import (
    userArea,
    user,
)
from apps_analytics.relacion.models import *
from apps_analytics.catalogo.models import *


# Utilerias
from smx_analytics.utilerias import GeneralViewSetMixin


class UserAreaViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = userArea.objects.all()
    serializer_class = UserAreaSerializers


class UserViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['usuario', 'email', 'nombre']
    filter_backends = [DjangoFilterBackend,]
    queryset = user.objects.all()
    serializer_class = UserSerializers

    def retrieve(self, request, pk):
        
        instancia = self.get_object()
        serializer = UserSerializers(instancia)
        data = serializer.data.copy()
        if instancia.foto != '' :             
            data['foto'] = "{0}://{1}".format(request.scheme, request.get_host()) + instancia.foto.url
        ListPerfiles = []
        ListMenu =[]
        refperfil = relacionUserPerfil.objects.filter(user=instancia).values('perfil','id')
        Objrefperfil = refperfil.all().values('perfil')
        refmenu = relacionPerfilMenu.objects.filter(perfil__in=Objrefperfil)
        menu = catalogoMenu.objects.filter(id__in=refmenu.values('menu'))
        if Objrefperfil.count() :
            Objperfil = catalogoPerfil.objects.filter(id__in=Objrefperfil)
            for op in Objperfil:
                obj = refperfil.get(perfil=op.id)
                strucPerfil ={
                    "idRef": obj.get('id'),
                    "id":op.id,
                    "nombre": op.nombre
                }
                #print("perfiles: ",op.nombre)
                for rmenu in refmenu:          
                    if op.id == rmenu.perfil.id:
                        for m in menu:
                            #print(m.id)
                            #print(rmenu.menu.id)
                            if rmenu.menu.id == m.id:
                                strcMenu = {
                                    "id": m.id,
                                    "nombre": m.nombre,
                                    "nivel": m.nivel,
                                    "parent": m.parent,
                                    "icon": m.icon,
                                    "url": m.url,
                                    "orden": m.orden
                                }
                                #print("menus: ",m.nombre)
                                ListMenu.append(strcMenu)    
                ListPerfiles.append(strucPerfil)
            data['perfiles'] = ListPerfiles
            # ordeno los menus y descarto repetidos
            data["menus"] = {menu['id']: menu for menu in ListMenu}.values()
            return Response(data)
        else :
            data['perfiles'] = ListPerfiles
            data["menus"] = {menu['id']: menu for menu in ListMenu}.values()
            return Response(data)

        return Response(serializer.data)

    """
    def update(self, request, *args, **kwargs):
        mhttp_status = None
        instancia = self.get_object()
        print("este es request.data")
        print(request.data)
        if isinstance(request.data['foto'], (str, list, dict, tuple)):
            del request.data['foto']
        serializer = self.get_serializer(instancia, data=request.data,)
        print("este es el seriali")
        print(serializer)
        if serializer.is_valid():
            self.perform_update(serializer)
            instancia.save()
            success = True
            msg = "Usuario Modificado Correctamente"
            mhttp_status = status.HTTP_202_ACCEPTED
        else:
            success = False
            msg = "%s" % serializer.errors
            mhttp_status = status.HTTP_400_BAD_REQUEST

        return Response({
            'success': success,
            'msg': msg
        }, mhttp_status)
    """

    
    def create(self, request, *args, **kwargs):     
        server = utility.get_server(self, request.build_absolute_uri(), request.path) 
        #print(server)
        #server = request.build_absolute_uri(url)
        #print(server + config('activateAccount'))  
        data = request.data.copy()
        if not 'area' in data :
            dato = userArea.objects.filter(nombre="defaulData")
            if dato.count() > 0:
                id = dato.id
            else:
                id = userArea.userAreaDeafult(self)
                data['area'] = id
        uid = str(uuid.uuid4())
        url = server + config('activateAccount') + uid
        data['token'] = uid
        serializer = self.get_serializer(data=data)
        if self.get_queryset().filter(
            usuario=request.data['usuario']
        ).exists():
            success = False
            mhttp_status = status.HTTP_400_BAD_REQUEST
            msg = "Usuario ya existente"
            return Response({'success': success, 'msg': msg}, mhttp_status)
        else:
            admin = relacionUserPerfil.objects.filter(perfil=1)
            listEmail = []
            for item in admin:
                listEmail.append(item.user.email)
            #print(listEmail)
            contenido = str(config('contenido_Activacion')).format(url,url)
            #print(contenido)
            result = utility.Gmail(self, config('asunto_Activacion'), listEmail, contenido)
            #print(result)
            result = {'success' : True}
            if result['success'] == False : 
                return Response(result, status.HTTP_400_BAD_REQUEST)
            if serializer.is_valid():
                obj = serializer.save()
                success = True
                msg = "Usuario Guardado Correctamente - Se envio un correo para activar usuario."
                mhttp_status = status.HTTP_201_CREATED
                return Response({
                    'success': success,
                    'msg': msg,
                    'id': obj.id
                }, mhttp_status)
            else:
                success = False
                msg = "%s" % serializer.errors
                mhttp_status = status.HTTP_400_BAD_REQUEST
                return Response({'success':success, 'msg':msg}, mhttp_status)
    

    def list(self, request):
        ListUsuario = []
        User = self.get_queryset()
        for itemUser in User:    
            #print(itemUser.foto)
            ListPerfil = []
            objPerfil = relacionUserPerfil.objects.filter(user=itemUser.id)
            for itemPerfiles in objPerfil:
                ListPerfil.append(PerfilSerializers(itemPerfiles.perfil).data)
            u = UserSerializers(itemUser).data
            if itemUser.foto != "" :                
                u['foto'] = "{0}://{1}".format(request.scheme, request.get_host()) + itemUser.foto.url
            u['perfiles']= ListPerfil
            ListUsuario.append(u)
        result = ListUsuario
        return Response(result, status.HTTP_200_OK)