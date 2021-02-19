""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_analytics.catalogo.api.views import (
    perfilViewSet,
    menuViewSet,
    fuenteDatosViewSet,
    predictivoViewSet,
    componenteViewSet,
    VariableViewSet,
    simbologiaViewSet,
)

router = routers.DefaultRouter()
router.register(r'^api/v1/perfil', perfilViewSet)
router.register(r'^api/v1/menu', menuViewSet)
router.register(r'^api/v1/fuenteDatos', fuenteDatosViewSet)
router.register(r'^api/v1/predictivo', predictivoViewSet)
router.register(r'^api/v1/componente', componenteViewSet)
router.register(r'^api/v1/catalogoVarDependiente', VariableViewSet)
router.register(r'^api/v1/simbologia', simbologiaViewSet )

urlpatterns = router.urls
