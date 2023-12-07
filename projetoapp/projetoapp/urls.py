"""projetoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ongs/', include('ong.urls', namespace='ong')),
    path('tutores/', include('tutor.urls', namespace='tutor')),
    path('especies/', include('especie.urls', namespace='especie')),
    path('racas/', include('raca.urls', namespace='raca')),
    path('animais/', include('animal.urls', namespace='animal')),
    path('adocoes/', include('adocao.urls', namespace='adocao')),
    path('veterinarios/', include('veterinario.urls', namespace='veterinario')),
    path('consultas/', include('consulta.urls', namespace='consulta')),
]
