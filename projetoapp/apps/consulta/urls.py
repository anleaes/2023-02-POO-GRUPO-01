from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'consultas'

router = routers.DefaultRouter()
router.register('', views.ConsultaViewSet, basename='consultas')

urlpatterns = [
    path('', include(router.urls) )
]