""" Views de variables"""


# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


# serializer
from apps_analytics.variables.api.serializers import (
    VariableSerializers
)

# Models
from apps_analytics.variables.models import (
    variables
)

# Utilerias
from smx_analytics.utilerias import GeneralViewSetMixin


class VariablesViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = variables.objects.all()
    serializer_class = VariableSerializers
