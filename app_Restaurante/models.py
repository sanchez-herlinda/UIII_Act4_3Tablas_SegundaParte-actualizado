from django.db import models

# ==========================
# MODELO: PLATILLO
# ==========================
class Platillo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)
    ingredientes = models.TextField(blank=True, null=True)
    tiempo_preparacion = models.IntegerField(verbose_name="Tiempo de preparación (min)")

    def __str__(self):
        return self.nombre

# ==========================
# MODELO: CLIENTE
# ==========================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion_casa = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================
# MODELO: PEDIDO (pendiente)
# ==========================
class Pedido(models.Model):
    fechahora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=30, default='Pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    notas = models.TextField(blank=True, null=True)
    cantidad = models.IntegerField(default=1)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    idplatillo = models.ForeignKey(Platillo, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"Pedido #{self.id} - Estado: {self.estado}"
