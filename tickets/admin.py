from django.contrib import admin
from .models import Ticket, RegistroMetrica


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'nombre_usuario',
        'area',
        'prioridad',
        'estado',
        'tecnico_asignado',
        'fecha_creacion',
    )

    list_filter = (
        'estado',
        'prioridad',
        'area',
    )

    search_fields = (
        'titulo',
        'nombre_usuario',
        'area',
        'tecnico_asignado',
    )


@admin.register(RegistroMetrica)
class RegistroMetricaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'accion',
        'ticket',
        'tiempo_operacion_ms',
        'estado_resultante',
        'prioridad',
        'fecha_registro',
    )

    list_filter = (
        'accion',
        'estado_resultante',
        'prioridad',
    )

    search_fields = (
        'accion',
        'estado_resultante',
        'prioridad',
    )