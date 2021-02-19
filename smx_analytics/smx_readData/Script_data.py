fuentedatos=[
           {
               "id": 1,
               "nombre": "test1",
               "urlregistro": "http://172.16.100.32:28000/api/v1/registro_json/",
               "urlcatalogo":"http://172.16.100.32:28000/api/v1/catalogoVariables_noSQL/",
               "urlvalidacion":"http://172.16.100.32:28000/api/v1/dispositivo_IoT/",
               "relacionMaquina": "12",
               "usuario": None,
               "contrasena": None,
               "paginacion": True,
               "filtros": {"campo_variable":"nombre_sensor",
                           "fecha":"fecha_inicio",
                           "fecha_fin":"fecha_final",
                           "relacion":"dispositivo_IoT",
                           "IDPieza":"no_parte"
                           },
                "estructuradatos": {"valorx":"valor",
                            "valory":"valor",
                            "referencia":"valor",
                            "fecha_ref":"fecha_creacion",
                            },

           },
           {
              "id": 2,
              "nombre": "test2",
              "urlregistro": "http://172.16.100.32:28000/api/v1/registro/",
              "urlcatalogo":"http://172.16.100.32:28000/api/v1/catalogoVariables_SQL/",
              "urlvalidacion":"http://172.16.100.32:28000/api/v1/dispositivo_IoT/",
              "relacionMaquina": "12",
              "usuario": None,
              "contrasena": None,
              "paginacion": True,
              "filtros": {"campo_variable":"nombre_sensor",
                          "fecha":"fecha_inicio",
                          "fecha_fin":"fecha_final",
                          "relacion":"dispositivo_IoT",
                          "IDPieza":"no_parte"
                          },
             "estructuradatos": {"valorx":"fecha_creacion",
                         "valory":"valor_float",
                         "referencia":"valor_string",
                         "fecha_ref":"fecha_creacion"},

           }
       ]

variablesindependientes=[
           {
               "id": 1,
               "nombre": "vibraciones_test_case4_Mod3/ai1",
               "fuenteDatos":2,
           },
          {
               "id": 1,
               "nombre": "corriente_test_case4_Mod4/ai1",
               "fuenteDatos":2,
           },        
          
       ]

import pandas as pd
import modulo_registros as  funciones_FD
import modulo_variables as  var_df
from datetime import datetime

df_fuenteDatos=pd.DataFrame.from_dict(fuentedatos)
variablesfD=var_df.get_df_variables(df_fuenteDatos)
datetime_str = None
IDpieza=None
FechaFilter={'inicio':datetime(2020,6,23,11,49,0),'fin':datetime(2020,6,23,11,50,0)}
struct_PP=False
list_varIndep=funciones_FD.get_reg_variablesIndependientes(variablesfD,df_fuenteDatos,variablesindependientes,FechaFilter,struct_PP,IDpieza)
#print(list_varIndep)

#Ejemplo de como se convertiria el dataframe en un diccionario
lst_var_Indep_dict=[]
for dict_indep_var in list_varIndep:
    
    dict_values=dict_indep_var['dataframe'].to_dict('list')
    dict_values['PP']=dict_indep_var['PP']
    lst_var_Indep_dict.append(dict_values)
    
###########################################################--------------------MAIN--------------------########################################################3
#
##Pasar los datos de fuente de datos a un dataframe
#FuenteDatos=receta["fuenteDatos"]
#
#df_fuenteDatos=pd.DataFrame.from_dict(FuenteDatos)
#variablesfD=get_df_variables(FuenteDatos,df_fuenteDatos)
##De las fuentes de datos se consiguen los valores del catalogo de VariablesIndependientes
#VariablesIndependientes=receta["VariablesIndependientes"]
#datetime_str = '2020-02-21 14:49:54.997439'
#datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
#FechaFilter=datetime_object
#IDpieza=None
#list_varIndep=get_variablesIndependientes(variablesfD,df_fuenteDatos,VariablesIndependientes,FechaFilter,IDpieza)
#

    