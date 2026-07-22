from django.db import models


class Ticket(models.Model):
    ESTADOS = [
        ('Abierto', 'Abierto'),
        ('En proceso', 'En proceso'),
        ('Resuelto', 'Resuelto'),
        ('Cerrado', 'Cerrado'),
    ]

    PRIORIDADES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    nombre_usuario = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=20, choices=PRIORIDADES, default='Media')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Abierto')
    tecnico_asignado = models.CharField(max_length=100, blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.estado}"


class RegistroMetrica(models.Model):
    ACCIONES = [
        ('Crear ticket', 'Crear ticket'),
        ('Actualizar ticket', 'Actualizar ticket'),
        ('Cerrar ticket', 'Cerrar ticket'),
    ]

    accion = models.CharField(max_length=50, choices=ACCIONES)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    tiempo_operacion_ms = models.IntegerField()
    estado_resultante = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.accion} - Ticket #{self.ticket.id} - {self.tiempo_operacion_ms} ms"