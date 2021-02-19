##########################################################################################        
#                           Author: Juana Noemi Perez Montoya                            #
#                                   Company: SISAMEX                                     #
##########################################################################################       
    

from ast import literal_eval
import pandas as pd

#Funcion principal
def estructurar_datos_df(var_indp,estructuradatos,registros_df,dataFinal_df,consultasubvar,nombre_variable):
    """
    Estructura los datos de una consulta de registros segun la estructura adecuada.
    """
    try:
        res=dict((v,k) for k,v in estructuradatos.items())
        #Retorna solamente las columnas de interes
        registros_df=registros_df[registros_df.columns.intersection(res.keys())]
        if registros_df.empty:
            print('No hay datos nuevos de la variable')
        #Ver estructura especifica
        else:
            for indice_fila, fila in registros_df.iterrows():
                registro_indv=fila.to_dict()
                dataFinal_df=generar_registro(var_indp,consultasubvar,estructuradatos,registro_indv,dataFinal_df,fila,nombre_variable)
    except:
            print('No se especifico estructura de datos')  
            dataFinal_df= None
    return dataFinal_df

######################################## Funciones auxiliares ########################################

def generar_registro(var_indp,consultasubvar,estructuradatos,registro_indv,dataFinal_df,fila,nombre_variable):
    """
    Estructura un registro de acuerdo a la estructura especifica o a la de fuente de datos general
    """
    try:
        if consultasubvar!=None:
            #Estructura de datos especifica
            consulta=consultasubvar[var_indp]
            for referencias in consulta:
                newdict=create_newdict(referencias,estructuradatos,registro_indv)
                dataFinal_df=verify_empty_fields(newdict,dataFinal_df)
        else:
            #Estructura de datos general
            dataFinal_df=reg_indv_df_general(nombre_variable,fila,estructuradatos,dataFinal_df)
    except:
        print('Registro con estructura diferente')
    return dataFinal_df      

def create_newdict(referencias,estructuradatos,registro_indv):
    """
    Genera un nuevo diccionario con la estructura de la referencia especificamente.
    """
    nombre_variable=referencias['nombre_referencia']
    valorx=referencias['valorx']
    reg_valorx=get_value_dict(valorx,estructuradatos,registro_indv)
    valory=referencias['valory']
    reg_valory=get_value_dict(valory,estructuradatos,registro_indv)
    ref=referencias['referencia']
    reg_ref=get_value_dict(ref,estructuradatos,registro_indv)
    fecha_ref=referencias['fecha_ref']
    reg_fechaRef=get_value_dict(fecha_ref,estructuradatos,registro_indv)
    newdict={'nombre_referencia':nombre_variable,
             'valorx':reg_valorx,
             'valory':reg_valory,
             'referencia':reg_ref,
             'fecha_ref':reg_fechaRef
             }
    return newdict

def get_value_dict(referencia_reg,estructura,registro_indv):
    """
    Consigue el valor adecuado de cada campo de interes 
    segun la estructura dada en la referencia
    """
    if referencia_reg!=None:
        vectorref=referencia_reg[0]
        registro=registro_indv[estructura[vectorref]]
        if len(referencia_reg)>1:
            registro=literal_eval(registro)
            for i in referencia_reg[1:-1]:
                registro=registro[i]
                registro=literal_eval(registro)
            registro=registro[referencia_reg[-1]]
    else:
        registro=None
    return registro

def verify_empty_fields(newdict,dataFinal_df):
    """
    Verifica si el valor que se va a agregar le falta un valor de x o y.
    De ser asi hace un query para ver si ya algun registro al que haga referencia
    y actualiza el mismo registro.
    En caso contrario, lo agrega al dataframe.
    """
    try:
        if newdict['valorx']==None or newdict['valory']==None:
            #Verificar que referencias fecha sea igual
            #Verificar si tiene ventanas o no
            if newdict['referencia']==None:
                query='nombre_referencia=="{0}" & fecha_ref=="{1}"'.format(newdict['nombre_referencia'],newdict['fecha_ref'])
            else: 
                query='nombre_referencia=="{0}" & fecha_ref=="{1}" & referencia=="{2}"'.format(newdict['nombre_referencia'],newdict['fecha_ref'], newdict['referencia'])
            dataFinal_df=verify_values_difreg(dataFinal_df,query,newdict)
        else:
            #For en caso de que los valores sean listas
            #Si los valores no son listas:
            dataFinal_df = dataFinal_df.append(newdict , ignore_index=True)
    except:
        dataFinal_df=None
            
    
    return dataFinal_df

def verify_values_difreg(dataFinal_df,query,newdict):
    """
    Verifica si hay registros del mismo query y lo completa en caso de que sus valores de x o y hagan falta.
    """
    registroigual=dataFinal_df.query(query)
    if registroigual.empty:
        dataFinal_df = dataFinal_df.append(newdict , ignore_index=True)
    else:
        #valores del registro actual
        index=registroigual.index.item()  
        registrox=registroigual.valorx.item()
        registroy=registroigual.valory.item()
        #En caso de que falte el valor de x
        if registroy!=None and registrox==None :
           dataFinal_df.iloc[index,1]=newdict['valorx']
        #En caso de que falte el valor de y
        if registrox!=None and registroy==None :
           dataFinal_df.iloc[index,2]=newdict['valory']
    return dataFinal_df
           

