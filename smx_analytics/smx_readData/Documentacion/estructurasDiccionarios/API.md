# Catalogo de variables

## Descripción
Cada fuente de datos debe contener una catalogo de variables que indique cómo debe ser su procesamiento.

Este catalogo debe de tener una estructura exacta para que funcione correctamente. 
### Estructura
```
{
    "maquina": {id_maquina},
    "variables": [
        {
            "nombre_variable": {nombre de la variable en terminos generales},
            "limite": {limite de datos a buscar por consulta},
            "consultaData": {
                {nombre de como se guardo la variable en los registros}: [
                    {
                        "nombre_referencia": {Como se busca que se llame},
                        "preprocesado": {
                            "ejex": {nombre del eje x},
                            "ejey": {nombre del eje y}
                        },
                        "valorx": [
                            {lista de valores para conseguir el valor unitario de x a partir de la estructura con la que se guardo la fuente de datos}
                        ],
                        "valory": [
                           {lista de valores para conseguir el valor unitario de y a partir de la estructura con la que se guardo la fuente de datos}
                        ],
                        "referencia": [{lista de valores para conseguir el valor unitario de la referencia a partir de la estructura con la que se guardo la fuente de datos}],
                        "fecha_ref": [
                            {lista de valores para conseguir el valor unitario de la fecha de referencia a partir de la estructura con la que se guardo la fuente de datos}
                        ]
                    }
                ],
                
            }
        }
    ]
}
```
### Notas
* El consultaData se puede omitir en caso de que sea un SQL normal
* El nombre de referencia se utiliza para determinar los valores de registros que hacen referencia a la misma fecha y a la misma variable pero están en diferentes registros.
* valorx, valory, referencia y fecha_ref pueden tener valores null en caso de que los registros no tengan esa información. Por ejemplo, si un registro contiene la información del valor de x y otro registro diferente el valor de y.
* La lista de valores dentro de valorx, valory, referencia y fecha_ref toman en cuenta que ya un valorx, valory, etc. base de la fuente de datos (a como fue configurada)

A continuación se verán algunos ejemplos para estructurar.

## Caso 1: SQL sin preprocesamiento
Para el ejemplo,el formato SQL es un diccionario como el siguiente:
```
{
            "id": 956061,
            "dispositivo_IoT": 12,
            "calidad": null,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0",
            "valor_float": 0.033198416,
            "valor_string": "",
            "pieza": null,
            "no_parte": "",
            "fecha_creacion": "2020-06-23T11:51:39.468637-05:00"
        },
```
Este debería mostrar un catalogo de variables por máquina de la siguiente manera:

```
{
    "maquina": 9,
    "variables": [
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai0",
            "limite": 1000,
            "consultaData": null
        },
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai1",
            "limite": 1000,
            "consultaData": null
        },
        {
            "nombre_variable": "corriente_test_case4_Mod4/ai0",
            "limite": 1000,
            "consultaData": null
        },
        {
            "nombre_variable": "corriente_test_case4_Mod4/ai1",
            "limite": 1000,
            "consultaData": null
        },
        {
            "nombre_variable": "acustico_test_case4_Mod2/ai0",
            "limite": 1000,
            "consultaData": null
        },
        {
            "nombre_variable": "acustico_test_case4_Mod2/ai1",
            "limite": 1000,
            "consultaData": null
        }
    ]
}
```
Dado que no requiere una estructuración especifica, no es necesario el consultaData.

## Caso 2: SQL con preprocesamiento sin ventanas
Este caso se da cuando se guardan datos preprocesados en SQL pero se ocupan más de un registro para obtener todos sus valores (ej. frecuencia y amplitud)
Para el ejemplo,el formato de los registros son de la siguiente manera:

### RMS
```
  {
            "id": 955974,
            "dispositivo_IoT": 12,
            "calidad": null,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0_RMS",
            "valor_float": 0.0323309273,
            "valor_string": "",
            "pieza": null,
            "no_parte": "",
            "fecha_creacion": "2020-06-23T11:50:59.128796-05:00"
        },
```
### FFT: Valor x (Frecuencia)
```
{
            "id": 955978,
            "dispositivo_IoT": 12,
            "calidad": null,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0_FFT_F",
            "valor_float": 0.0,
            "valor_string": "",
            "pieza": null,
            "no_parte": "",
            "fecha_creacion": "2020-06-23T11:50:59.128796-05:00"
        },
```
### FFT: Valor y (Amplitud)
```
  {
            "id": 955976,
            "dispositivo_IoT": 12,
            "calidad": null,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0_FFT_A",
            "valor_float": 0.00104486869,
            "valor_string": "",
            "pieza": null,
            "no_parte": "",
            "fecha_creacion": "2020-06-23T11:50:59.128796-05:00"
        },
```

