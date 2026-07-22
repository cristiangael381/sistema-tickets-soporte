from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Ticket, RegistroMetrica
from .forms import TicketForm, ActualizarTicketForm
import time


def inicio(request):
    estado = request.GET.get('estado')
    prioridad = request.GET.get('prioridad')
    buscar = request.GET.get('buscar')

    tickets = Ticket.objects.all().order_by('-fecha_creacion')

    if estado:
        tickets = tickets.filter(estado=estado)

    if prioridad:
        tickets = tickets.filter(prioridad=prioridad)

    if buscar:
        tickets = tickets.filter(
            titulo__icontains=buscar
        ) | Ticket.objects.filter(
            nombre_usuario__icontains=buscar
        ) | Ticket.objects.filter(
            area__icontains=buscar
        ) | Ticket.objects.filter(
            tecnico_asignado__icontains=buscar
        )

    total_tickets = Ticket.objects.count()
    abiertos = Ticket.objects.filter(estado='Abierto').count()
    en_proceso = Ticket.objects.filter(estado='En proceso').count()
    resueltos = Ticket.objects.filter(estado='Resuelto').count()
    cerrados = Ticket.objects.filter(estado='Cerrado').count()

    return render(request, 'tickets/inicio.html', {
        'tickets': tickets,
        'total_tickets': total_tickets,
        'abiertos': abiertos,
        'en_proceso': en_proceso,
        'resueltos': resueltos,
        'cerrados': cerrados,
        'estado_seleccionado': estado,
        'prioridad_seleccionada': prioridad,
        'buscar': buscar,
    })


def crear_ticket(request):
    if request.method == 'POST':
        inicio_tiempo = time.time()
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save()
            fin_tiempo = time.time()
            tiempo_ms = int((fin_tiempo - inicio_tiempo) * 1000)

            RegistroMetrica.objects.create(
                accion='Crear ticket',
                ticket=ticket,
                tiempo_operacion_ms=tiempo_ms,
                estado_resultante=ticket.estado,
                prioridad=ticket.prioridad
            )

            messages.success(request, 'El ticket fue creado correctamente.')
            return redirect('inicio')
    else:
        form = TicketForm()

    return render(request, 'tickets/crear_ticket.html', {
        'form': form
    })


def detalle_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    return render(request, 'tickets/detalle_ticket.html', {
        'ticket': ticket
    })


def editar_ticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if request.method == 'POST':
        inicio_tiempo = time.time()
        form = ActualizarTicketForm(request.POST, instance=ticket)

        if form.is_valid():
            ticket = form.save()
            fin_tiempo = time.time()
            tiempo_ms = int((fin_tiempo - inicio_tiempo) * 1000)

            RegistroMetrica.objects.create(
                accion='Actualizar ticket',
                ticket=ticket,
                tiempo_operacion_ms=tiempo_ms,
                estado_resultante=ticket.estado,
                prioridad=ticket.prioridad
            )

            messages.success(request, 'El ticket fue actualizado correctamente.')
            return redirect('detalle_ticket', id=ticket.id)
    else:
        form = ActualizarTicketForm(instance=ticket)

    return render(request, 'tickets/editar_ticket.html', {
        'form': form,
        'ticket': ticket
    })


def cerrar_ticket(request, id):
    inicio_tiempo = time.time()
    ticket = get_object_or_404(Ticket, id=id)

    ticket.estado = 'Cerrado'
    ticket.save()

    fin_tiempo = time.time()
    tiempo_ms = int((fin_tiempo - inicio_tiempo) * 1000)

    RegistroMetrica.objects.create(
        accion='Cerrar ticket',
        ticket=ticket,
        tiempo_operacion_ms=tiempo_ms,
        estado_resultante=ticket.estado,
        prioridad=ticket.prioridad
    )

    messages.success(request, 'El ticket fue cerrado correctamente.')
    return redirect('detalle_ticket', id=ticket.id)


def reporte_tickets(request):
    total = Ticket.objects.count()
    abiertos = Ticket.objects.filter(estado='Abierto').count()
    en_proceso = Ticket.objects.filter(estado='En proceso').count()
    resueltos = Ticket.objects.filter(estado='Resuelto').count()
    cerrados = Ticket.objects.filter(estado='Cerrado').count()

    prioridad_alta = Ticket.objects.filter(prioridad='Alta').count()
    prioridad_media = Ticket.objects.filter(prioridad='Media').count()
    prioridad_baja = Ticket.objects.filter(prioridad='Baja').count()

    total_metricas = RegistroMetrica.objects.count()

    return render(request, 'tickets/reporte_tickets.html', {
        'total': total,
        'abiertos': abiertos,
        'en_proceso': en_proceso,
        'resueltos': resueltos,
        'cerrados': cerrados,
        'prioridad_alta': prioridad_alta,
        'prioridad_media': prioridad_media,
        'prioridad_baja': prioridad_baja,
        'total_metricas': total_metricas,
    })
