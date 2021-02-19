"""metodo catalogo serializers"""


# Django Rest Framework
from rest_framework import serializers
from apps_analytics.regla.models import regla 


class reglaSerializers(serializers.ModelSerializer):
    class Meta:
        model = regla
        fields = (
            'id',
            'variable',
            'nominal',
            'usl',
            'lsl',
            'ucl',
            'lcl',
            'estatus',
        )
