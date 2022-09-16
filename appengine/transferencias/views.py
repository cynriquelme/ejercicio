from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CuentaBancaria, Transferencia
from .serializers import CuentaBancariaSerializer, TransferenciasSerializer
from rest_framework import permissions

class Transferencias(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # Creación
        return_ = {'error': True, 'data': {}, 'info': ''}
        data = {
            'cuenta_origen': request.data.get('cuenta_origen'),
            'cuenta_destino': request.data.get('cuenta_destino'),
            'entidad_destino': request.data.get('entidad_destino'),
            'moneda': request.data.get('moneda'),
            'monto': request.data.get('monto'),
        }
        serializer = TransferenciasSerializer(data=data)
        if serializer.is_valid():
            cuenta = CuentaBancaria.objects.filter(id=(data['cuenta_origen'])) 
            saldo = cuenta[0].saldo
            if saldo>0 and data['monto']<saldo:
                serializer.save()
                return_['info'] = 'Transferencia realizada con éxito'
                return_['error'] = False
                return_['data'] = serializer.data
                return Response(return_, status=status.HTTP_201_CREATED)
            else:
                return_['info'] = 'El saldo de la Cuenta es insuficiente'
                return Response(return_)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class EstadoTransferencia(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return_ = {'error': True, 'data': {}, 'info': ''}
        data = {
            'id_transferencia': request.data.get('id_transferencia'),
        }
        transferencia = Transferencia.objects.filter(id=(data['id_transferencia']))
        if transferencia:
            print(transferencia)
            serializer = TransferenciasSerializer(transferencia, many=True)
            return_['info'] = 'Información de Transferencia'
            return_['error'] = False
            return_['data'] = serializer.data
            return Response(return_, status=status.HTTP_200_OK)
        else:
            return_['info'] = 'El id ingresado no existe'
            return Response(return_)
           
class ListTransacciones(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return_ = {'error': True, 'data': {}, 'info': ''}
        data = {
            'cuenta_origen': request.data.get('cuenta_origen'),
        }
        cuenta = CuentaBancaria.objects.filter(nro_cuenta=(data['cuenta_origen']))
        if cuenta:
            transferencia = Transferencia.objects.filter(cuenta_origen=cuenta[0].id)
            serializer = TransferenciasSerializer(transferencia, many=True)
            return_['info'] = 'Información de Transferencia'
            return_['error'] = False
            return_['data'] = serializer.data
            return Response(return_, status=status.HTTP_200_OK)
        else:
            return_['info'] = 'La cuenta ingresada no existe'
            return Response(return_)