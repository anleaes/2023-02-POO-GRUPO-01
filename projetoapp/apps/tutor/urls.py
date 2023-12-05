from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tutores'

router = routers.DefaultRouter()
router.register('', views.TutorViewSet, basename='tutores')

urlpatterns = [
    path('', include(router.urls)),
]