
receta={
       "id": 1,
       "predictivo": {
           "id": 1,
           "nombre": "Predictivo 1",
           "descripcion": "test 1"
       },
       "componentes": {
           "id": 1,
           "maquina": 1,
           "nombre": "MAIN_CHAFT_GRANDE",
           "descripcion": "test",
           "imagen": "/media/uploads/Untitled_Diagram.png"
       },
       "referencias": {
           "maquina": {
               "id": 1,
               "linea": 1,
               "nombre": "DR1014",
               "imagen": "/media/uploads/Untitled_Diagram_Cdiq5U6.png"
           },
           "linea": {
               "id": 1,
               "planta": 1,
               "nombre": "Carrier"
           },
           "planta": {
               "id": 1,
               "empresa": 1,
               "nombre": "Planta Componentes"
           },
           "empresa": {
               "id": 1,
               "nombre": "sisamex - planta componentes"
           }
       },
       "fuenteDatos": [
           {
               "id": 1,
               "nombre": "test1",
               "urlregistro": "http://172.16.100.32:28000/api/v1/registro_json/",
               "urlcatalogo":"http://172.16.100.32:28000/api/v1/catalogoVariables_noSQL/",
               "urlvalidacion":"http://172.16.100.32:28000/api/v1/dispositivo_IoT/",
               "relacionMaquina": "9",
               "usuario": None,
               "contrasena": None,
               "paginacion": True,
               "filtros": {"campo_variable":"nombre_sensor",
                           "fecha":"fecha_creacion",
                           "relacion":"dispositivo_IoT",
                           "IDPieza":"no_parte"
                           },
                "estructuradatos": {"valorx":"valor",
                            "valory":"valor",
                            "referencia":"valor",
                            "fecha_ref":"valor",
                            },

           },
           {
              "id": 2,
              "nombre": "test1",
              "urlregistro": "http://172.16.100.32:28000/api/v1/registro/",
              "urlcatalogo":"http://172.16.100.32:28000/api/v1/catalogoVariables_SQL/",
              "urlvalidacion":"http://172.16.100.32:28000/api/v1/dispositivo_IoT/",
              "relacionMaquina": "9",
              "usuario": None,
              "contrasena": None,
              "paginacion": True,
              "filtros": {"campo_variable":"nombre_sensor",
                          "fecha":"fecha_creacion",
                          "relacion":"dispositivo_IoT",
                          "IDPieza":"no_parte"
                          },
             "estructuradatos": {"valorx":"fecha_creacion",
                         "valory":"valor_float",
                         "referencia":"valor_string",
                         "fecha_ref":"fecha_creacion"},

           }
       ],
       "VariablesIndependientes": [
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
                   
                   
          
       ],
       "metodo_procesamiento": []
   }
       
       
       
import moduloFunciones as  funciones_FD
from datetime import datetime
import pandas as pd

#Pasar los datos de fuente de datos a un dataframe
FuenteDatos=receta["fuenteDatos"]

df_fuenteDatos=pd.DataFrame.from_dict(FuenteDatos)
variablesfD=funciones_FD.get_df_variables(df_fuenteDatos)
#De las fuentes de datos se consiguen los valores del catalogo de VariablesIndependientes
VariablesIndependientes=receta["VariablesIndependientes"]
datetime_str = '2020-02-24 15:33:11'
datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
FechaFilter=datetime_object
IDpieza=None
FechaFilter=None
list_varIndep=funciones_FD.get_variablesIndependientes(variablesfD,df_fuenteDatos,VariablesIndependientes,FechaFilter,IDpieza)
print(list_varIndep)
