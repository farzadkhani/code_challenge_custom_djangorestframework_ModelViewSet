from django.urls import path

from rest_framework import routers

from .views import UserModelViewSet


router = routers.SimpleRouter()

router.register(r"users", UserModelViewSet, basename="users")


# app_name = "account"

urlpatterns = [] + router.urls
