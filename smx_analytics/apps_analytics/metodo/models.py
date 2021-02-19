from django.db import models
from apps_analytics.catalogo.models import catalogoPredictivo
from django.contrib.postgres.fields import JSONField

""" Modelo DE CATALOGO DE METODOS """


class metodoCatalogo(models.Model):
    
    PROCESAMIENTO = 1
    PREDICTIVO = 2

    TIPO_MET = (
        (PROCESAMIENTO, "PROCESAMIENTO"),
        (PREDICTIVO, "PREDICTIVO")
    )

    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    tipoMetodo = models.IntegerField(choices=TIPO_MET, default=0, null=False, blank=False)

    class Meta:
        db_table = 'metodoCatalogo'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo de metodo catalogo procesamiento """


class metodoCatalogoProc(models.Model):
    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    catalogo = models.ForeignKey(metodoCatalogo, on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        db_table = 'metodoCatalogoProc'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo de CATALOGO PROCESAMIENTO """


class metodoProcesamiento(models.Model):

    INDEPENDIENTE = 1
    DEPENDIENTE = 2

    TIPO_MET = (
        (INDEPENDIENTE, "INDEPENDIENTE"),
        (DEPENDIENTE, "DEPENDIENTE")
    )

    predictivo = models.ForeignKey(catalogoPredictivo, on_delete=models.CASCADE, null=False, blank=False)
    catalogoProc = models.ForeignKey(metodoCatalogoProc, on_delete=models.CASCADE, null=False, blank=False)
    jsonVar = JSONField()
    tipoVariable = models.IntegerField(choices=TIPO_MET, default=0, null=False, blank=False)



    class Meta:
        db_table = 'metodoProcesamiento'

