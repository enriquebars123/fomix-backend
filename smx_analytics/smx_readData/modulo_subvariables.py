##########################################################################################        
#                           Author: Juana Noemi Perez Montoya                            #
#                                   Company: SISAMEX                                     #
##########################################################################################       
import pdb

def get_varI_df(varI_nombre,varI_fD,variablesfD):
    """
    Query para obtener los datos de una variable indpendiente especifica 
    desde el dataframe de variables
    """
    query='nombre_variable=="{0}" & fuenteDatos=={1}'.format(varI_nombre,varI_fD)
    varI_df=variablesfD.query(query)
    return varI_df    

def get_datosfDvar(varI_fD,df_fuenteDatos):
    """
    Query para obtener los datos de una fuente de datos con su id
    desde el dataframe de fuente de datos
    """
    #pdb.set_trace()
    query='id=="{0}"'.format(varI_fD)
    datosfDvar=df_fuenteDatos.query(query)
    datosfDvar=next(datosfDvar.iterrows())[1]
    return datosfDvar

def validacion_datos_subvariables(limitefd,varI_df,varI_nombre):
    """
    Verifica la existencia del limite y las subvariables en la variable especifica y actualiza.
    En caso de no existir, toma los valores de la fuente de datos o el por defecto.
    """
    
    limite=limitefd
    if varI_df.empty:
        subvariables=[varI_nombre]
        consultasubvar=None
    else:
        limite=varI_df["limite"].values[0]
        #Procesar el consultData, si no existe, entonces se toma el nombre de la variable
        consultasubvar=varI_df['consultaData'].values[0]
        if consultasubvar == None:
            subvariables=[varI_nombre]
        else:
            subvariables=list(consultasubvar.keys())

        
    return limite, subvariables,consultasubvar

