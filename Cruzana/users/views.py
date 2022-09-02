from django.views import View
from .models import Customer
from django.http import JsonResponse
from django.forms.models import model_to_dict


class CustomerListView(View):
    def get(self, request):
        if('name' in request.GET):
            cList = Customer.objects.filter(name__contains = request.GET['first_name'])
        else:
            cList = Customer.objects.all()
        return JsonResponse(list(cList.values()), safe = False)

    
class CustomerDetailView(View):
    def get(self, request, pk):
        customerOne = Customer.objects.get(pk=pk)
        return JsonResponse(model_to_dict(customerOne))
