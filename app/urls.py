from django.urls import path
from django.http import HttpResponse
from . import views
# Informa o caminho da url, subdominio e a função que irá ser executada quando for feito a requisição da rota

urlpatterns = [
    path('', views.home, name="recipe-home"),
    path('recipe/<int:id>/', views.recipe, name="recipes-recipe")
]
