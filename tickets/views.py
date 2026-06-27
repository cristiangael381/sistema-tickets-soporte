from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm, ActualizarTicketForm


def inicio(request):
    tickets = Ticket.objects.all().order_by('-fecha_creacion')

    total_tickets = tickets.count()
    abiertos = tickets.filter(estado='Abierto').count()
    en_proceso = tickets.filter(estado='En proceso').count()
    resueltos = tickets.filter(estado='Resuelto').count()

    return render(request, 'tickets/inicio.html', {
        'tickets': tickets,
        'total_tickets': total_tickets,
        'abiertos': abiertos,
        'en_proceso': en_proceso,
        'resueltos': resueltos,
    })


def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            form.save()
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
        form = ActualizarTicketForm(request.POST, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect('detalle_ticket', id=ticket.id)
    else:
        form = ActualizarTicketForm(instance=ticket)

    return render(request, 'tickets/editar_ticket.html', {
        'form': form,
        'ticket': ticket
    })