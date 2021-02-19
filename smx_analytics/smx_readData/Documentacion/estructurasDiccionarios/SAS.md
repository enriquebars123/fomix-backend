# Diccionario ejemplos como entrada

## Diccionario de fuente de datos
Es necesario que este tenga las siguientes llaves con su nombre exacto. 

Como ejemplo, se tienen las fuentes de datos de IoT
```
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
```       
       
## Variables independientes
Este diccionario debe contener el nombre de la variable como aparece en los catalogos de las fuentes de datos y el id de la fuente de datos a la que pertenece según el diccionario anterior.

Como ejemplo se muestran dos variables independientes de las fuentes de IoT:

```      
variablesindependientes=[
           {
               "id": 1,
               "nombre": "vibraciones_test_case4_Mod3/ai1",
               "fuenteDatos":1,
           },
          {
               "id": 1,
               "nombre": "corriente_test_case4_Mod4/ai1",
               "fuenteDatos":2,
           },        
          
       ]
```  