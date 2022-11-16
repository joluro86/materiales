from django.contrib import admin
from django.urls import path
from controlmateriales.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('gestionbd/', gestionarbd, name="gestionbd"),
    path('reiniciar/', reiniciar, name="reiniciar"),
    path('faltantes_fenix/', calculo_diferencia_perseo_vs_fenix,
         name="faltantesenperseo"),
]
