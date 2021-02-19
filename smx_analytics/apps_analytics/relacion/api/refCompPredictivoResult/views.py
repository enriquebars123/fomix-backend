from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests
from requests.auth import HTTPBasicAuth
from apps_analytics.relacion.models import (
    relacionCompPredictivo,
    relacionMaqFuenteDatos,
    relacionPredFuenteDatos,
    relacionCompPredictivoResult,
    relacionMaqFuenteDatosVarInd,
)
from apps_analytics.relacion.api.serializers import (
    CompPredictivoResultSerializers,
    
)
from apps_analytics.referencias.models import referenciaDmcCiclo
from apps_analytics.referencias.api.serializers import RefDmcCicloSerializers
from apps_analytics.catalogo.api.serializers import (
    VariableSerializers,
    FuenteDatosSerializers
)
from apps_analytics.catalogo.models import (
    catalogoComponente,
    catalogoVariable,
)

from apps_analytics.referencias.models import referenciaMaquina
from datetime import datetime   
from dateutil.parser import parse
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from apps_analytics.catalogo.api.serializers import PredictivoSerializers
import pytz
import json
import pandas as pd
import smx_readData.modulo_registros as  funciones_FD
import smx_readData.modulo_variables as  var_df

#requests.get('http://sam-rdsdev/api/reportes/fomix/?fecha_inicio=2019-11-01&fecha_fin=2019-11-30', auth=HTTPBasicAuth('cecilio-diaz', 'Sisamex.17#'))

class predictivosItems(APIView):
    
    def get_object(self, maq, pz):
        return relacionCompPredictivo.objects.filter(maquina=maq, componentes=pz)

    def get(self, request):
        try:
            maq = request.GET['maquina']
            pz = request.GET['componente']
            instance = self.get_object(maq, pz)
            listPredict = []
           
            for itemPredic in instance:
                #print(itemPredic)
                listPredict.append({
                    'idCompPred':itemPredic.id,
                    "predictivo": PredictivoSerializers(itemPredic.predictivo).data
                })
            result = {
                "success": True,
                "data": listPredict
            }
            #print(result)
            return Response(result, status.HTTP_200_OK)
        except :
            result = {'detail': 'No encontrado.'}
            return Response(result , status.HTTP_401_UNAUTHORIZED)
       
