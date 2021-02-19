""" view para metodo """


# Django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# serializers
from apps_analytics.metodo.api.serializers import (
    metodoCatalogoSerializers,
    metodoCatalogoProcSerializers,
    metodoProcSerializers
)

# Modelo
from apps_analytics.metodo.models import (
    metodoCatalogo,
    metodoCatalogoProc,
    metodoProcesamiento,
)

# Utileria
from smx_analytics.utilerias import GeneralViewSetMixin


""" viewSet metodo de catalogo """


class metodoCatalogoViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['tipoMetodo',]
    filter_backends = [DjangoFilterBackend,]
    queryset = metodoCatalogo.objects.all()
    serializer_class = metodoCatalogoSerializers


class metodoCatalogoProcViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = metodoCatalogoProc.objects.all()
    serializer_class = metodoCatalogoProcSerializers


class metodoProcViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['predictivo','catalogoProc','tipoVariable']
    filter_backends = [DjangoFilterBackend,]
    queryset = metodoProcesamiento.objects.all()
    serializer_class = metodoProcSerializers

