from rest_framework.response import Response
from rest_framework import status
import time
import os
# http return
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound    
from django.views.decorators.http import require_http_methods   

from apps_user.smxAnalitica_user.models import user
from apps_analytics.catalogo.models import catalogoMenu
from rest_framework.views import APIView
from apps_analytics.relacion.models import (
    relacionUserPerfil,
    relacionPerfilMenu
)
from apps_analytics.catalogo.models import (
    catalogoMenu,
    catalogoPerfil
)
from apps_analytics.catalogo.api.serializers import MenuSerializers
from apps_user.smxAnalitica_user.api.serializers import UserSerializers

 
def ActivateAccount(request,hash):

    print(hash)
    try:
        
        User = user.objects.get(token = hash)
        User.activo = True
        
        User.token = ""
        User.save()
        return render(request, 'ActivateAccount.html')
    except user.DoesNotExist: 
        return render(request, 'ActivateAccountFailure.html')
def redirectLogin(request):
        ip = os.environ.get('SERVER_FRONTEND_URL')
        path = os.environ.get('PATH_LOGIN')
        url = ip + path
        return redirect(url)
  

class Login(APIView):
    def post(self, request, *args, **kwargs):
       
       
        data = request.data
        aute = False
        if data:
            User = {}
            ListMenu =[]
            ListPefiles = []

            usuario = data.get('usuario')
            password = data.get('password')
            #print("Usuario swww:", usuario)
            try:
                objUser = user.objects.get(
                    usuario=usuario,
                )          
                #print(objUser)
                if objUser.activo:
                    #print("password swww:", objUser.check_password(password))
                    if objUser.check_password(password):
                        aute = True
                        #print(aute)
                    else:
                        result = {'success': False,'msg': 'Proporcione credenciales correctas'}
                        return Response(result, status.HTTP_401_UNAUTHORIZED)
                else: 
                    result = {
                        "success": False,
                        "msg": "Usuario temporalmente desactivado"
                    }
                    return Response(result, status.HTTP_403_FORBIDDEN)
                #print("aute")
                if aute:
                    Objrefperfil = relacionUserPerfil.objects.filter(user=objUser.id).values('perfil','id')
                    refperfil = Objrefperfil.all().values('perfil')
                    #print(refperfil)
                    #print(Objrefperfil)
                    Objperfil = catalogoPerfil.objects.filter(id__in=refperfil)
                    #print(Objperfil)
                    refmenu = relacionPerfilMenu.objects.filter(perfil__in=refperfil)
                    #print(refmenu)
                    menu = catalogoMenu.objects.filter(id__in=refmenu.values('menu'))
                    result = UserSerializers(objUser).data
                
                    result["perfiles"] = []
                    result["menus"] = []
                    #print("perfiles")
                    for op in Objperfil:
                        obj = Objrefperfil.get(perfil=op.id)
                        strcPerfil = {
                            "idRef": obj.get('id'),
                            "id": op.id,
                            "nombre": op.nombre,
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
                        ListPefiles.append(strcPerfil)
                    #print(objUser.foto)
                    if objUser.foto != '' :  
                        #print("1iue pqso")              
                        result['foto'] = "{0}://{1}".format(request.scheme, request.get_host()) + objUser.foto.url
                    result["perfiles"] = ListPefiles
                    # dato = sorted(result["menus"], key=lambda objeto: objeto[0])
                    result["menus"] = {menu['id']: menu for menu in ListMenu}.values()
                    return Response(result, status.HTTP_200_OK)
                else:
                    return Response(result, status.HTTP_401_UNAUTHORIZED)
            
            except:   
                result = { "success": False, "msg": "Proporcione credenciales correctas"}         
                return Response(result, status.HTTP_401_UNAUTHORIZED)

