from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('equipos/', views.equipos, name='equipos'),
    path('equipos/listar/', views.listar, name='listar'),
    path('equipos/modificar/<int:id>/', views.modificar, name='modificar'),
    path('equipos/eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('ubicacion/listarb/', views.listarubicaciones, name='listarb'),
    path('ubicacion/modificarb/<int:id>/', views.modificarubicacion, name='modificarb'),
    path('ubicacion/eliminarb/<int:id>/', views.eliminarubicacion, name='eliminarb'),
    path('empleados/', views.empleados, name='empleados'),
    path('empleados/listaempleados/', views.listadeempleados, name='listaempleados'),
    path('empleados/modificarempleado/<int:id>/', views.modificarempleado, name='modificarempleado'),
    path('empleados/eliminarempleado/<int:id>/', views.eliminarempleado, name='eliminarempleado'),
    path('asignacion/', views.asignacion, name='asignacion'),
    path('asignacion/listadoa/', views.lista_asignaciones, name='lista_asignaciones'),
    path('asignacion/eliminarasignacion/<int:id>/', views.eliminarasignacion, name='eliminarasignacion'),
    path('buscar/', views.buscar_global, name='buscar'),
]

