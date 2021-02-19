FROM python:3.7

# COPIANDO ARCHIVOS.
RUN mkdir -p /django_app
WORKDIR /django_app
COPY . .
RUN pip install -r requirements.txt

#Realizar migraciones
#RUN python3 manage.py makemigrations --noinput; exit 0
#RUN python3 manage.py migrate --noinput; exit 0

# MIGRACIONES

# CONFIUGURANDO USARIO Y CONTRASENA POR DEFECTO (ADMIN)

# CARGAR DATOS DE BACKUP

#CMD ${EJECUTAR}
