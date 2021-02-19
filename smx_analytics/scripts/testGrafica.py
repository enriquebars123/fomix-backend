from apps_analytics.relacion.models import (
    relacionMaqFuenteDatos,
    relacionMaqFuenteDatosVarInd,
)
from apps_analytics.relacion.api.serializers import (
    CompPredictivoResultSerializers,
    
)
from datetime import datetime
from apps_analytics.referencias.models import referenciaDmcCiclo
from apps_analytics.referencias.api.serializers import RefDmcCicloSerializers
from apps_analytics.catalogo.api.serializers import (
    FuenteDatosSerializers
)
import pdb;
import smx_readData.modulo_registros as  funciones_FD
import smx_readData.modulo_variables as  var_df
import pandas as pd
def reporteIndependiente(maq,dmc):
    #print(request)
    try:
        #format = "%Y-%m-%d %H:%M:%S.%f"
        #maq = request.GET['maquina']
        #dmc = request.GET['dmc']
       
        objMaqFD =  relacionMaqFuenteDatos.objects.filter(maquina=maq)
        #print(objMaqFD)
        objRefDmc = referenciaDmcCiclo.objects.get(maquina=maq,dmc=dmc)
        #print(objRefDmc)
        fechaIni = objRefDmc.fechaIni.astimezone().strftime('%Y-%m-%d %H:%M:%S')
        fechaFin = objRefDmc.fechaFin.astimezone().strftime('%Y-%m-%d %H:%M:%S')
        datetime_str = '09/19/18 13:55:26'

        datetime_ini = datetime.strptime(fechaIni, '%Y-%m-%d %H:%M:%S')
        datetime_fin = datetime.strptime(fechaFin, '%Y-%m-%d %H:%M:%S')

        print(type(datetime_ini))
        print(datetime_ini)  # printed in default format
      
        #print(fechaFin)
        listFuenteDatos = []
        for item in objMaqFD:
            print("entre al for")
            idFuente = item.fuenteDatos.id
            idmaquina = item.referenciaId
            nomFuente = item.fuenteDatos.nombre
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
                
                #pdb.set_trace()
                
                #print(fuentedatos)
                fuentedatos_list=[]
                fuentedatos_list.append(fuentedatos)

                df_fuenteDatos=pd.DataFrame.from_dict(fuentedatos_list)
               
                variablesfD=var_df.get_df_variables(df_fuenteDatos)
                #print(variablesfD)
                #datetime_str = None
                IDpieza=None
              
             
                #FechaFilter={'inicio':datetime_ini, 'fin':datetime(2020, 2, 21, 14, 30, 9)} #'fin':datetime_fin }
                #FechaFilter={'inicio':datetime(2020,6,23,11,49,0),'fin':datetime(2020,6,23,11,50,0)}
                FechaFilter={'inicio':datetime(2020,2,21,14,30,8),'fin':datetime(2020, 2, 21, 14, 30, 9)}
                #FechaFilter={'inicio':datetime(2020,6,23,11,49,0),'fin':datetime(2020,6,23,11,50,0)}
                #print(FechaFilter)
                struct_PP=False
                list_varIndep=funciones_FD.get_reg_variablesIndependientes(variablesfD,df_fuenteDatos,variablesindependientes,FechaFilter,struct_PP,IDpieza)
                #print(list_varIndep)

                #Ejemplo de como se convertiria el dataframe en un diccionario
                lst_var_Indep_dict=[]
                for dict_indep_var in list_varIndep:
                    #print(dict_indep_var['nombre'])
                    dict_values=dict_indep_var['dataframe'].to_dict('list')
                    #print(dict_values)
                    #print("valor x")
                    #print(dict_values['valorx'])
                    #print("valor y")
                    #print(dict_values['valory'])
                    dict_values['nombre'] = dict_indep_var['nombre']
                    dict_values['PP']=dict_indep_var['PP']
                    lst_var_Indep_dict.append(dict_values)
                    #print(lst_var_Indep_dict)
                jsonFuenteDatos = {
                    'fuenteDatos': nomFuente,
                    'graficas' : lst_var_Indep_dict,
                }
                listFuenteDatos.append(jsonFuenteDatos)
                print(listFuenteDatos)

            
        result = {'detail': 'No encontrado.'}
    except :
        result = {'detail': 'No encontrado.'}

    return result


def run():
    reporteIndependiente(1,23763467)