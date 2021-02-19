"""Usuario serializers."""


# Django Rest Framework
from rest_framework import serializers
from apps_analytics.variables.models import (
    variables
)


class VariableSerializers(serializers.ModelSerializer):
    class Meta:
        model = variables
        fields = (
           'fuenteDato',
           'componente',
           'maquina',
           'id',
           'nombre',
           'componente',
           'fuenteDato',
           'variable',
           'variableRef',
           'tipoDato',
           'tipoVarible',
           'isActive'
        )
