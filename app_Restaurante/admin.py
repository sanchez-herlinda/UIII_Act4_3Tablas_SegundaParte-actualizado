from django.contrib import admin
from .models import Platillo, Cliente, Pedido

@admin.register(Platillo)
class PlatilloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'disponibilidad', 'tiempo_preparacion')
    search_fields = ('nombre', 'categoria')
    list_filter = ('disponibilidad', 'categoria')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fechahora', 'estado', 'total', 'cantidad')
    list_filter = ('estado',)
