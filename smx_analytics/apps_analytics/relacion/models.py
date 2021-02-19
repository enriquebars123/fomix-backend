# Django
from django.db import models

# Modelos
from apps_user.smxAnalitica_user.models import user
from apps_analytics.catalogo.models import (
    catalogoPerfil,
    catalogoMenu,
    catalogoComponente,
    catalogoPredictivo,
    catalogoFuenteDatos,
)
from django.contrib.postgres.fields import JSONField
from apps_analytics.referencias.models import referenciaMaquina
from django.utils               import timezone
from datetime import datetime 
import pytz
""" Modelo de PERFIL - SUBMENU"""


class relacionPerfilMenu(models.Model):
    perfil = models.ForeignKey(catalogoPerfil, on_delete=models.CASCADE, null=False, blank=False)
    menu = models.ForeignKey(catalogoMenu, on_delete=models.CASCADE, null=False, blank=False)
    isActive = models.BooleanField(default=True, null=False, blank=False)

    class Meta:
        db_table = 'relacionPerfilMenu'


""" Modelo de USUARIO - PERFIL"""


class relacionUserPerfil(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=False, blank=False)
    perfil = models.ForeignKey(catalogoPerfil, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'relacionUserPerfil'


""" Modelo de COMPONENTE PREDICTIVO"""


class relacionCompPredictivo(models.Model):
    componentes = models.ForeignKey(catalogoComponente, on_delete = models.CASCADE, null=False, blank=False)
    predictivo = models.ForeignKey(catalogoPredictivo, on_delete = models.CASCADE, null=False, blank=False)
    maquina = models.ForeignKey(referenciaMaquina, on_delete= models.CASCADE, null=False, blank=False)


    class Meta:
        db_table = 'relacionCompPredictivo'


""" Modelo de PREDICTIVO - FUENTE DATOS"""


class relacionPredFuenteDatos(models.Model):
    fuenteDatos = models.ForeignKey(catalogoFuenteDatos, on_delete=models.CASCADE, null=False, blank=False )
    predictivo = models.ForeignKey(catalogoPredictivo, on_delete=models.CASCADE, null=False, blank=False )

    class Meta:
        db_table = 'relacionPredFuenteDatos'


class relacionMaqFuenteDatos(models.Model):
    maquina = models.ForeignKey(referenciaMaquina, on_delete=models.PROTECT, null=False, blank=False)
    fuenteDatos = models.ForeignKey(catalogoFuenteDatos, on_delete= models.PROTECT, null= False, blank=False)
    referenciaId = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=50,)
    
    class Meta:
        db_table = 'relacionMaqFuenteDatos'

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


class relacionCompPredictivoResult(models.Model):
    compPredictivo = models.ForeignKey(relacionCompPredictivo, on_delete=models.PROTECT, null=False, blank=False)
    jsonPrediccion = JSONField()
    fecha = models.DateTimeField(default=datetime.now())
    codigoPieza = models.CharField(max_length=100)
    estatus = models.CharField(max_length=5)
    
    class Meta:
        db_table : 'relacionCompPredictivoResult'

    def __str__(self):
        return self.codigoPieza

    def __unicode__(self):
        return self.codigoPieza

class relacionMaqFuenteDatosVarInd(models.Model):
    maqFuenteDato = models.ForeignKey(relacionMaqFuenteDatos, on_delete=models.CASCADE, null=False, blank=False)
    nombre = models.CharField(max_length=250, null=False, blank=False)

    class Meta:
        db_table = 'relacionMaqFuenteDatosVarInd'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre