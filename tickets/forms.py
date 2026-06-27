from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'nombre_usuario',
            'area',
            'titulo',
            'descripcion',
            'prioridad',
        ]

        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'prioridad': forms.Select(attrs={'class': 'form-control'}),
        }


class ActualizarTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'estado',
            'tecnico_asignado',
            'comentario',
        ]

        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'tecnico_asignado': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }