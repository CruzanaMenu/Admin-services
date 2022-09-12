from rest_framework.serializers import ModelSerializer
from users.models import Customer , Comida, Bebida, Pedido

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'telephone_number', 'gender', 'pub_date']

class ComidaSerializer(ModelSerializer):
    class Meta:
        model = Comida
        fields = ['id', 'name_food', 'desc_small', 'desc_large', 'desc_full', 'price']

class BebidaSerializer(ModelSerializer):
    class Meta:
        model = Bebida
        fields = ['id', 'name_bebida', 'desc_bebida', 'price']

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'date_pedido']