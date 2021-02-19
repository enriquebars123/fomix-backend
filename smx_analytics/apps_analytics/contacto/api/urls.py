""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_analytics.contacto.api.views import (
    contactoNotificacionViewSet,
    contactoDepartamentoViewSet,
    contactoPersonaViewSet,
)

router = routers.DefaultRouter()
router.register(r'^api/v1/contactoNotificacion', contactoNotificacionViewSet)
router.register(r'^api/v1/contactoDepartamento', contactoDepartamentoViewSet)
router.register(r'^api/v1/contactoPersona', contactoPersonaViewSet)


urlpatterns = router.urls
