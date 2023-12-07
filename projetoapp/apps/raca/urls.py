from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'raca'

router = routers.DefaultRouter()
router.register('', views.RacaViewSet, basename='racas')

urlpatterns = [
    path('', include(router.urls)),
]