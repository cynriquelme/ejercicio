from django.urls import path
from . import views

urlpatterns = [
    path('transferencias/', views.Transferencias.as_view(), name='transferencias'),
    path('estado_transferencia/', views.EstadoTransferencia.as_view(), name='estado_transferencia'),
    path('list_transacciones/', views.ListTransacciones.as_view(), name='list_transacciones'),
]