from django.db import models
from apps_analytics.catalogo.models import catalogoComponente

# Modelos 
from apps_user.smxAnalitica_user.models import user

       
""" Modelo grupo de contactos """


class contactoDepartamento(models.Model):
    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    #persona = models.ManyToManyField(contactoPersona)
    #notificacion = models.ManyToManyField(contactoNotificacion)
    

    class Meta:
        db_table = 'contactoDepartamento'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class contactoPersona(models.Model):
    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    correo = models.EmailField(max_length=250, unique=True, null=False, blank=False)
    ext = models.CharField(max_length=5,null=False, blank=False)
    departamento = models.ForeignKey(contactoDepartamento, on_delete=models.CASCADE, null=False, blank=False )

    class Meta:
        db_table = 'contactoPersona'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo catalogo de contactos"""


class contactoNotificacion(models.Model):
    ENPROCESO = 1
    TIEMPO = 2

    TIPO_EJECUCION = (
        (ENPROCESO, "PIEZA PREDICCION"),
        (TIEMPO, "TIEMPO")
    )

    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    departamento = models.ManyToManyField(contactoDepartamento)
    tipoEjecucion = models.IntegerField(choices=TIPO_EJECUCION, default=0, null=False, blank=False)

    class Meta:
        db_table = 'contactoNotificacion'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre