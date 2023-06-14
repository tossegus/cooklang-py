from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def recipes(request):
    return render(request, 'recipes.html')

def shopping_list(request):
    return render(request, 'shopping_list.html')