Este debería mostrar un catalogo de variables por máquina de la siguiente manera:
```
{
    "maquina": 8,
    "variables": [
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai0",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai0_RMS": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_RMS",
                        "preprocesado": {
                            "ejex": "time",
                            "ejey": "RMS"
                        },
                        "valorx": [
                            "valorx"
                        ],
                        "valory": [
                            "valory"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "vibraciones_test_case4_Mod3/ai0_FFT_A": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": null,
                        "valory": [
                            "valory"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "vibraciones_test_case4_Mod3/ai0_FFT_F": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": [
                            "valory"
                        ],
                        "valory": null,
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        },
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai1",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai1_RMS": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1_PP_RMS",
                        "preprocesado": {
                            "ejex": "time",
                            "ejey": "RMS"
                        },
                        "valorx": [
                            "valorx"
                        ],
                        "valory": [
                            "valory"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "vibraciones_test_case4_Mod3/ai1_FFT_A": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1_PP_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": null,
                        "valory": [
                            "valory"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "vibraciones_test_case4_Mod3/ai1_FFT_F": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1_PP_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": [
                            "valory"
                        ],
                        "valory": null,
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        }
    ]
}
```

## Caso 3: SQL con preprocesamiento con ventanas
Este caso se da cuando se guardan datos preprocesados en SQL pero se ocupan más de un registro para obtener todos sus valores (ej. frecuencia y amplitud) y además se separó la muestra en diferentes ventanas, las cuales tienen una referencia.
Para el ejemplo,el formato de los registros son de la siguiente manera:

### RMS
```
        {
            "id": 955918,
            "dispositivo_IoT": 12,
            "calidad": null,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0",
            "valor_float": 6.35886159,
            "valor_string": "ventana0",
            "pieza": null,
            "no_parte": "",
            "fecha_creacion": "2020-06-23T11:50:49.528876-05:00"
        },
```
### FFT: Valor x (Frecuencia)
```
        {
            "id": 955932,
            "dispositivo_IoT": 12,
            "calidad": null,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0",
            "valor_float": 0.0,
            "valor_string": "ventana1_0_20",
            "pieza": null,
            "no_parte": "",
            "fecha_creacion": "2020-06-23T11:50:49.528876-05:00"
        },
```
### FFT: Valor y (Amplitud)
```
{
            "id": 955926,
            "dispositivo_IoT": 12,
            "calidad": null,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0",
            "valor_float": 40.3881064,
            "valor_string": "ventana1_0_20",
            "pieza": null,
            "no_parte": "",
            "fecha_creacion": "2020-06-23T11:50:49.528876-05:00"
        },
```

Este debería mostrar un catalogo de variables por máquina de la siguiente manera:
```
{
    "maquina": 7,
    "variables": [
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai0",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai0_RMS": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_V_RMS",
                        "preprocesado": {
                            "ejex": "time",
                            "ejey": "RMS"
                        },
                        "valorx": [
                            "valorx"
                        ],
                        "valory": [
                            "valory"
                        ],
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "vibraciones_test_case4_Mod3/ai0_FFT_A": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_V_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": null,
                        "valory": [
                            "valory"
                        ],
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "vibraciones_test_case4_Mod3/ai0_FFT_F": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_V_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": [
                            "valory"
                        ],
                        "valory": null,
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        },
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai1",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai1_RMS": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1_PP_V_RMS",
                        "preprocesado": {
                            "ejex": "time",
                            "ejey": "RMS"
                        },
                        "valorx": [
                            "valorx"
                        ],
                        "valory": [
                            "valory"
                        ],
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "vibraciones_test_case4_Mod3/ai1_FFT_A": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1_PP_V_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": null,
                        "valory": [
                            "valory"
                        ],
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "vibraciones_test_case4_Mod3/ai1_FFT_F": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1_PP_V_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": [
                            "valory"
                        ],
                        "valory": null,
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        },
        {
            "nombre_variable": "corriente_test_case4_Mod4/ai0",
            "limite": 100,
            "consultaData": {
                "corriente_test_case4_Mod4/ai0_RMS": [
                    {
                        "nombre_referencia": "corriente_test_case4_Mod4/ai0_PP_V_RMS",
                        "preprocesado": {
                            "ejex": "time",
                            "ejey": "RMS"
                        },
                        "valorx": [
                            "valorx"
                        ],
                        "valory": [
                            "valory"
                        ],
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "corriente_test_case4_Mod4/ai0_FFT_A": [
                    {
                        "nombre_referencia": "corriente_test_case4_Mod4/ai0_PP_V_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": null,
                        "valory": [
                            "valory"
                        ],
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ],
                "corriente_test_case4_Mod4/ai0_FFT_F": [
                    {
                        "nombre_referencia": "corriente_test_case4_Mod4/ai0_PP_V_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": [
                            "valory"
                        ],
                        "valory": null,
                        "referencia": [
                            "referencia"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        }
    ]
}
```

## Caso 4: no SQL sin preprocesamiento
Este caso se utiliza un JSON para guardar todos los datos.
Para el ejemplo, los registros tienen el siguiente formato:
```
{
            "id": 49118,
            "pieza": null,
            "no_parte": "",
            "dispositivo_IoT": 12,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0",
            "calidad": null,
            "valor": "{'valores': [-3.442321E-2, 5.004295E-3, -1.139755E-2, -1.619525E-3, 2.796355E-3, 3.427195E-3, 2.729950E-4, -5.492551E-2, -3.915451E-2, -3.578450E-4], 'fechas': ['2020-06-23T11:49:17.938645', '2020-06-23T11:49:17.948645', '2020-06-23T11:49:17.958645', '2020-06-23T11:49:17.968645', '2020-06-23T11:49:17.978645', '2020-06-23T11:49:17.988645', '2020-06-23T11:49:17.998645', '2020-06-23T11:49:18.008645', '2020-06-23T11:49:18.018645', '2020-06-23T11:49:18.028645']}",
            "fecha_creacion": "2020-06-23T11:49:17.938645-05:00"
        },
```

