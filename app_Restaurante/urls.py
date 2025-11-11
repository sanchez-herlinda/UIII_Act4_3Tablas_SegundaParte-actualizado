from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Platillo
    path('platillo/ver/', views.ver_platillos, name='ver_platillos'),
    path('platillo/agregar/', views.agregar_platillo, name='agregar_platillo'),
    path('platillo/actualizar/<int:platillo_id>/', views.actualizar_platillo, name='actualizar_platillo'),
    path('platillo/borrar/<int:platillo_id>/', views.borrar_platillo, name='borrar_platillo'),

    # Cliente
    path('cliente/ver/', views.ver_clientes, name='ver_clientes'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
]
