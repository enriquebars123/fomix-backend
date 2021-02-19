from apps_analytics.relacion.models import (
    relacionMaqFuenteDatos,
    relacionPredFuenteDatos,
    relacionCompPredictivo
)
from apps_analytics.catalogo.api.serializers import VariableSerializers
from apps_analytics.catalogo.models import *
from apps_analytics.referencias.models import referenciaMaquina
from requests.auth import HTTPBasicAuth
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests
import uuid
from django.http import Http404
class DeleteMaqFuenteDatos(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            relacionMaqFuenteDatos.objects.filter(id__in=data).delete()
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


class bulkMaqFuenteDatos(APIView):
    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        JSONPM = request.data
        batch_size = 100
        objs = []
        for objcPM in JSONPM:

            objs.append(
                relacionMaqFuenteDatos(
                    maquina=referenciaMaquina.objects.get(pk=objcPM.get('maquina')),
                    fuenteDatos=catalogoFuenteDatos.objects.get(pk=objcPM.get('fuenteDatos')),
                    referenciaId=objcPM.get('referenciaId')
                )
            )

        relacionMaqFuenteDatos.objects.bulk_create(objs)

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

            return Response(r, status.HTTP_401_UNAUTHORIZED)


"""
   Para obtener la variables independientes permitidas de acuerdo a la tabla maqFuenteDatos.
"""

class variablesIndependientes(APIView):
    
    def get_object(self, pk):
        try:
            #print("entre")
            #print(pk)
            return relacionCompPredictivo.objects.get(id=pk)
        except relacionCompPredictivo.DoesNotExist:
            #print("esnte al var indeoen")
            result = { "success" : False, "msg" :"No existe predictivo" }
            raise Http404
           

    def get(self, request, pk, format=None):
        objPredic = []
        objData = {}
        #print("hpal")
        instance = self.get_object(pk)
        objFuenteDatos = relacionPredFuenteDatos.objects.filter(predictivo=instance.predictivo.id)
        #print(objFuenteDatos)
        idMaquina = instance.maquina.id
        nomMaq = instance.maquina.nombre
        ListData = []
        result = []
        ListVariable = []
        for objFD in objFuenteDatos :
            if objFD.fuenteDatos.tipoFuente == 1:
                objMaqFuenteDato = relacionMaqFuenteDatos.objects.get(maquina=idMaquina, fuenteDatos=objFD.fuenteDatos.id)
                url = objFD.fuenteDatos.urlCatalogo + objMaqFuenteDato.referenciaId
                nomFuenteDatos = objFD.fuenteDatos.nombre
                user = objFD.fuenteDatos.usuario
                passw = objFD.fuenteDatos.contrasena
                
                try:
                    if (user != None and user!="") and (passw != None and passw!=""):
                        response = requests.get(url, auth=HTTPBasicAuth(user, passw))
                    else :
                       
                        response = requests.get(url)
                    #print(nomFuenteDatos)
                    #print(url)
                    #print(response.status_code)
                    if response.status_code==200:  # Verificar que exista conectividad con la URL
                        content = response.json()
                        #print(content)
                        if not content['variables'] == None :
                            for itemJson in content['variables']:
                                
                                if 'consultaData' in itemJson:
                                    if itemJson['consultaData'] == None:
                                        listVariable = []
                                    else :
                                        #print("entre al consuldata")
                                        for item in itemJson['consultaData']:
                                            listVariable = []
                                            for variables in itemJson['consultaData'][item]:
                                                listVariable.append(variables['nombre_referencia'])
                                id = uuid.uuid4()
                                varJson = {
                                
                                    'idDinamica' : str(id.int),
                                    'fuenteDatos': nomFuenteDatos,
                                    'nombre_variable' : itemJson['nombre_variable'],
                                    'subVariables': listVariable
                                }
                                ListVariable.append(varJson)
                            objData = {
                                'maquina': nomMaq,
                                'variables': ListVariable
                            }
                            ListData.append(objData)
                    result = objData
                except :
                    print("------------ERROR----------------------")
                    print(url)
                  
                    result = {
                        "success" : False,
                        "msg" : "variables no disponible en Fuente de datos."
                         
                    }
                    
                    return Response(result, status.HTTP_400_BAD_REQUEST)
        return Response(result, status.HTTP_200_OK)

class variablesDependientes(APIView):
    
    def get_object(self, pk):
        try:
            return relacionCompPredictivo.objects.get(id=pk)
        except relacionCompPredictivo.DoesNotExist:
            print("no existe datos")
            raise Http404
    
    def get_variablsDependiente(self, pk):
        return catalogoVariable.objects.filter(componente=pk)

    def get(self, request, pk, format=None):
        objPredic = []
        #print(pk)
        instance = self.get_object(pk)

        #print(instance)
        objFuenteDatos = relacionPredFuenteDatos.objects.filter(predictivo=instance.predictivo.id)
        #print(objFuenteDatos)
        idComp = instance.componentes.id
        #print(idComp)
        nomMaq = instance.maquina.nombre 
        objVar = self.get_variablsDependiente(idComp)
        
        ListData = []
        result = []
        ListVariable = []
        for objFD in objFuenteDatos :
            if objFD.fuenteDatos.tipoFuente == 2:   
                nomFuenteDatos = objFD.fuenteDatos.nombre  
                for item in objVar:
                    varJson = {
                        'idDinamica' : item.id ,
                        'fuenteDatos': nomFuenteDatos,
                        'nombre_variable' : item.nombre,
                        'subVariables': []
                    }
                    ListVariable.append(varJson)
                objData = {
                    'maquina': nomMaq,
                    'variables': ListVariable
                }
                ListData.append(objData)
                result = objData
        return Response(result, status.HTTP_200_OK)

"""
class variablesDependientes(APIView):
    
    def get_object(self, pk):
        try:
            return relacionCompPredictivo.objects.get(id=pk)
        except relacionCompPredictivo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        objPredic = []
        instance = self.get_object(pk)
        objFuenteDatos = relacionPredFuenteDatos.objects.filter(predictivo=instance.predictivo.id)
        print(objFuenteDatos)
        idMaquina = instance.maquina.id
        nomMaq = instance.maquina.nombre
        nomComp = instance.componentes.nombre
        ListData = []
        result = []
        for objFD in objFuenteDatos :
            if objFD.fuenteDatos.tipoFuente == 2:                                        
                objMaqFuenteDato = relacionMaqFuenteDatos.objects.get(maquina=idMaquina, fuenteDatos=objFD.fuenteDatos.id)
                url = objFD.fuenteDatos.urlCatalogo + "?maquina=" + objMaqFuenteDato.referenciaId + "&componente=" + nomComp
                print(url)
                nomFuenteDatos = objFD.fuenteDatos.nombre
                try:   
                    response = requests.get(url)
                    print(response.status_code)
                    ListVariable = []
                    if response.status_code==200:  # Verificar que exista conectividad con la URL
                        content = response.json()
                        for itemJson in content['variables']:
                            if 'consultaData' in itemJson:
                                if itemJson['consultaData'] == None:
                                    listVariable = []
                                else :  
                                    print("entre al consuldata")
                                    for item in itemJson['consultaData']:  
                                        listVariable = []
                                        for variables in itemJson['consultaData'][item]:
                                            listVariable.append(variables['nombre_referencia']) 
                            varJson = {
                                'nombre_variable' : itemJson['nombre_variable'],
                                'subVariables': listVariable
                            }
                            ListVariable.append(varJson)
                        objData = {
                            'maquina': nomMaq,
                            'fuenteDatos': nomFuenteDatos,
                            'variables': ListVariable
                        }
                        ListData.append(objData)
                    result = ListData
                except :
                    print("-------------------")
                    print(url)
                    return Response("erro", status.HTTP_400_BAD_REQUEST)
        return Response(result, status.HTTP_200_OK)
"""
        
