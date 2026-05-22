from django import forms
from .models import Equipo, Empleados, Asignacion, Ubicacion    

#formularios

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
        }

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'
        widgets = {
            'fecha_asignacion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'
      
        