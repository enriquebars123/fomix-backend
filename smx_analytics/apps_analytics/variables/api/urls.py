""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_analytics.variables.api.views import (
    VariablesViewSet
)

router = routers.DefaultRouter()
router.register(r'^api/v1/variables', VariablesViewSet)

urlpatterns = router.urls
