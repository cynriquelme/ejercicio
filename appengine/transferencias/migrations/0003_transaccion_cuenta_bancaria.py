# Generated by Django 3.2 on 2022-09-16 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transferencias', '0002_auto_20220916_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='cuenta_bancaria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transferencias.cuentabancaria'),
            preserve_default=False,
        ),
    ]