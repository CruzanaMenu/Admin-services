from django.urls import path
from .views import CustomerDetailView, CustomerListView
from . import views

urlpatterns = [
    path('customer/', CustomerListView.as_view(), name = 'Customer_list'),
    path('customer/<int:pk>', CustomerDetailView.as_view(), name='company'),
]