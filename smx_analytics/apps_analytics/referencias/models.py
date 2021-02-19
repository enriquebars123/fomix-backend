# Django
from django.db import models
from apps_analytics.catalogo.models import (
    catalogoComponente,
)



""" Modelo de referencia empresa """


class referenciaEmpresa(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        db_table = 'referenciaEmpresa'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo de referencia planta """


class referenciaPlanta(models.Model):
    empresa = models.ForeignKey(referenciaEmpresa, on_delete=models.PROTECT, null=False, blank=False)
    nombre = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'referenciaPlanta'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo de referencia linea """


class referenciaLinea(models.Model):
    planta = models.ForeignKey(referenciaPlanta, on_delete=models.PROTECT, null=False, blank=False)
    nombre = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'referenciaLinea'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo de referencia maquina """


class referenciaMaquina(models.Model):
    linea = models.ForeignKey(referenciaLinea, on_delete=models.CASCADE, null=False, blank=False)
    nombre = models.CharField(max_length=250, null=True, blank=True)
    imagen = models.ImageField(upload_to='uploads/maquina')
    componente = models.ManyToManyField(catalogoComponente)
    
    class Meta:
        db_table = 'referenciaMaquina'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class referenciaDmcCiclo(models.Model):
    maquina = models.ForeignKey(referenciaMaquina, on_delete=models.CASCADE, null=False, blank=False)
    dmc = models.CharField(max_length=50, null=False, blank=False)
    componente = models.CharField(max_length=50, null=True, blank=True)
    fechaIni = models.DateTimeField()
    fechaFin = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'referenciaDmcCiclo'

    def __str__(self):
        return self.dmc

    def __unicode__(self):
        return self.dmc