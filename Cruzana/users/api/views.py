from rest_framework.viewsets import ModelViewSet
from users.models import Customer
from users.api.serializers import CustomerSerializer

class CustomerApiViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()