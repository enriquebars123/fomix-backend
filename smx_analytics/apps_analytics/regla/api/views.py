""" view para metodo """


# Django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# serializer 
from  apps_analytics.regla.api.serializers import reglaSerializers


# Modelo
from apps_analytics.regla.models import regla

# Utileria
from smx_analytics.utilerias import GeneralViewSetMixin


""" viewSet de reglas de componentes """


class reglaViewSet(GeneralViewSetMixin, ModelViewSet):
    #filter_fields = ['componente',]
    #filter_backends = [DjangoFilterBackend,]
    queryset = regla.objects.all()
    serializer_class = reglaSerializers

