from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request):
    ...
    return render(request, 'recipes/pages/home.html', {
        'name':'Fernando'
    })

# Status de resposta HTTP : https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status#respostas_bem-sucedidas