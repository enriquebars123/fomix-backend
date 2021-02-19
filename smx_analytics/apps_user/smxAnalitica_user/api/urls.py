""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_user.smxAnalitica_user.api.views import (
    UserViewSet,
    UserAreaViewSet,
)

router = routers.DefaultRouter()
router.register(r'^api/v1/user', UserViewSet)
router.register(r'^api/v1/userArea', UserAreaViewSet)
router.register(r'^api/v1/login', UserViewSet)


urlpatterns = router.urls
