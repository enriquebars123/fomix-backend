""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_analytics.relacion.api.views import (
    PerfilMenuViewSet,
    UserPerfilViewSet,
    CompPredictivoViewSet,
    PredFuenteDatosViewSet,
    MaqFuenteDatosViewSet,
    CompPredictivoResultViewSet,
)

router = routers.DefaultRouter()
router.register(r'^api/v1/perfilMenu', PerfilMenuViewSet)
router.register(r'^api/v1/userPerfil', UserPerfilViewSet)
router.register(r'^api/v1/comPredictivo', CompPredictivoViewSet)
router.register(r'^api/v1/predFuenteDatos', PredFuenteDatosViewSet)
router.register(r'^api/v1/MaqFuenteDatos', MaqFuenteDatosViewSet)
router.register(r'^api/v1/CompPredictivoResult',CompPredictivoResultViewSet)

urlpatterns = router.urls
