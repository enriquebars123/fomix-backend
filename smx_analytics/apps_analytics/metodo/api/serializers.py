"""metodo catalogo serializers"""


# Django Rest Framework
from rest_framework import serializers
from apps_analytics.metodo.models import (
    metodoCatalogo,
    metodoCatalogoProc,
    metodoProcesamiento
)


class metodoCatalogoSerializers(serializers.ModelSerializer):
    class Meta:
        model = metodoCatalogo
        fields = (
            'id',
            'nombre',
            'tipoMetodo',
        )


class metodoCatalogoProcSerializers(serializers.ModelSerializer):
    class Meta:
        model = metodoCatalogoProc
        fields = (
            'id',
            'nombre',
            'catalogo',
        )


class metodoProcSerializers(serializers.ModelSerializer):
    class Meta:
        model = metodoProcesamiento
        fields = (
            'id',
            'predictivo',
            'catalogoProc',
            'jsonVar',
            'tipoVariable',
        )


