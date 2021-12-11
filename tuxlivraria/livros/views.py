from django.http import HttpResponse
from django.shortcuts import render
from .models import Livros2

# Create your views here.

def index(request):
    livros = Livros2.objects.all()
    return render(request, 'livrox/index.html', {
        'livros': livros
    })
