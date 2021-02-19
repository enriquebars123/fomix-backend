##########################################################################################        
#                           Author: Juana Noemi Perez Montoya                            #
#                                   Company: SISAMEX                                     #
##########################################################################################       
    
import requests
import json



def GetData(obj_data):
    """
    Hace una peticion tipo GET a un end-point
    """
    
    api=obj_data['api']
    filtering=obj_data['filtering']
    authorization=obj_data['auth']
    
    try:
        response=requests.get(api,params=filtering, timeout=5, auth=authorization)
        value=json.loads(response.text)
        code=response.status_code
    except Exception as a:
        print(a)
        response=None
        value=None
        code=None


    if code==200 or code==201:
        #print('API: DATOS CONSEGUIDOS de:',printvalue)
        try:
            value=value
            print('API: Datos conseguidos')
        except:
            value=None
            print('API: No hay datos')


    elif code==400:
        print('ERROR SOLICITUD INCORRECTA')
        value=None

    elif code==500:
        print('ERROR INTERNO EN EL SERVIDOR')
        value=None
    else:
        value=None

    return value

#from datetime import datetime
#date='2020-03-05T11:34:16.481862-06:00'
##date=datetime.strptime(date)
#date=datetime.now()
#
#obj_data={"api":'http://localhost:8000/api/v1/registro/',
#          "filtering":{"fecha_creacion__gte"},
#          "auth":None}
#x=GetData(obj_data)
#print(x)

#from datetime import datetime
#obj_data={"api":'http://172.16.100.32:28000/api/v1/registro/',
#          "filtering":{"maquina":9,"nombre_sensor":"vibraciones_test_case4_Mod3/ai0_FFT_A",
#                       "fecha_final":None},
#          "auth":None}
#x=GetData(obj_data)