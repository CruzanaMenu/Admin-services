from rest_framework.viewsets import ModelViewSet
from users.models import Customer, Comida, Bebida, Pedido
from users.api.serializers import CustomerSerializer, ComidaSerializer, BebidaSerializer, PedidoSerializer

class CustomerApiViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class ComidaApiViewSet(ModelViewSet):
    serializer_class = ComidaSerializer
    queryset = Comida.objects.all()


class BebidaApiViewSet(ModelViewSet):
    serializer_class = BebidaSerializer
    queryset = Bebida.objects.all()

class PedidoApiViewSet(ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()