class reporteRealPredictivo(APIView):     
            
    def getResultRealQDA(self, maq, pz, fini, ffin):
        objFuenteDatos = relacionMaqFuenteDatos.objects.filter(maquina=maq)
        #print(objFuenteDatos)
        nomComponente = catalogoComponente.objects.get(id=pz)
        #print(nomComponente)
        ListQDA = []
        listMes = []
        listQDA = []

        for objFD in objFuenteDatos :  
            #print(objFD.fuenteDatos)
            if objFD.fuenteDatos.tipoFuente == 3 and objFD.fuenteDatos.tipoConsulta==1:  
                #print("entrdhhhehe")
                #print(fini)
                fecha_inicio = datetime.strptime(fini, '%Y-%m-%d %H:%M:%S.%f')
                #print(fecha_inicio)
                fecha_fin = datetime.strptime(ffin, '%Y-%m-%d %H:%M:%S.%f')
                #print(fecha_fin)
                fi = fecha_inicio.strftime('%Y-%m-%d')
                ff = fecha_fin.strftime('%Y-%m-%d')
                
                url = objFD.fuenteDatos.urlRegistro + "?descripcion=" + objFD.referenciaId  + "&fecha_inicio=" + fi + "&fecha_fin=" + ff
                #print(url)
                #url = objFD.fuenteDatos.urlRegistro + str(objFD.fuenteDatos )
                #QDADmc/?maquina=OP150&componente=DS_A9482620103&fechaIni=20200301&fechaFin=20200313
                try:
                    #requests.get('http://sam-rdsdev/api/reportes/fomix/?fecha_inicio=2019-11-01&fecha_fin=2019-11-30', )
                    #print(objFD.fuenteDatos.usuario)
                    #print(objFD.fuenteDatos.contrasena) 
                    response = requests.get(url, auth=HTTPBasicAuth(objFD.fuenteDatos.usuario, objFD.fuenteDatos.contrasena))
                    #print(response)
                    if response.status_code==200:  # Verificar que exista conectividad con la URL
                        content = response.json()
                        #print(content)
                        for item in content:
                            #print(item['numero_serie'])
                            listMes.append({ 
                                'info': "REPORTE",
                                'folio': item['numero_serie'],
                                'date': ""
                            })
                            #listMes.append(item)
                        #print(listMes)
                        #df = pd.DataFrame(listMes)
                        #print(df)
                except :
                    print("------------ERROR----------------")
                    print(url)
            elif objFD.fuenteDatos.tipoFuente == 2 and objFD.fuenteDatos.tipoConsulta== 2:
                
                url = objFD.fuenteDatos.urlRegistro + "?maquina=" + objFD.referenciaId + "&componente=" + nomComponente.info + "&fechaIni=" + fini + "&fechaFin=" + ffin
                #url = objFD.fuenteDatos.urlRegistro + str(objFD.fuenteDatos )
                #QDADmc/?maquina=OP150&componente=DS_A9482620103&fechaIni=20200301&fechaFin=20200313
                #print("QDA")
                #print(url)
                try:
                    user = objFD.fuenteDatos.usuario
                    passw = objFD.fuenteDatos.contrasena
                    if user != "" and passw != "" :
                        response = requests.get(url, auth=HTTPBasicAuth(user, passw))
                    else :
                        response = requests.get(url)

                   
                    print(response.status_code)
                    if response.status_code==200:  # Verificar que exista conectividad con la URL
                        content = response.json()

                        for item in content:
                            #print(item)
                            listQDA.append(item)
                        #print(listQDA)
                except :
                    print("----------------------------------")
                    print(url)
                    return Response("error", status.HTTP_400_BAD_REQUEST)
        #print("entre aki al filter")
        #print(listMes)
        for item in listMes:
            filter_data = list(filter(lambda x :x['folio'] == item['folio'] ,listQDA))
            if len(filter_data):
                ListQDA.append(filter_data[0])
        #print(listQDA)
        #dato = filter(lambda x, y  : x['folio'] == y['folio'] , listMes, listQDA)
        #dato = map(filter(lambda x : x['folio'] == y, listQDA),listMes)
        #map(filterObj)
        #print(ListQDA)
        return ListQDA 

    def getResultPredictivo(self,predictivo, fi, ff):
        date_time_ini = datetime.strptime(fi, '%Y-%m-%d %H:%M:%S.%f')
        date_time_fin = datetime.strptime(ff, '%Y-%m-%d %H:%M:%S.%f')
       
        resultComPred = relacionCompPredictivoResult.objects.filter(compPredictivo=predictivo,fecha__range=[date_time_ini, date_time_fin])
        listResultPred = []
       
        for item in resultComPred:
           
            dato = CompPredictivoResultSerializers(item).data
          
            listResultPred.append({ 
                'info': "PREDICTIVO",
                'folio': str(dato['codigoPieza']),
                'date': dato['fecha'],
                'estatus': dato['estatus']
            })

        return listResultPred
    
    def get_object(self, pk):

        try:
            return relacionCompPredictivo.objects.get(id=pk)
        except relacionCompPredictivo.DoesNotExist:
            raise Http404


    def get(self, request):
        try:

            maq = request.GET['maquina']
            pz = request.GET['componente']
            comPred = request.GET['compredictivo']
            fi = request.GET['fechaIni']
            ff = request.GET['fechaFin']
            # paso 1 obtengo intancia de predictivo
            # parametro predictivo
            #instance = self.get_object(comPred)
            # paso 2 obtener medicion de piezas de QDA disponibles
            # parametros maquina y pieza con fecha de inicio y fecha fin
            ListResult = []

            resultRealQDA = self.getResultRealQDA(maq,pz,fi,ff)
            #print(resultRealQDA)
            resultPredictivo = self.getResultPredictivo(comPred, fi,ff)
            #print("result predictivo")
         
            # paso 3 obtengo resultados de predictivo
            #nomPz = instance.componentes.nombre
            #idPred =instance.predictivo.id
            #idMaq = instance.maquina.id 
        
            ListResult.extend(resultRealQDA)
            ListResult.extend(resultPredictivo)
            resultData = []
            if ListResult.count:
                resultData = sorted(ListResult, key=lambda x: x['date'])
            result = {
                "success": True,
                "data": resultData
            }
            return Response(result, status.HTTP_200_OK)
        except :
            result = {'detail': 'No encontrado.'}
            return Response(result , status.HTTP_401_UNAUTHORIZED)
       
class predictivoDMC(APIView):
    def get(self, request):
        try:
            dmc = request.GET['folio']
            objResult = relacionCompPredictivoResult.objects.get(codigoPieza=dmc)

            listVar = objResult.jsonPrediccion
            ListVariables = []
            for item in listVar:
                #print(item)
                try:        
                    itemVar = catalogoVariable.objects.get(id=int(item['id']))
                    serializer = VariableSerializers(itemVar).data
                    serializer['actvalue'] = float(item['result'])
                   
                    ListVariables.append(serializer)
                except catalogoVariable.DoesNotExist:
                    print("ocurrio un error al obtener catalogo de variables dependientes")
            if ListVariables.count:
            
                result = {
                    "success" : True,
                    "data" : {
                        "details": ListVariables
                    }
                }
            else :
                result = {
                    "success": False,
                    "data":[]
                }
            return Response(result, status.HTTP_200_OK)
        except :
            result = {'detail': 'No encontrado.'}

            return Response(result , status.HTTP_401_UNAUTHORIZED)

