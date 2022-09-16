from django.contrib import admin
from .models import Entidad, CuentaBancaria, Transferencia, Moneda

class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = (
            'nro_cuenta',
            'saldo',
        )
    search_fields = ('nro_cuenta',)

class EntidadAdmin(admin.ModelAdmin):
    search_fields = ('descripcion',)

admin.site.register(Entidad, EntidadAdmin)
admin.site.register(Moneda)
admin.site.register(CuentaBancaria, CuentaBancariaAdmin)
admin.site.register(Transferencia)