Este debería mostrar un catalogo de variables por máquina de la siguiente manera:
```
{
    "maquina": 10,
    "variables": [
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai0",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai0": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0",
                        "valorx": [
                            "valorx",
                            "fechas"
                        ],
                        "valory": [
                            "valorx",
                            "valores"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        },
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai1",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai1": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1",
                        "valorx": [
                            "valorx",
                            "fechas"
                        ],
                        "valory": [
                            "valorx",
                            "valores"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        },
    ]
}
```
## Caso 5: no SQL con preprocesamiento
Este caso se utiliza un JSON para guardar todos los datos.
Para el ejemplo, los registros tienen el siguiente formato:
```
{
            "id": 49088,
            "pieza": null,
            "no_parte": "",
            "dispositivo_IoT": 12,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0_PP",
            "calidad": null,
            "valor": "{'valor_RMS': 5.777531E-3, 'fecha': '2020-06-23T11:47:39.108719', 'valor_FFT_A': 1.179275E-5, 'valor_FFT_F': 1.000000E+1}",
            "fecha_creacion": "2020-06-23T11:47:39.108719-05:00"
        },
```
Este debería mostrar un catalogo de variables por máquina de la siguiente manera:
```
{
    "maquina": 11,
    "variables": [
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai0",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai0_PP": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_RMS",
                        "preprocesado": {
                            "ejex": "time",
                            "ejey": "RMS"
                        },
                        "valorx": [
                            "valorx",
                            "fecha"
                        ],
                        "valory": [
                            "valorx",
                            "valor_RMS"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    },
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": [
                            "valorx",
                            "valor_FFT_F"
                        ],
                        "valory": [
                            "valorx",
                            "valor_FFT_A"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        },
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai1",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai1_PP": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1_PP_RMS",
                        "preprocesado": {
                            "ejex": "time",
                            "ejey": "RMS"
                        },
                        "valorx": [
                            "valorx",
                            "fecha"
                        ],
                        "valory": [
                            "valorx",
                            "valor_RMS"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    },
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai1_PP_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": [
                            "valorx",
                            "valor_FFT_F"
                        ],
                        "valory": [
                            "valorx",
                            "valor_FFT_A"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        },
    ]
}
```
## Caso 6: no SQL con preprocesamiento con ventanas
Este caso se utiliza un JSON para guardar todos los datos.
Para el ejemplo, los registros tienen el siguiente formato:
```
{
            "id": 49073,
            "pieza": null,
            "no_parte": "",
            "dispositivo_IoT": 12,
            "nombre_sensor": "vibraciones_test_case4_Mod3/ai0_PP_V",
            "calidad": null,
            "valor": "{'valor_RMS': [3.309509E-2, 3.265927E-2, 3.233774E-2, 1.935400E-2], 'fecha': ['2020-06-23T11:45:29.158711', '2020-06-23T11:45:29.188711', '2020-06-23T11:45:29.218711', '2020-06-23T11:45:29.248711'], 'valor_FFT_A': [1.074372E-3, 1.548424E-7, 5.745440E-8], 'valor_FFT_F': [0.000000E+0, 3.000000E+1, 4.000000E+1], 'ventanas': ['ventana1_0_20', 'ventana2_20_40', 'ventana3_40_60']}",
            "fecha_creacion": "2020-06-23T11:45:29.158711-05:00"
        },
```
Este debería mostrar un catalogo de variables por máquina de la siguiente manera:
```
{
    "maquina": 12,
    "variables": [
        {
            "nombre_variable": "vibraciones_test_case4_Mod3/ai0",
            "limite": 100,
            "consultaData": {
                "vibraciones_test_case4_Mod3/ai0_PP_V": [
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_V_RMS",
                        "preprocesado": {
                            "ejex": "time",
                            "ejey": "RMS"
                        },
                        "valorx": [
                            "valorx",
                            "fecha"
                        ],
                        "valory": [
                            "valorx",
                            "valor_RMS"
                        ],
                        "referencia": null,
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    },
                    {
                        "nombre_referencia": "vibraciones_test_case4_Mod3/ai0_PP_V_FFT",
                        "preprocesado": {
                            "ejex": "Frequency",
                            "ejey": "Amplitude"
                        },
                        "valorx": [
                            "valorx",
                            "valor_FFT_F"
                        ],
                        "valory": [
                            "valorx",
                            "valor_FFT_A"
                        ],
                        "referencia": [
                            "valorx",
                            "ventanas"
                        ],
                        "fecha_ref": [
                            "fecha_ref"
                        ]
                    }
                ]
            }
        },
    ]
}
```
