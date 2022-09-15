# Generated by Django 3.2 on 2022-09-14 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuentaBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_cuenta', models.IntegerField(verbose_name='Número de Cuenta')),
                ('saldo', models.FloatField(verbose_name='Cuenta Corriente')),
            ],
            options={
                'verbose_name': 'Cuenta Bancaria',
                'verbose_name_plural': 'Cuentas Bancarias',
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Entidad',
                'verbose_name_plural': 'Entidades',
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField(verbose_name='Detalle de Transacción')),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transferencias.entidad')),
            ],
            options={
                'verbose_name': 'Transacción',
                'verbose_name_plural': 'Transacciones',
            },
        ),
    ]