"""teste URL Configuration

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
from django.http import HttpResponse
from django.urls import path


def initial_page(request):
    return HttpResponse('tela 1: Pagina de inicial.')


def about(request):
    return HttpResponse('tela 2: sobre')


def contacts(request):
    return HttpResponse('tela 3: contatos.')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', initial_page),  # /initial-page/
    path('about', about),  # /about/
    path('contacts', contacts),  # /contacts/
]
