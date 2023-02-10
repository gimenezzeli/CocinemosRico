from django import forms
from recipes.models import Recipes

class RecipesForm(forms.ModelForm):
    class Meta:
        model= Recipes
        fields=['name','ingredients','description','image']