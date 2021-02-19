# Django
from django.db import models

from django.contrib.postgres.fields import JSONField
from decouple import config

from django.utils import timezone


""" Modelo de CATALOGOO PERFIL """


class catalogoPerfil(models.Model):
    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'catalogoPerfil'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo de CATALOGOO PERFIL """


class catalogoMenu(models.Model):
    nombre = models.CharField(max_length=250, null=False, blank=False)
    nivel = models.IntegerField(default=1)
    parent = models.IntegerField(default=1)
    icon = models.CharField(max_length=50, null=True, blank= True)
    url = models.CharField(max_length=250, null=True, blank= True)
    orden = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = 'catalogoMenu'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre

    def regresaName(self):
        return 'catalogoMenu'

""" Modelo de CATALOGO COMPONENTE """


class catalogoComponente(models.Model):
    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='uploads/componente')
    nomDibujo = models.CharField(max_length=100)
    noParte = models.CharField(max_length=20)
    info = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'catalogoComponente'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo de CATALOGO PREDICTIVO """


class catalogoPredictivo(models.Model):
    PRUEBA = 1
    PRODUCCION = 2
    ENTRENAMIENTO = 3
    
    TIPO_STATUS = (
        (PRUEBA, "A prueba"),
        (PRODUCCION, "En produccion"),
        (ENTRENAMIENTO, "En entrenamiento"),
    )

    nombre = models.CharField(max_length=250,unique=True, null=False, blank=False)
    descripcion = models.TextField()
    certeza = models.FloatField(null=True, blank=True)
    status = models.IntegerField(choices=TIPO_STATUS , default=0,null=True, blank=True)
    
    class Meta:
        db_table = 'catalogoPredictivo'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


""" Modelo de CATALOGO FUENTE DATOS """


class catalogoFuenteDatos(models.Model):
    INDEPENDIENTE = 1
    DEPENDIENTE = 2
    CONSULTA = 3
    
    TIPO_MET = (
        (INDEPENDIENTE, "INDEPENDIENTE"),
        (DEPENDIENTE, "DEPENDIENTE"),
        (CONSULTA, "CONSULTA"),
    )

    MES = 1
    QDA = 2
    TIPO_CONS = (
        (MES, "CONSULTA MES"),
        (QDA, "CONSULTA QDA")

    )

    nombre = models.CharField(max_length=250, unique=True, null=False, blank=False)
    urlRegistro = models.CharField(max_length=250)
    urlCatalogo = models.CharField(max_length=250)
    urlValComRel = models.CharField(max_length=250, null=True, blank=True)
    #ralacionMaquina = models.CharField(max_length=50)
    usuario = models.CharField(max_length=150, null=True, blank=True)
    contrasena = models.CharField(max_length=150, null=True, blank=True)
    paginacion = models.BooleanField(default=True)
    filtro = JSONField()
    estructura = JSONField(null=True, blank=True)
    tipoFuente = models.IntegerField(choices=TIPO_MET, default=0, null=False, blank=False)
    tipoConsulta = models.IntegerField(choices=TIPO_CONS , default=0,null=True, blank=True)
    dateEnd = models.DateTimeField(default=timezone.now, null=False, blank=False)

    class Meta:
        db_table = 'catalogoFuenteDatos'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class catalogoSimbologia(models.Model):
    nombre = models.CharField(max_length=20, unique=True, null=False, blank=False)
    icon = models.ImageField(upload_to='uploads/simbologia')

    class Meta:
        db_table = 'catalogoSimbologia'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class catalogoVariable(models.Model):
    componente = models.ForeignKey(catalogoComponente, on_delete=models.CASCADE, null=False, blank=False)
    #simbologia = models.OneToOneField(catalogoSimbologia, on_delete=models.CASCADE, primary_key=False)
    simbologia = models.ForeignKey(catalogoSimbologia, on_delete=models.CASCADE, null=False, blank=False )
    nombre = models.CharField(max_length=250, null=False, blank=False)
    nominal = models.FloatField()
    usl = models.FloatField()
    lsl = models.FloatField()
    ucl = models.FloatField()
    lcl = models.FloatField()

    class Meta:
        db_table = 'catalogoVariable'

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


