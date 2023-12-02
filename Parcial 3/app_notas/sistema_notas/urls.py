from django.urls import path

from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('gestion/',views.GestionNota, name='gestionNota'),
    path('crear/',views.CrearNota, name='crearNota'),
    path('ver/<id>/',views.VerNota, name='verNota'),
    path('editar/<id>/',views.EditarNota, name='editarNota'),
    path('borrar/<id>/',views.BorrarNota, name='borrarNota')
]