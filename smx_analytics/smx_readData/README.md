# Lectura de fuente de datos
# Version V1.0

DESCRIPCIÓN: Este proyecto es para poder consultar diferentes fuentes de datos con estructuras diferentes.

## Versiones disponibles.

| Funciones                                  | v1.0  | 
| :---                                       | :---: | 
| Lectura de datos de diferentes REST API    | OK    | 
| Estructuración de datos flotantes o listas | OK    |
| Estructura para datos preprocesados        | OK    | 

OK: Funcionalidad incorporada.
X : Funcionalidad eliminada.
D : Funcionalidad en desarrollo.
P : Previsto a desarrollar


## Modo de uso

### Importar la librería

Este proyecto es importado como un módulo o libreria 
```
import Lectura_fuente_datos as read_fD
```

### Obtención de dataframes de variables y fuentes de datos
Estas funciones se llaman una sóla vez para leer los catalogos de variables de las fuentes de datos y obtener la estructura de las variables independientes.

```
df_fuenteDatos=pd.DataFrame.from_dict(fuentedatos)
variablesfD=read_fD.var_df.get_df_variables(df_fuenteDatos)

```

*  fuentedatos: Lista de diccionarios de fuente de datos


### Obtener los registros a partir de fecha de inicio
Posteriormente, cada cierto tiempo se hará llamar la función para traer los registros de las variables independientes a partir de una fecha señalada

```
list_varIndep=read_fD.funciones_FD.get_reg_variablesIndependientes(variablesfD,df_fuenteDatos,variablesindependientes,FechaFilter)
```

*  variablesfD:Lista de diccionarios con las fuentes de datos
*  df_fuenteDatos: Dataframe previamente obtenido de la fuente de datos.
*  variablesindependientes: Lista de diccionarios con los datos de las variables independientes
*  FechaFilter: Fecha a filtrar en los end-point
*  struct_PP: booleano para indicar si se quiere estructurar los datos preprocesados como vector fila

#### Nota:
La fecha es un diccionario con el siguiente formato:
```
{"inicio":datetime(2020,2,20,12,0),"fin":datetime(2020,2,20,12,5)}
```
La fecha fin puede ser omitida.

## Ejemplo de uso
El ejemplo se puede encontrar en el archivo llamado '''Script_main.py'''

## Consideraciones para el uso del script
1. Se requiere que los diccionarios (fuentes de datos, variables), tengan las claves con los nombres exactos. Para más información revisar Documentacion/estructurasDiccionarios/SAS.md
2. Se requiere tener acceso a las fuentes de datos.
3. Se requiere que las información de los catalogos de variables y de la estructura de las fuentes de datos sea correcta. Para más información sobre la estructura que debe tener, revisar Documentacion/estructuraDiccionarios/API.md
