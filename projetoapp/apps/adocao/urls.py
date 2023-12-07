from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'adocoes'

router = routers.DefaultRouter()
router.register('', views.AdocaoViewSet, basename='adocoes')

urlpatterns = [
    path('', include(router.urls) )
]