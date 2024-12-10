from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_bodega/', views.crear_bodega, name='crear_bodega'),
    path('buscar_vino/', views.buscar_vino, name='buscar_vino'),
]