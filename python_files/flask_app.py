from flask import Flask, render_template, request
from server import Server
from recipe import Recipe
from shoppinglist import ShoppingList
from cooklang import parseRecipe
import os, re

server_item = None
shopping_list = []
app = Flask(__name__)

def add_to_shoppinglist(path):
    global shopping_list
    if path not in shopping_list:
      print("Added to list")
      # Only add each recipe once.
      shopping_list.append(path)

@app.route('/')
def home():
    return seed()

@app.route('/seed/')
def seed():
    global server_item
    if not server_item:
      server_item = Server(os.getcwd())
    recipe_tree = server_item.recipe_tree.tree
    from pprint import pprint
    pprint(recipe_tree)
    return render_template('seed.html', recipe_tree=recipe_tree)

@app.route('/shoppinglist/', methods=['POST','GET'])
def shoppinglist():
    global server_item, shopping_list
    if not server_item:
        server_item = Server(os.getcwd())

    if request.method == 'POST':
      print('Handle post')
      url = request.form.get('button')
      if url in shopping_list:
        shopping_list.remove(url)
     
    int_dict = {}

    if not shopping_list:
      # The shopping_list is empty
      print("Empty list")
    else:
      print("List not empty")
      for item in shopping_list:
        filename = os.path.basename(item)
        int_dict[filename] = item
      print("List is not empty")
    return render_template('shopping_list.html', recipes=int_dict)

@app.route('/printshoppinglist/', methods=["POST", "GET"])
def printshoppinglist():
    global shopping_list
    shoppinglist = ShoppingList()
    int_dict = {}
    if request.method == 'POST':
      if request.form.get('button') == 'empty_list':
        shopping_list = []
    else:
      for item in shopping_list:
          shoppinglist.add_recipe(parseRecipe(item))

      for item in shoppinglist.items:
        int_dict[item] = f'{shoppinglist.items[item].quantity}{shoppinglist.items[item].unit}'

    return render_template('print_shopping_list.html', shoppinglist=int_dict)

@app.route('/recipe/', methods=['POST', 'GET'])
def recipe():
    path = request.args.get('recipe_path')
    if request.method == 'POST':
      print("Got button press!")
      if request.form.get('add_to_recipe') == 'add':
        # add this recipe to the shopping_list
        add_to_shoppinglist(path)
        
    else:
      path = request.args.get('recipe_path')

    recipe = Recipe(path)
    ingredients = []
    for item in recipe.ingredients:
      ingredients.append(f'{item["name"]} {item["quantity"]}{item["units"]}')

    step_list = recipe.steps_str.split('\n')
    step_dict = {}
    for item in step_list:
      m = re.search('[^\ ]', item)
      if m:
        index = m.start()
      else:
        index = 0
      # Strip leading white spaces
      key = item[index:]
      step_dict[key] = "TAB" if key.startswith('[') else "BASE"

    return render_template('recipe.html',
                           path=path, 
                           metadata=recipe.metadata, 
                           ingredients=ingredients, 
                           steps=step_dict)

def main(path):
    global server_item
    if not server_item:
      server_item = Server(path)
      print("Server setup!")

    # Start application
    app.run(debug=True)

if __name__ == '__main__':
    # Running interactively
    print("HELLO!")
    main(os.getcwd())

