from django.shortcuts import render
from django.http import JsonResponse

import os, sys

if "__file__" in vars():
    print("We are running the script non interactively")
    path = os.path.join(os.path.dirname(__file__), os.pardir + os.sep + os.pardir)
    sys.path.append(path)
else:
    print("We are running the script interactively")
    sys.path.append(os.pardir + os.sep + os.pardir)

from server import Server
from recipe import Recipe

server_item = Server(os.getcwd())


def home(request):
    # This is the entry point.
    # Create the server object here.
    path = os.getcwd()
    global server_item
    server_item = Server(path)
    return render(request, "home.html")


def seed(request):
    global server_item
    if not server_item:
        server_item = Server(os.getcwd())
    recipe_tree = server_item.recipe_tree.tree
    context = {"recipe_tree": recipe_tree}
    return render(request, "seed.html", context)


def shopping_list(request):
    global server_item
    if not server_item:
        server_item = Server(os.getcwd())
    return render(request, "shopping_list.html")


def recipe(request):
    path = request.GET.get("recipe_path")
    recipe = Recipe(path)
    from pprint import pprint

    #  pprint(recipe.ingredients)
    ingredients = []
    for item in recipe.ingredients:
        ingredients.append(f'{item["name"]} {item["quantity"]}{item["units"]}')
    for item in recipe.steps:
        import pdb

        pdb.set_trace()
    context = {
        "path": path,
        "metadata": recipe.metadata,
        "ingredients": ingredients,
        "steps": recipe.steps,
    }
    return render(request, "recipe.html", context)


def add_to_list(request):
    # Your function logic goes here
    # ...
    print("HEJHEJHEJ")
    return JsonResponse({"message": "Successully added to list"})
