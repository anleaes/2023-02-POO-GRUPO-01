from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ongs'

router = routers.DefaultRouter()
router.register('', views.OngViewSet, basename='ongs')

urlpatterns = [
    path('', include(router.urls) )
]