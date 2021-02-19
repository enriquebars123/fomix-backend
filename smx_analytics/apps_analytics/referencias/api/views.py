""" view para referencia """


# Django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework import status
from django.db.models.deletion import ProtectedError

# serialisers
from apps_analytics.referencias.api.serializers import (
    RefEmpresaSerializers,
    RefPlantaSerializers,
    RefLineaSerializers,
    RefMaquinaSerializers,
    CURefMaquinaSerializers, 
    RefDmcCicloSerializers,
)
import json
# Models
from apps_analytics.referencias.models import (
    referenciaEmpresa,
    referenciaPlanta,
    referenciaLinea,
    referenciaMaquina,
    referenciaDmcCiclo,
)

# Utileria
from smx_analytics.utilerias import GeneralViewSetMixin


# view REFERECIA_EMPRESA
class refEmpresaViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['nombre',]
    filter_backends = [DjangoFilterBackend,]
    queryset = referenciaEmpresa.objects.all()
    serializer_class = RefEmpresaSerializers


# view REFERECIA_PLANTA
class refPlantaViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['empresa','nombre',]
    filter_backends = [DjangoFilterBackend,]
    queryset = referenciaPlanta.objects.all()
    serializer_class = RefPlantaSerializers


# view REFERECIA_LINEA
class refLineaViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['planta','nombre',]
    filter_backends = [DjangoFilterBackend,]
    queryset = referenciaLinea.objects.all()
    serializer_class = RefLineaSerializers

  
   



# view REFERECIA_MAQUINA
class refMaquinaViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['linea','nombre',]
    filter_backends = [DjangoFilterBackend,]
    queryset = referenciaMaquina.objects.all()
    #serializer_class = RefMaquinaSerializers
    serializer_classes = {
        'list': CURefMaquinaSerializers
    }

    default_serializer_class = RefMaquinaSerializers 
    #serializer_class = assignedUserSerializers
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,  self.default_serializer_class)
      

    """
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CURefMaquinaSerializers(queryset, many=True)
        return Response(serializer.data)
    """
    def retrieve(self, request, pk):
        instancia = self.get_object()
        serializer = CURefMaquinaSerializers(instancia)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        instancia = self.get_object()
        mhttp_status = None
        respuesta = None
        serializer = self.get_serializer(instancia, data=request.data,)
        if serializer.is_valid():
            mhttp_status = status.HTTP_202_ACCEPTED
            self.perform_update(serializer)
            instancia = self.get_object()
            serializer = CURefMaquinaSerializers(instancia)

            respuesta = {
                'success': True,
                'msg': 'Registro Actualizado',
                'data': serializer.data
            }
        else:
            mhttp_status = status.HTTP_400_BAD_REQUEST
            respuesta = {
                'success': False,
                'msg': '%s' % serializer.errors
            }
        return Response(respuesta, mhttp_status)


# view REFERECIA_DMC_CICLO

class dmCicloFilter(django_filters.FilterSet):
    fechaIni = django_filters.DateFromToRangeFilter()
    fechaFin = django_filters.DateFromToRangeFilter()
    class Meta:
        model = referenciaDmcCiclo
        fields = {
            'dmc': ['exact'],
            'maquina': ['exact'],
            'componente':['exact'],
        }

class refDmcCicloViewSet(GeneralViewSetMixin, ModelViewSet):
    #filter_fields = ['dmc','maquina','componente', 'fechaIni','fechaFin' ]
    filter_backends = [DjangoFilterBackend,]
    filter_class = dmCicloFilter
    queryset = referenciaDmcCiclo.objects.all()
    serializer_class = RefDmcCicloSerializers