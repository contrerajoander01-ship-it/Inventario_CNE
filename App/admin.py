from django.contrib import admin
from .models import Equipo, Empleados, Asignacion, Ubicacion

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Empleados)
admin.site.register(Asignacion)
admin.site.register(Ubicacion)
