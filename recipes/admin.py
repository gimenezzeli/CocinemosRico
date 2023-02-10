from django.contrib import admin
from recipes.models import Recipes

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display= ('name', 'ingredients')
    

