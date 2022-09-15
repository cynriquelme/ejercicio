from rest_framework import serializers
from .models import CuentaBancaria
class CuentaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = ["nro_cuenta", "saldo"]