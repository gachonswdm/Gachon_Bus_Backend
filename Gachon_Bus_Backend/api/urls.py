from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'locations', views.LocationViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

