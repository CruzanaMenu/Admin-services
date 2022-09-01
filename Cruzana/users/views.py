from django.shortcuts import render
from django.http import HttpResponse


def index(request): 
    return HttpResponse("Información de los clientes")


def detail(request, users_id):
    return HttpResponse(f"Estas viendo al cliente número {users_id}")