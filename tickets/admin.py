from django.contrib import admin
from .models import Ticket


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