##########################################################################################        
#                           Author: Juana Noemi Perez Montoya                            #
#                                   Company: SISAMEX                                     #
##########################################################################################       
    
import pandas as pd
import smx_readData.modulo_APIrequests as  API
import smx_readData.modulo_generales_df as gen_df


#Funcion principal
def get_df_variables(df_fuenteDatos):
    """
    Retorna un dataframe con todas las variables de las fuentes de datos
    """
    variablesfD=pd.DataFrame(columns=['fuenteDatos','nombre_variable','limite','consultaData'])    
    for indice_fila, fila in df_fuenteDatos.iterrows():
        auth=gen_df.get_auth_fromDF(fila)
        catalogoVar=fila["urlcatalogo"]
        relacionmaq=fila["relacionMaquina"]
        api=catalogoVar+relacionmaq+"/"
        try:
            variablesmaq=request_variablesmaq(api,auth)
            variablesfD=get_variablesfD(fila,variablesmaq,variablesfD)
        except:
            print("No hay datos en la fuente de datos para la maquina dada")
            
    return variablesfD

######################################## Funciones auxiliares ########################################
    
def request_variablesmaq(api,auth):
    """
    Hace un request a la API de catalogo de variables de una fuente de datos
    """
    catVar={"api":api,
                    "filtering":None,
                    "auth":auth
                    }
    variablesmaq=API.GetData(catVar)['variables']
    
    return variablesmaq
    


def get_variablesfD(fuentedatos,variablesmaq,variablesfD):
    """
    Estructura las variables contenidas en variablesmaq a un dataframe.
    """
    for var in variablesmaq:
        consultadata=var['consultaData']
        variable_name=var['nombre_variable']
        dict_nom_ref=obtener_nombres_ref_and_PP(variable_name,consultadata)
        dictvar={'fuenteDatos':fuentedatos['id'],
                 'nombre_variable':variable_name,
                 'limite':var['limite'],
                 'nombres_referencia':dict_nom_ref,
                 'consultaData':consultadata
                 }
        variablesfD=variablesfD.append(dictvar,ignore_index = True)
    
    return variablesfD

def obtener_nombres_ref_and_PP(variable_name,consultadata):
    """
    Obtiene los diferentes nombres de referencia y si es ya se encuentra preprocesado
    dependiendo del consultasubvar de una fuente de datos
    """
    
    nom_ref=[]
    PP_list=[]
    if consultadata !=None:
        subvar_values=list(consultadata.values())
        for lst_ref in subvar_values:
            for i in lst_ref:
                ref_name=i['nombre_referencia']
#               index_PP = ref_name.find(variable_name)+len(variable_name)
#               PP_name=ref_name[index_PP:]
#               print(PP_name)
                   #Verificar si existe preproecesamiento
                PP=gen_df.verify_field_df(i,'preprocesado')  
                if not ref_name in nom_ref:     
                    nom_ref.append(ref_name)  
                    PP_list.append(PP)

    else:
        nom_ref.append(variable_name)
        PP_list.append(False)
    
    dict_nom_ref = dict(zip(nom_ref,PP_list))
    return dict_nom_ref