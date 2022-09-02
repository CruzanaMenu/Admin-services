from rest_framework.serializers import ModelSerializer
from users.models import Customer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'telephone_number', 'gender', 'pub_date']