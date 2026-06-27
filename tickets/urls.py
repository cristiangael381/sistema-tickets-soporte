from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_ticket, name='crear_ticket'),
    path('ticket/<int:id>/', views.detalle_ticket, name='detalle_ticket'),
    path('ticket/<int:id>/editar/', views.editar_ticket, name='editar_ticket'),
]