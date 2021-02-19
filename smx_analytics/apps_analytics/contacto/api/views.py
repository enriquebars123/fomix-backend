""" view para catalogos """


# Django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


# serializers
from apps_analytics.contacto.api.serializers import (
    contactoNotificacionSerializers,
    contactoDepartamentoSerializers,
    contactoPersonaSerializers
)

# Modelo
from apps_analytics.contacto.models import (
    contactoNotificacion,
    contactoDepartamento,
    contactoPersona
)

# Utileria
from smx_analytics.utilerias import GeneralViewSetMixin


""" viewSet menu """


class contactoNotificacionViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = contactoNotificacion.objects.all()
    serializer_class = contactoNotificacionSerializers

    
class contactoDepartamentoViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = contactoDepartamento.objects.all()
    serializer_class = contactoDepartamentoSerializers

class contactoPersonaViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = contactoPersona.objects.all()
    serializer_class = contactoPersonaSerializers