def reg_indv_df_general(nombre_variable,fila,estructuradatos,dataFinal_df):
    """
    Forma registro indiviaul con la estructura general con la que se buscaron los datos.
    """
    registro_indv={"nombre_referencia":nombre_variable,
                   "valorx":fila[estructuradatos['valorx']],
                   "valory":fila[estructuradatos['valory']],
                   "fecha_ref":fila[estructuradatos['fecha_ref']],
                   "referencia":fila[estructuradatos['referencia']],
                   }
    dataFinal_df = dataFinal_df.append(registro_indv, ignore_index=True)
    return dataFinal_df
    

######################################## Segunda funcion principael
def final_struct(dataFinal_df,nom_ref,struct_PP):
    """
    Separa los nombres_ref de cada var_indep, les da la estructura final
    y genera vector de preprocesamiento.
    """
    dF_var_list=[]
    VPP=[]
    try:
        nom_ref=nom_ref.item()
        keysnom_ref=list(nom_ref.keys())
        for nombre in keysnom_ref:
            PP=nom_ref[nombre]
            df_filtered=separate_ref_name(nombre,dataFinal_df)
            df_filtered=struct_nom_ref(PP,df_filtered,struct_PP)

            var={'nombre':nombre,
                 'PP':PP,
                 'dataframe':df_filtered}
            dF_var_list.append(var)
    except:
        print('No hay datos de nombre_referencia')
    return dF_var_list, VPP

def separate_ref_name(nombre,dataFinal_df):
    """
    Hace un query a un dataframe para el nombre de referencia especifico
    """
    query='nombre_referencia=="{0}"'.format(nombre)
    df_filtered=dataFinal_df.query(query)   
    
    return df_filtered

def struct_nom_ref(PP,df_filtered,struct_PP):
    """
    Estructura el nombre_ref
    """
    df_filtered=verify_list_values(df_filtered)
    if struct_PP:
        df_filtered=verify_PP(df_filtered,PP)

    return df_filtered



def verify_list_values(df_filtered):
    """
    Verifica si el dataframe tiene valores lista. De ser así lo convierte a reg individuales y si no, los deja igual.
    """
    try:
        dt=df_filtered['valory'].dtype
        if dt == object: #Significa que es una lista
            try:
                df_filtered=convert_list_values(df_filtered) 
            except Exception as e:
                print(e)
    except:
        print('Sin valores para este nombre_ref')

    return df_filtered


def convert_list_values(df_filtered):
    """
    Convierte un dataframe cuyos valores son listas a valores sin listas
    """
    df_aux=pd.DataFrame(columns=['valorx','valory','fecha_ref','referencia'])
    for indice_fila, fila in df_filtered.iterrows():
        valorx=fila['valorx']
        valory=fila['valory']
        ref=fila['referencia']
        refexist=ref!=None
        fecha_ref=fila['fecha_ref']
        num_val=len(valorx)
        for i in range(num_val):
            if refexist:
                refs=ref[i]
            else:
                refs=ref
            newval={'valorx':valorx[i],
                    'valory':valory[i],
                    'referencia':refs,
                    'fecha_ref':fecha_ref
                    }

            df_aux=df_aux.append(newval, ignore_index=True)

    return df_aux

def verify_PP(df_filtered,PP):
    """
    Si la data es PP, lo pone en vector fila, si es no es PP toma como index el timestamp
    """
    #PP={'ejex':'Frequency',
     #   'ejey':'Amplitude'}
    
    df_filtered=verify_timstamp(df_filtered)
    
    if PP!=False and PP!=None:
        #Estructurar vector fila
        df_filtered=struct_PP(df_filtered,PP)
    else:
        df_filtered=df_filtered.set_index('valorx')
        
    
    return df_filtered

def struct_PP(df_filtered,PP):
    """
    Estructura el dataframe a vector fila
    """
#    #Acomodar por fecha de referencia
#    df_filtered['fecha_ref'] = pd.to_datetime(df_filtered['fecha_ref'])
#    df_filtered = df_filtered.sort_values(by = 'fecha_ref')
    try:
        name_ejex=PP['ejex']
        name_ejey=PP['ejey']

    except:
        print('Error en la estructura de preprocesamiento')
        name_ejex='x'
        name_ejey='y'
    #import pdb; pdb.set_trace()
    try:
        df_aux=pd.DataFrame()
        for indice_fila, fila in df_filtered.iterrows():
            ref=fila['referencia']
            if ref==None:
                ref=''
            else:
                ref='_'+ref
            df_aux[name_ejex+str(indice_fila)+ref]=[fila['valorx']]
            df_aux[name_ejey+str(indice_fila)+ref]=[fila['valory']]
    except Exception as e:
        print(e)
        
    return df_aux

def verify_timstamp(df_filtered):
    """
    Pone el index de valorx(timestamp) como index dado que es dato no preprocesado.
    """
    #Verificar que el valorx es un timestamp, o da error
    try:
        try:
            df_filtered.loc[:,'valorx']=df_filtered.loc[:,'valorx'].astype(float)
            df_filtered.loc[:,'fecha_ref'] = pd.to_datetime(df_filtered.loc[:,'fecha_ref'])
        except:
            #es una fecha
            df_filtered.loc[:,'valorx'] = pd.to_datetime(df_filtered.loc[:,'valorx'])
            
    except:
        print('Error al convertir la fecha en datetimefield')
    
    return df_filtered




#







