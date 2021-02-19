""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_analytics.metodo.api.views import (
    metodoCatalogoViewSet,
    metodoCatalogoProcViewSet,
    metodoProcViewSet,

)

router = routers.DefaultRouter()
router.register(r'^api/v1/metodoCatalogo', metodoCatalogoViewSet)
router.register(r'^api/v1/metodoCatalogoProc', metodoCatalogoProcViewSet)
router.register(r'^api/v1/metodoProc', metodoProcViewSet)


urlpatterns = router.urls
