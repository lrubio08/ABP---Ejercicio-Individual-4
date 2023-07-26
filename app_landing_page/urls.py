from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('usuarios/', views.lista_usuarios , name='usuarios'),
    path('registrarse/', views.registrarse , name='registrarse'),
]