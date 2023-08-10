from django.urls import path

from . import views

urlpatterns = [
    path('registrar/', views.UserFormView.as_view(), name='register'),

    path("libros/", views.index, name="index"),
    path('libros/<int:libro_id>/', views.books, name='books'),

    path("autores/", views.autores, name="autores"),
    path('autores/<int:autor_id>/', views.detalles_autor, name='detalles_autor'),

    path('crear_libro', views.crear_libro, name="crear_libro"),
    path('crear_autor', views.crear_autor, name="crear_autor"),

    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro, name="eliminar_libro"),
    path('eliminar_autor/<int:autor_id>/', views.eliminar_autor, name="eliminar_autor"),

    path('editar_libro/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    path('editar_autor/<int:autor_id>/', views.editar_autor, name='editar_autor'),

    path('buscar/', views.buscar, name='buscar'),

]