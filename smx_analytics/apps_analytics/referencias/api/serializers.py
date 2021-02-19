# Django Rest Framework
from rest_framework import serializers
import sys
import json
# Models
from apps_analytics.referencias.models import (
    referenciaEmpresa,
    referenciaPlanta,
    referenciaLinea,
    referenciaMaquina,
    referenciaDmcCiclo,
)
from apps_analytics.catalogo.api.serializers import (
    ComponenteSerializers,
    ComponenteImgFormatSerializers
    ) 

""" serializer de REFERENCIA EMPRESA """


class RefEmpresaSerializers(serializers.ModelSerializer):
    class Meta:
        model = referenciaEmpresa
        fields = (
            'id',
            'nombre',
        )


"""Serializers de REFERENCIA PLANTA"""


class RefPlantaSerializers(serializers.ModelSerializer):
    class Meta:
        model = referenciaPlanta
        fields = (
            'id',
            'empresa',
            'nombre',
        )


"""Serializer de REFERENCIA LINEA """


class RefLineaSerializers(serializers.ModelSerializer):
    class Meta:
        model = referenciaLinea
        fields = (
            'id',
            'planta',
            'nombre',
        )


"""Serializer de REFERENCIA MAQUINA """

"""
    serializers con hijos "componentes"
"""


class RefMaquinaSerializers(serializers.ModelSerializer):
    #componente = ComponenteSerializers(many=True, read_only = True)
    imagen = serializers.ImageField(write_only=False,required=False)
    #imagen = serializers.SerializerMethodField()
    #linea = serializers.CharField(write_only=False,required=False)
    class Meta:
        model = referenciaMaquina
        fields = (
            'id',
            'linea',
            'nombre',
            'imagen',
            'componente',
        )

  
class CURefMaquinaSerializers(serializers.ModelSerializer):

    componente = ComponenteImgFormatSerializers(many=True, read_only = True)
    #imagen = serializers.ImageField(write_only=False,required=False)
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = referenciaMaquina
        fields = (
            'id',
            'linea',
            'imagen',
            'nombre',
            'componente',
        )
    
    def get_imagen(self, obj):   
        request = self.context.get('request')
        photo_url =  obj.imagen.url
        
        return photo_url  
    
    """
        serializers sin hijos "componentes"
    """
class RefMaquinaPredSerializers(serializers.ModelSerializer):
    imagen = serializers.ImageField(write_only=False,required=False)
    class Meta:
        model = referenciaMaquina
        fields = (
            'id',
            'linea',
            'nombre',
            'imagen',
        )


class RefDmcCicloSerializers(serializers.ModelSerializer):

    class Meta:
        model = referenciaDmcCiclo
        fields = (
            'id',
            'maquina',
            'dmc',
            'componente',
            'fechaIni',
            'fechaFin',
        )
