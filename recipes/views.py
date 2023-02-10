from django.shortcuts import render

from recipes.models import Recipes
from recipes.forms import RecipesForm
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

@login_required
def create_recipes(request):
    if request.method == 'GET':
        context = {
            'form': RecipesForm()
        }
        return render(request, 'recipes/create_recipes.html', context= context)

    elif request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            Recipes.objects.create(
                name= form.cleaned_data['name'],
                ingredients= form.cleaned_data['ingredients'],
                description = form.cleaned_data['description'],
                image=form.cleaned_data['image'],
            )
            context={
                'message':'Receta creada exitosamente',
            }
            return render(request, 'recipes/create_recipes.html', context=context)
        else:
            context= {
                'form_errors': form.errors,
                'form': RecipesForm(),
            }
            return render(request, 'recipes/create_recipes.html', context=context)


def list_recipes(request):
    if 'search' in request.GET:
        search= request.GET['search']
        recipes= Recipes.objects.filter(name__icontains=search)
    else:
        recipes= Recipes.objects.all()

    context={
        'recipes': recipes,
    }
    return render(request, 'recipes/recipes.html', context=context)


class RecipesDetailView(DetailView):
    model= Recipes
    template_name = 'recipes/detail_recipes.html'


