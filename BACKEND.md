# BACKEND DE LA APLICACIÓN DE IMPACTO-ANALYTICS: Plataforma Predictiva de Sisamex (FOMIX)
# Version V1.0

DESCRIPCIÓN: En este apartado se muestra la arquitectura del backend
Integración
![conexion_hxh_200px](documentación/conexion_hxh.png)


## Funcionalidades disponibles por versiones.

| Funciones                                     | v1.0  |
| :---                                          | :---: |
| Maquetado del Backend                         | D     |

OK: Funcionalidad incorporada.
X : Funcionalidad eliminada.
D : Funcionalidad en desarrollo.
P : Previsto a desarrollar


## 1.0 App Usuario.

Los datos requeridos por cada usuario son los siguientes:

![conexion_hxh_300px](documentación/backend/tabla_v1_user.png)

### Descripción de veriables:
#### user              : Nombre del usuario (string)
#### email             : Dirección de correo electrónico del usuario: (email,unic=True)
#### tipo_de_usuario   : Nivel de acceso del usuario.
#### Versiones piloto  : Mostrar versiones no estables
#### Notificar         : Enviar Notificaciones al usuario.


## 1.0 App Referencia.
En esta Apps se encuentran las tablas para referencias a las máquinas Herramientas.
![conexion_hxh_300px](documentación/backend/tabla_v2_referencia.png)



# HERRAMIENTAS DE EDICIÓN.
Para editar los diagramas emplar [https://inkscape.org/es/release/inkscape-0.92.3/]


# Comandos para construir servidor en el localhost:

## Construir bases de datos:

```
# proyecto/
docker-compose -f build.yml up -d postgres

# Construir Redis.
docker-compose -f build.yml up -d redis

# Construir FLOWER

docker-compose -f build.yml up -d flower

```

## Cambiar archivo .env

```
# LOCAL LOCALHOST (Windows).
DB_URL       = "postgres://postgres:galileo.1564@10.0.75.1:65432/db_analytics"
DB_URL_REDIS = "postgres://postgres:galileo.1564@10.0.75.1:6379/db_analytics"
```

## Construir Django.

### Opción A) Ir al directorio y ejecutar directamente backend de django.

### Opción B) Usar un contenedor docker.

Cambio de variable .env
```
# DOCKER IMAGEN .
DB_URL       = "postgres://postgres:galileo.1564@sas_pg:5432/db_analytics"
DB_URL_REDIS = "postgres://postgres:galileo.1564@redis:6379/db_analytics"

```

Construir imagen.

```
docker-compose -f build.yml up -d django
```
Hacer migraciones

```
docker-compose -f build.yml run django python manage.py migrate

```

## Comandos útiles.
Entrar de forma interactiva al contedor.
```
docker exec -it sas_dj bash
```

## Montar servicios Celery

```
docker-compose -f build.yml up -d celery_beat
docker-compose -f build.yml up -d celery_worker
```
