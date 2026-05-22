from django.db import models
from django.utils import timezone
class Ubicacion(models.Model):
    ubicacion = models.CharField(max_length=100, unique=True, verbose_name="Ubicación")
    def __str__(self):
        return self.ubicacion

class Equipo(models.Model):
    # Opciones para el campo 'estado'
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo / Operativo'),
        ('MANTENIMIENTO', 'En Mantenimiento'),
        ('DEBAJA', 'Dado de Baja'),
        ('ALMACENADO', 'En Almacén'),
    ]

    nombre = models.CharField(max_length=100,blank=True, null=True, verbose_name="Nombre del Equipo")
    modelo = models.CharField(max_length=100,blank=True, null=True, verbose_name="Modelo")
    serial = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="Número de Serial")
    inventario = models.CharField(max_length=50, unique=True,blank=True, null=True, verbose_name="Código de Inventario")
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='ACTIVO', 
        verbose_name="Estado actual"
    )
    accesorios = models.CharField(max_length=50, verbose_name="Accesorios")
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True)
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    fecha_registro = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - {self.serial} ({self.inventario})"

class Empleados(models.Model):

    nombre = models.CharField(max_length=100, verbose_name="Nombre") 
    apellido = models.CharField(max_length=100, verbose_name="Apellido") 
    cedula = models.CharField(max_length=20, unique=True, verbose_name="Cédula") 
    correo = models.EmailField(unique=True, verbose_name="Correo") 
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"

class Asignacion(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(blank=True, null=True)
    fecha_devolucion = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipo} - {self.empleado} ({self.fecha_asignacion})"