from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    ...
    return HttpResponse('HOME 2')

def sobre_view(request):
    ...
    return HttpResponse('SOBRE')

def contato_view(request):
    ...
    return HttpResponse('CONTATO')
