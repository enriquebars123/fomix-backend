
      
##########################################################################################        
#                           Author: Juana Noemi Perez Montoya                            #
#                                   Company: SISAMEX                                     #
##########################################################################################       
       
import pandas as pd
import smx_readData.modulo_APIrequests as  API
import smx_readData.modulo_generales_df as gen_df
import smx_readData.modulo_subvariables as subvar
import smx_readData.modulo_reg_estructura as reg_estr
import pdb                
#Funcion principal
def get_reg_variablesIndependientes(variablesfD,df_fuenteDatos,VariablesIndependientes,FechaFilter,struct_PP=False,IDpieza=None):
    """
    Retorna una lista de dataframes que contienen los registros acomodados por variable
    """
    list_varIndep=[]
    for i in VariablesIndependientes:
        #Se consultan los datos de la variables
        varI_fD=i['fuenteDatos']
        varI_nombre=i['nombre']
        varI_df=subvar.get_varI_df(varI_nombre,varI_fD,variablesfD) 
        datosfDvar=subvar.get_datosfDvar(varI_fD,df_fuenteDatos)     
        filtrosfD=datosfDvar["filtros"]
        limite=gen_df.verify_field_df(filtrosfD,'limite') 
        limite, subvariables,consultasubvar=subvar.validacion_datos_subvariables(limite,varI_df, varI_nombre)
        dataFinal_df=get_dataFinal_df(subvariables,datosfDvar,IDpieza,FechaFilter,consultasubvar,limite)
        #Quitar registros donde no existan los campos requeridos
        dataFinal_df=dataFinal_df.dropna(subset=['valorx', 'valory','fecha_ref'])  
        nom_ref=varI_df['nombres_referencia']
        dataFinal_df_list,VPP=reg_estr.final_struct(dataFinal_df,nom_ref,struct_PP)
        list_varIndep.extend(dataFinal_df_list)    
    
    return list_varIndep

######################################## Funciones auxiliares ########################################
def get_dataFinal_df(subvariables,datosfDvar,IDpieza,FechaFilter,consultasubvar,limite):
    """
    Retorna un dataframe con los registros de una variable independiente
    """
    
    relacion=datosfDvar["relacionMaquina"]
    api=datosfDvar["urlregistro"]
    paginacion=datosfDvar["paginacion"]
    estructuradatos=datosfDvar["estructuradatos"]
    filtrosfD=datosfDvar["filtros"]
    auth=gen_df.get_auth_fromDF(datosfDvar)
    dataFinal_df=pd.DataFrame(columns=['nombre_referencia','valorx','valory','fecha_ref','referencia'])
    for i in subvariables:
        nombre_variable=i
        registros=request_registros(filtrosfD,IDpieza,nombre_variable,relacion,FechaFilter,limite,api,paginacion,auth)
        #dataframe con los registros del request
        registros_df=pd.DataFrame(registros)
        #Cambiar los nombres de las columnas de acuerdo a la estructuradatos
        dataFinal_df= reg_estr.estructurar_datos_df(i,estructuradatos,registros_df,dataFinal_df,consultasubvar,nombre_variable)
    return dataFinal_df
            

def request_registros(filtrosfD,IDpieza,nombre_variable,relacion,fecha,limite,api,paginacion,auth):
    """
    Hace un request a la API de registros de la fuente de datos 
    """
    try:
        fecha_fin=filtrosfD['fecha_fin']
        fecha_fin_filter=fecha['fin']
    except:
        fecha_fin=None
        
    if fecha_fin==None:
        filtering={filtrosfD['campo_variable']:nombre_variable,
                      filtrosfD['relacion']:relacion,
                      filtrosfD['IDPieza']:IDpieza,
                      filtrosfD['fecha']:fecha['inicio'],
                      "limite":limite,
    
            }
    else:
        filtering={filtrosfD['campo_variable']:nombre_variable,
                      filtrosfD['relacion']:relacion,
                      filtrosfD['IDPieza']:IDpieza,
                      filtrosfD['fecha']:fecha['inicio'],
                      fecha_fin:fecha_fin_filter,
                      "limite":limite,
    
            }
    
    obj_data={"api":api,
              "filtering":filtering,
              "auth":auth,
              }
    registros=API.GetData(obj_data)
    try:
        if paginacion==True:
            registros=registros["results"]
    except:
        print("Sin datos o paginacion configurada incorrectamente")
    return registros













            
    


