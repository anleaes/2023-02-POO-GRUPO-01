from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'tutor'

router = routers.DefaultRouter()
router.register('', views.TutorViewSet, basename='tutores')

urlpatterns = [
    path('tutores/', include('tutores.urls', namespace='tutores')),
]