from django.shortcuts import render
from django.http import HttpResponse
#Define as funções que indicam o que será feito naquela rota e envia para o urls

def home(request):
    return render(request, 'global/home.html')
