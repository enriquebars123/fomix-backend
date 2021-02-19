""" view para catalogos """


# Django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


# serializers
from apps_analytics.catalogo.api.serializers import (
    MenuSerializers,
    PerfilSerializers,
    ComponenteSerializers,
    PredictivoSerializers,
    FuenteDatosSerializers,
    VariableSerializers,
    SimbologiaSerializers,
)
from django_filters.rest_framework import DjangoFilterBackend

# Modelo
from apps_analytics.catalogo.models import (
    catalogoMenu,
    catalogoPerfil,
    catalogoComponente,
    catalogoPredictivo,
    catalogoFuenteDatos,
    catalogoVariable,
    catalogoSimbologia,
)

# Utileria
from smx_analytics.utilerias import GeneralViewSetMixin


""" viewSet menu """


class menuViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = catalogoMenu.objects.all()
    serializer_class = MenuSerializers


""" viewSet perfil """


class perfilViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = catalogoPerfil.objects.all()
    serializer_class = PerfilSerializers


""" viewSet COMPONENTE """


class componenteViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = catalogoComponente.objects.all()
    serializer_class = ComponenteSerializers
    


""" viewSet PREDICTIVOS """


class predictivoViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = '__all__'
    filter_backends = [DjangoFilterBackend,]
    queryset = catalogoPredictivo.objects.all()
    serializer_class = PredictivoSerializers


""" viewSet FUENTE DE DATOS """


class fuenteDatosViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = catalogoFuenteDatos.objects.all()
    serializer_class = FuenteDatosSerializers
    filter_fields = ['tipoFuente',]
    filter_backends = [DjangoFilterBackend,]


class simbologiaViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = catalogoSimbologia.objects.all()
    serializer_class = SimbologiaSerializers


class VariableViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = catalogoVariable.objects.all()
    serializer_class = VariableSerializers
