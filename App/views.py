from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Ubicacion, Empleados, Asignacion
from .forms import EquipoForm, UbicacionForm, EmpleadosForm, AsignacionForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q

# Create your views here.
def buscar_global(request):
    query = request.GET.get('buscar','') #obtenemos el termino de busqueda
    equipo = Equipo.objects.filter(
        Q(nombre__icontains=query) | Q(serial__icontains=query) | Q(inventario__icontains=query)
    ).order_by('id')
    empleado = Empleados.objects.filter(
        Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(cedula__icontains=query)
    ).order_by('id')

    ubicacion = Ubicacion.objects.filter(
        Q(ubicacion__icontains=query)
    ).order_by('id')

    asignacion = Asignacion.objects.filter(
        Q(empleado__nombre__icontains=query) |
        Q(equipo__nombre__icontains=query) |
        Q(ubicacion__ubicacion__icontains=query)
    ).order_by('id')

    context = {
        'buscar' : query,
        'equipo' : equipo,
        'empleado' : empleado,
        'ubicacion' : ubicacion,
        'asignacion' : asignacion
    }

    return render(request, 'search/searchinv.html', context)

def dashboard(request):
    total_equipos = Equipo.objects.count()
    total_empleados = Empleados.objects.count()
    total_asignaciones = Asignacion.objects.count()
    data = {
        'total_equipos': total_equipos,
        'total_empleados': total_empleados,
        'total_asignaciones': total_asignaciones
    }
    return render(request, 'app/dashboard.html', data)

def equipos(request):
    data = {
        'form': EquipoForm()
    }
    if request.method == 'POST':
        formulario = EquipoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Equipo guardado correctamente")
        else:
            data["form"] = formulario

    total_equipos = Equipo.objects.count()        
        
    return render(request, 'app/equipos/equipo.html', data)

def listar(request):
    equipos = Equipo.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(equipos, 5)
    try:
        equipos = paginator.page(page)
    except: 
        raise Http404

    data = {
        'entity': equipos,
        'paginator': paginator

    }

    return render(request, 'app/equipos/listar.html', data)

def modificar(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    data = {
        'form': EquipoForm(instance=equipo)
    }
    if request.method == 'POST':
        formulario = EquipoForm(data=request.POST, instance=equipo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Equipo Modificado correctamente")
            return redirect(to='listar')
        else:
            data["form"] = formulario
    return render(request, 'app/equipos/modificar.html', data)

def eliminar(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to='listar')

def ubicacion(request):
    data = {
        'form': UbicacionForm
    }
    if request.method == 'POST':
        formulario = UbicacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Ubicacion guardada correctamente")
        else:
            data["form"] = formulario
        
    return render(request, 'app/ubicacion/ubicacion.html', data)

def listarubicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(ubicaciones, 5)
    try:
        ubicaciones = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': ubicaciones,
        'paginator': paginator
    }
    return render(request, 'app/ubicacion/listarb.html', data)

def modificarubicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    data = {
        'form': UbicacionForm(instance=ubicacion)
    }
    if request.method == 'POST':
        formulario = UbicacionForm(data=request.POST, instance=ubicacion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Ubicacion modificada correctamente")
            return redirect(to='listarb')
        else:
            data["form"] = formulario
    return render(request, 'app/ubicacion/modificarb.html', data)

def eliminarubicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    ubicacion.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to='listarb') 

def empleados(request):
    data = {
        'form': EmpleadosForm()
    }
    if request.method == 'POST':
        formulario = EmpleadosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Empleado guardado correctamente")
        else:
            data["form"] = formulario
        
    return render(request, 'app/empleados/empleados.html', data)

def listadeempleados(request):
    empleados = Empleados.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(empleados, 5)
    try:
        empleados = paginator.page(page)
    except: 
        raise Http404

    data = {
        'entity': empleados,
        'paginator': paginator
    }
    return render(request, 'app/empleados/listaempleados.html', data)

def modificarempleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)
    data = {
        'form': EmpleadosForm(instance=empleado)
    }
    if request.method == 'POST':
        formulario = EmpleadosForm(data=request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Empleado modificado correctamente")
            return redirect(to='listaempleados')
        else:
            data["form"] = formulario
    return render(request, 'app/empleados/modificare.html', data)

def eliminarempleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)
    empleado.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to='listaempleados')

def asignacion(request):
    data = {
        'form': AsignacionForm()
    }
    if request.method == 'POST':
        formulario = AsignacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Asignacion guardada correctamente")
        else:
            data["form"] = formulario
        
    return render(request, 'app/asignacion/asignacion.html', data)

def lista_asignaciones(request):
    asignaciones = Asignacion.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(asignaciones, 5)
    try:
        asignaciones = paginator.page(page)
    except: 
        raise Http404
    data = {
        'entity': asignaciones,
        'paginator': paginator
    }
    return render(request, 'app/asignacion/listadoa.html', data)

def eliminarasignacion(request, id):
    asignacion = get_object_or_404(Asignacion, id=id)
    asignacion.delete()
    messages.success(request,"Asignacion Eliminada ")
    return redirect(to='lista_asignaciones')
