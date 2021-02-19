""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_analytics.regla.api.views import reglaViewSet
router = routers.DefaultRouter()
router.register(r'^api/v1/regla', reglaViewSet)


urlpatterns = router.urls
