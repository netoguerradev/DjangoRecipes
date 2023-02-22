from django.shortcuts import render
from utils.recipes.factory import make_recipe
#Define as funções que indicam o que será feito naquela rota e envia para o urls

def home(request):
    return render(request, 'global/home.html', context={
        'recipes': [make_recipe() for _ in range(3)]
    })


def recipe(request, id):
    return render(request, 'global/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })
