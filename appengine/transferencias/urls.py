from django.urls import path
from . import views

urlpatterns = [
    path('transferencias/', views.Transferencias.as_view(), name='transferencias'),
]