class reporteIndependiente(APIView):
    def get(self, request):
        try:
            #format = "%Y-%m-%d %H:%M:%S.%f"
            maq = request.GET['maquina']
            dmc = request.GET['dmc']
            #print(maq)
            #print(dmc)
            objMaqFD =  relacionMaqFuenteDatos.objects.filter(maquina=maq)
            #print(objMaqFD)
            objRefDmc = referenciaDmcCiclo.objects.get(maquina=maq,dmc=dmc)
            #print(objRefDmc)
            fechaIni = objRefDmc.fechaIni.astimezone().strftime('%Y-%m-%d %H:%M:%S')
            fechaFin = objRefDmc.fechaFin.astimezone().strftime('%Y-%m-%d %H:%M:%S')
            datetime_ini = datetime.strptime(fechaIni, '%Y-%m-%d %H:%M:%S')
            datetime_fin = datetime.strptime(fechaFin, '%Y-%m-%d %H:%M:%S')        
            #print(fechaFin)
            listFuenteDatos = []
            for item in objMaqFD:
                #print("entre al for")
                #print(item.fuenteDatos)
                idFuente = item.fuenteDatos.id
                #print(idFuente)
                idmaquina = item.referenciaId
                #print(idmaquina)
                nomFuente = item.fuenteDatos.nombre
                #print(nomFuente)
                #print("------------")
                #print(idFuente)
                objVar = relacionMaqFuenteDatosVarInd.objects.filter(maqFuenteDato=item.id)
                #print(len(objVar))
                if len(objVar):
                    variablesindependientes = []
                    for var in objVar:
                        variable = {
                            "id": 2,
                            "nombre": var.nombre,
                            "fuenteDatos" : idFuente
                        }
                        variablesindependientes.append(variable)
                    #print(variablesindependientes)
                    fuentedatos = FuenteDatosSerializers(item.fuenteDatos).data
                    fuentedatos['urlregistro'] = fuentedatos['urlRegistro']
                    fuentedatos['urlcatalogo'] = fuentedatos['urlCatalogo']
                    fuentedatos['urlvalidacion'] = fuentedatos['urlValComRel']
                    fuentedatos['relacionMaquina'] = idmaquina
                    fuentedatos['filtros'] = fuentedatos['filtro']
                    fuentedatos['estructuradatos'] = fuentedatos['estructura']
                    del fuentedatos['urlRegistro']
                    del fuentedatos['urlCatalogo']
                    del fuentedatos['urlValComRel']
                    del fuentedatos['filtro']
                    del fuentedatos['estructura']
                    del fuentedatos['tipoFuente']
                    del fuentedatos['tipoConsulta']
                    #print(fuentedatos)
                    #pdb.set_trace()
                    
                    #print(fuentedatos)
                    fuentedatos_list=[]
                    fuentedatos_list.append(fuentedatos)

                    df_fuenteDatos=pd.DataFrame.from_dict(fuentedatos_list)
                
                    variablesfD=var_df.get_df_variables(df_fuenteDatos)
                    #print(variablesfD)
                    #datetime_str = None
                    IDpieza=None
                
                
                    FechaFilter={'inicio':datetime_ini,'fin':datetime_fin } # 'fin':datetime(2020, 2, 21, 14, 30, 9) }
                    #FechaFilter={'inicio':datetime(2020,6,23,11,49,0),'fin':datetime(2020,6,23,11,50,0)}
                    #FechaFilter={'inicio':datetime(2020,2,21,14,30,8),'fin':datetime(2020, 2, 21, 14, 30, 9)}
                    #FechaFilter={'inicio':datetime(2020,6,23,11,49,0),'fin':datetime(2020,6,23,11,50,0)}
                    #print(FechaFilter)
                    struct_PP=False
                    list_varIndep=funciones_FD.get_reg_variablesIndependientes(variablesfD,df_fuenteDatos,variablesindependientes,FechaFilter,struct_PP,IDpieza)
                    #print(list_varIndep)

                    #Ejemplo de como se convertiria el dataframe en un diccionario
                    lst_var_Indep_dict=[]
                    for dict_indep_var in list_varIndep:
                        dict_values=dict_indep_var['dataframe'].to_dict('list')
                        dict_values['nombre'] = dict_indep_var['nombre']
                        dict_values['PP']=dict_indep_var['PP']
                        lst_var_Indep_dict.append(dict_values)
                    jsonFuenteDatos = {
                        'fuenteDatos': nomFuente,
                        'graficas' : lst_var_Indep_dict,
                    }
                    listFuenteDatos.append(jsonFuenteDatos)
                    #print(listFuenteDatos)
            result = {'success': True, 'msg': 'exito', 'result': listFuenteDatos }
        except  :
            result = {'detail': 'No encontrado.'}
        return Response(result , status.HTTP_200_OK)

class QDADmc(APIView):
    def get(self, request):
        folio = request.GET['folio']
        url = 'http://172.16.100.99:38000/api/v1/QDADmc/?folio=' + folio
        user = 'Fomix_CIMAT'
        password = 'Sisamex.2020'

        try:
            response = requests.get(url, auth=HTTPBasicAuth(user, password))
            return Response(response.json(), status=response.status_code)
        except:
            return Response({ 'detail': 'Internal Server Error' }, status=response.status_code)

