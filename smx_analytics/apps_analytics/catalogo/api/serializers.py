"""Usuario serializers."""


# Django Rest Framework
from rest_framework import serializers
from apps_analytics.catalogo.models import (
    catalogoPerfil,
    catalogoMenu,
    catalogoComponente,
    catalogoPredictivo,
    catalogoFuenteDatos,
    catalogoVariable,
    catalogoSimbologia,
)
from rest_framework.fields import ChoiceField

class PerfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = catalogoPerfil
        fields = (
           'id',
           'nombre',
        )


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = catalogoMenu
        fields = (
           'id',
           'nombre',
           'nivel',
           'parent',
           'icon',
           'url',
           'orden',
        )


class ComponenteImgFormatSerializers(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = catalogoComponente
        fields = (
           'id',
           'nombre',
           'descripcion',
           'imagen',
           'nomDibujo',
           'noParte',
           'info'
        )
    
    def get_imagen(self, obj):   
        request = self.context.get('request')
        photo_url =  obj.imagen.url
        return photo_url   

class ComponenteSerializers(serializers.ModelSerializer):
    imagen = serializers.ImageField(write_only=False,required=False)

    class Meta:
        model = catalogoComponente
        fields = (
           'id',
           'nombre',
           'descripcion',
           'imagen',
           'nomDibujo',
           'noParte',
           'info'
        )


class PredictivoSerializers(serializers.ModelSerializer):
    class Meta:
        model = catalogoPredictivo
        fields = (
           'id',
           'nombre',
           'descripcion',
           'certeza',
           'status'
        )


class FuenteDatosSerializers(serializers.ModelSerializer):
    #tipoConsulta = serializers.IntegerField(read_only=True,required=False)
    class Meta:
        model = catalogoFuenteDatos
        fields = (
            'id',
            'nombre',
            'urlRegistro',
            'urlCatalogo',
            'urlValComRel',
            'usuario',
            'contrasena',
            'paginacion', 
            'filtro',
            'estructura',
            'tipoFuente',
            'tipoConsulta',
            'dateEnd'
        )
        

class VariableSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = catalogoVariable
        fields = ( 
            'id',
            'componente',
            'simbologia',
            'nombre',
            'nominal',
            'usl',
            'lsl',
            'ucl',
            'lcl',
        )



class SimbologiaSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = catalogoSimbologia
        fields = (
            'id',
            'nombre',
            'icon',
        )