from django.shortcuts import render
import os, sys
if '__file__' in vars():
    print("We are running the script non interactively")
    path = os.path.join(os.path.dirname(__file__), os.pardir + os.sep + os.pardir)
    sys.path.append(path)    
else:
    print('We are running the script interactively')
    sys.path.append(os.pardir + os.sep + os.pardir)

from server import Server

global server_item

def home(request):
    # This is the entry point.
    # Create the server object here.
    path = os.getcwd()
    global server_item
    server_item = Server(path)
    return render(request, 'home.html')

def recipes(request):
    global server_item
    recipe_tree = server_item.recipe_tree
    for item in recipe_tree:
      recipes_list
    recipes_list = ['Recipe 1', 'Recipe 2', 'Recipe 3']  # Replace with your actual recipe data
    context = {'recipes_list': recipes_list}
    return render(request, 'recipes.html', context)

def shopping_list(request):
    global server_item
    return render(request, 'shopping_list.html')

