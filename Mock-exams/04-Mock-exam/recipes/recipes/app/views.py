from django.shortcuts import render, redirect

from recipes.app.forms import RecipeForm, DeleteRecipeForm
from recipes.app.models import Recipe


def show_home(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'create.html', {'form': form})


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        return render(request, 'edit.html', {'form': form})
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'edit.html', {'form': form})


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
        return render(request, 'delete.html', {'form': form})
    else:
        recipe.delete()
        return redirect('home')


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    return render(request, 'details.html', {'recipe': recipe, 'ingredients': ingredients})
