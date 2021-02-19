""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_analytics.referencias.api.views import (
    refEmpresaViewSet,
    refPlantaViewSet,
    refLineaViewSet,
    refMaquinaViewSet,
    refDmcCicloViewSet
)
from apps_analytics.referencias import views

router = routers.DefaultRouter()
router.register(r'^api/v1/refEmpresa', refEmpresaViewSet)
router.register(r'^api/v1/refPlanta', refPlantaViewSet)
router.register(r'^api/v1/refLinea', refLineaViewSet)
router.register(r'^api/v1/refMaquina', refMaquinaViewSet)
router.register(r'^api/v1/refDmcCiclo', refDmcCicloViewSet)

urlpatterns = router.urls
