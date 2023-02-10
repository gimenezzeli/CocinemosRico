from django.urls import path
from recipes.views import create_recipes, list_recipes, RecipesDetailView

urlpatterns = [
    path('list-recipes/', list_recipes),
    path('create-recipes/', create_recipes),
    path('detail-recipes/<int:pk>/', RecipesDetailView.as_view() , name='details')
]