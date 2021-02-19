##########################################################################################        
#                           Author: Juana Noemi Perez Montoya                            #
#                                   Company: SISAMEX                                     #
##########################################################################################       
    

#Autentificacion
def get_auth_fromDF(df):
    """
    Retorna la autentificacion en el formato adecuado para hacer los request
    """
    user=df['usuario']
    paswd=df['contrasena']
    if user !=None and user != '':
        auth=(user,paswd)
    else:
        auth=None
        print('entre')
    return auth


def filtrar_df_datetime(FechaFilter,dataFinal_df):
    """
    Filtra un dataframe por fecha
    """
    if FechaFilter!=None:
            try:
                filter_mask = dataFinal_df['fecha_ref'] > FechaFilter
                dataFinal_df=dataFinal_df[filter_mask]
            except:
                print("Problemas con la fecha dada para filtrar")
    return dataFinal_df

def verify_field_df(filtrosfD,namefield):
    """
    Verifica si existe un campo en la serie de dataframe. En caso de que no, retorna None
    """
    try:
        field=filtrosfD[namefield]
    except:
        field=None 
    return field
    