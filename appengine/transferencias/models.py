from django.db import models
class Entidad(models.Model):
    descripcion = models.CharField('Descripción', max_length=60)
    
    class Meta:
        verbose_name= 'Entidad'
        verbose_name_plural= 'Entidades'

    def __str__(self):
        return self.descripcion

class Moneda(models.Model):
    descripcion = models.CharField('Moneda', max_length=60)
    
    class Meta:
        verbose_name= 'Moneda'
        verbose_name_plural= 'Monedas'

    def __str__(self):
        return self.descripcion

class CuentaBancaria(models.Model):
    nro_cuenta = models.IntegerField('Número de Cuenta')
    saldo = models.FloatField('Cuenta Corriente')
    class Meta:
        verbose_name= 'Cuenta Bancaria'
        verbose_name_plural= 'Cuentas Bancarias'

    def __str__(self):
        return str(self.saldo)

class Transferencia(models.Model):
    ESTADOS_CHOICES = (
            ('PEN', 'PENDIENTE'),
            ('CON', 'CONFIRMADO'),
            ('REC', 'RECHAZADO'),
    )
  
    cuenta_origen = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE)
    cuenta_destino = models.IntegerField('Cuenta Destino')
    entidad_destino = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    monto = models.FloatField('Monto')
    estado = models.CharField('Estado', max_length=3, default="PEN",choices=ESTADOS_CHOICES)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    class Meta:
        verbose_name= 'Transferencia'
        verbose_name_plural= 'Transferencias'

    def __str__(self):
        return str(self.cuenta_origen)