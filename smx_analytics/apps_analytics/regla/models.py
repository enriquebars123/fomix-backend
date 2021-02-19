from django.db import models
from apps_analytics.contacto.models import *
from apps_analytics.catalogo.models import (
    catalogoVariable
)

""" Modelo reglas """


class regla(models.Model):

    #nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    #departamento = models.ForeignKey(contactoDepartamento, on_delete=models.CASCADE, null=False, blank=False)
    #notificacion = models.ForeignKey(contactoNotificacion, on_delete=models.CASCADE, null=False, blank=False)
    variable = models.ForeignKey(catalogoVariable, on_delete=models.CASCADE, null=False, blank=False )
    nominal = models.FloatField()
    usl = models.FloatField()
    lsl = models.FloatField()
    ucl = models.FloatField()
    lcl = models.FloatField()
    estatus = models.BooleanField()
    
    class Meta:
        db_table = 'regla'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

