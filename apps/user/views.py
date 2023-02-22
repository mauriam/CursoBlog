from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return HttpResponse("hola estas en el login")
def register(request):
    return HttpResponse("esto es un registro")