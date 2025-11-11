from django.shortcuts import render, redirect, get_object_or_404
from .models import Platillo, Cliente

# ==========================
# INICIO
# ==========================
def inicio(request):
    platillos = Platillo.objects.all().order_by('-id')  # más recientes primero
    clientes = Cliente.objects.all().order_by('-id')
    total_platillos = platillos.count()
    total_clientes = clientes.count()

    return render(request, 'inicio.html', {
        'platillos': platillos,
        'clientes': clientes,
        'total_platillos': total_platillos,
        'total_clientes': total_clientes,
    })

# ==========================
# CRUD PLATILLO
# ==========================
def ver_platillos(request):
    platillos = Platillo.objects.all().order_by('nombre')
    return render(request, 'platillo/ver_platillos.html', {'platillos': platillos})

def agregar_platillo(request):
    if request.method == 'POST':
        Platillo.objects.create(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            precio=request.POST.get('precio'),
            categoria=request.POST.get('categoria'),
            disponibilidad=True if request.POST.get('disponibilidad') == 'on' else False,
            ingredientes=request.POST.get('ingredientes'),
            tiempo_preparacion=request.POST.get('tiempo_preparacion')
        )
        return redirect('ver_platillos')
    return render(request, 'platillo/agregar_platillo.html')

def actualizar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    if request.method == 'POST':
        platillo.nombre = request.POST.get('nombre')
        platillo.descripcion = request.POST.get('descripcion')
        platillo.precio = request.POST.get('precio')
        platillo.categoria = request.POST.get('categoria')
        platillo.disponibilidad = True if request.POST.get('disponibilidad') == 'on' else False
        platillo.ingredientes = request.POST.get('ingredientes')
        platillo.tiempo_preparacion = request.POST.get('tiempo_preparacion')
        platillo.save()
        return redirect('ver_platillos')
    return render(request, 'platillo/actualizar_platillo.html', {'platillo': platillo})

def borrar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    if request.method == 'POST':
        platillo.delete()
        return redirect('ver_platillos')
    return render(request, 'platillo/borrar_platillo.html', {'platillo': platillo})

# ==========================
# CRUD CLIENTE
# ==========================
def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido')
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            direccion_casa=request.POST.get('direccion_casa'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento') or None,
            alergias=request.POST.get('alergias')
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion_casa = request.POST.get('direccion_casa')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
        cliente.alergias = request.POST.get('alergias')
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})
