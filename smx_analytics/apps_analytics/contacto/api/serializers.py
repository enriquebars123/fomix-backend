"""contacto serializers."""


# Django Rest Framework
from rest_framework import serializers
from apps_user.smxAnalitica_user.models import user
from apps_analytics.contacto.models import (
    contactoNotificacion,
    contactoDepartamento,
    contactoPersona,
)


class contactoNotificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = contactoNotificacion
        fields = (
           'id',
           'nombre',
           'departamento',
           'tipoEjecucion'
        )

class contactoDepartamentoSerializers(serializers.ModelSerializer):
    #users = serializers.PrimaryKeyRelatedField(queryset=user.objects.all(), many=True)
    class Meta:
        model = contactoDepartamento
        fields = (
           'id',
           'nombre',
        )

class contactoPersonaSerializers(serializers.ModelSerializer):

    class Meta: 
        model = contactoPersona
        fields = (
            'id',
            'nombre',
            'correo',
            'ext',
            'departamento',
            
        )