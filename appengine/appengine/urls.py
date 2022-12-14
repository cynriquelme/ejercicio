"""appengine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from transferencias import views as trans_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('transferencias/', trans_views.Transferencias.as_view(), name="transferencias"),
    path('estado_transferencia/', trans_views.EstadoTransferencia.as_view(), name="estado_transferencia"),
    path('list_transacciones/', trans_views.ListTransacciones.as_view(), name="list_transacciones"),
]

admin.site.site_header = "API"
admin.site.index_title = "Panel de Administrador"
admin.site.site_title = "API"