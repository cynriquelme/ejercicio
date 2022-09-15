from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CuentaBancaria
from .serializers import CuentaBancariaSerializer
from rest_framework import permissions

class Transferencias(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        cuenta = CuentaBancaria.objects.all()
        serializer = CuentaBancariaSerializer(cuenta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'nro_cuenta': request.data.get('nro_cuenta'),
            'saldo': request.data.get('saldo'),
        }
        serializer = CuentaBancariaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)