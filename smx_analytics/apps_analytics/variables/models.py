# Django
from django.db import models

# modelos

from apps_analytics.referencias.models import referenciaMaquina
from apps_analytics.catalogo.models import catalogoComponente
from apps_analytics.catalogo.models import catalogoFuenteDatos

""" Modelo de referencia empresa """


class variables(models.Model):
    fuenteDato = models.ForeignKey(catalogoFuenteDatos, on_delete=models.PROTECT, null=False, blank=False)
    componente = models.ForeignKey(catalogoComponente, on_delete=models.PROTECT, null=False, blank=False)
    maquina = models.ForeignKey(referenciaMaquina, on_delete=models.PROTECT, null=False, blank=False)
    nombre = models.CharField(max_length=250, null=False)
    componente = models.CharField(max_length=250, null=True, blank=True)
    fuenteDato = models.CharField(max_length=250, null=True, blank=True)
    variable = models.CharField(max_length=250, null=True, blank=True)
    variableRef = models.CharField(max_length=250, null=True, blank=True)
    tipoDato = models.CharField(max_length=250, null=True, blank=True)
    tipoVarible = models.CharField(max_length=250, null=True, blank=True)
    isActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'variables'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
