from rest_framework import serializers
from .models import CuentaBancaria, Transferencia
class CuentaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = ["nro_cuenta", "saldo"]

class TransferenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencia
        fields = ["cuenta_origen", "cuenta_destino", "entidad_destino", "moneda", "monto", "estado"]