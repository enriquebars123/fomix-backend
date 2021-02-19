"""Usuario serializers."""


# Django Rest Framework
from rest_framework import serializers
from apps_analytics.relacion.models import (
   relacionPerfilMenu,
   relacionUserPerfil,
   relacionCompPredictivo,
   relacionPredFuenteDatos,
   relacionMaqFuenteDatos,
   relacionCompPredictivoResult,
)


class PerfilMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = relacionPerfilMenu
        fields = (
            'id',
            'perfil',
            'menu',
            'isActive'
        )


class UserPerfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = relacionUserPerfil
        fields = (
            'id',
            'user',
            'perfil',
        )


class CompPredictivoSerializers(serializers.ModelSerializer):
    class Meta:
        model = relacionCompPredictivo
        fields = (
            'id',
            'componentes',
            'predictivo',
            'maquina',
        )


class PredFuenteDatosSerializers(serializers.ModelSerializer):
    maquina = serializers.IntegerField(write_only=True,required=False)

    class Meta:
        model = relacionPredFuenteDatos
        fields = (
            'id',
            'fuenteDatos',
            'predictivo',
            'maquina',
        )


class MaqFuenteDatoSerializers(serializers.ModelSerializer):
    class Meta:
        model = relacionMaqFuenteDatos
        fields = (
            'id',
            'maquina',
            'fuenteDatos',
            'referenciaId',
            'descripcion',
        )

class CompPredictivoResultSerializers(serializers.ModelSerializer):
    fecha = serializers.DateTimeField(format= '%Y-%m-%dT%H:%M:%S.%f')
    class Meta:
        model = relacionCompPredictivoResult
        fields = (
            'id',
            'compPredictivo',
            'jsonPrediccion',
            'fecha',
            'codigoPieza',
            'estatus'
        )
