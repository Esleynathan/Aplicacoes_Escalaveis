from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Usuario
from random import randint

#@cache_page(60*1)
def teste(request):
    usuario = Usuario.objects.all()
    x = randint(1,10)

    return render(request, 'teste.html', {'usuarios': usuario, 'x': x})