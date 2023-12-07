from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'veterinarios'

router = routers.DefaultRouter()
router.register('', views.VeterinarioViewSet, basename='veterinarios')

urlpatterns = [
    path('', include(router.urls) )
]