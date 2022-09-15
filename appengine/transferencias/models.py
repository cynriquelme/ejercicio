from django.db import models
class Entidad(models.Model):
    descripcion = models.CharField('Descripción', max_length=60)
    
    class Meta:
        verbose_name= 'Entidad'
        verbose_name_plural= 'Entidades'

    def __str__(self):
        return self.descripcion

class CuentaBancaria(models.Model):
    nro_cuenta = models.IntegerField('Número de Cuenta')
    saldo = models.FloatField('Cuenta Corriente')
    class Meta:
        verbose_name= 'Cuenta Bancaria'
        verbose_name_plural= 'Cuentas Bancarias'

    def __str__(self):
        return str(self.nro_cuenta)

class Transaccion(models.Model):
    detalle = models.TextField('Detalle de Transacción')
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    class Meta:
        verbose_name= 'Transacción'
        verbose_name_plural= 'Transacciones'

    def __str__(self):
        return self.detalle