from flask import Flask, render_template
from server import Server

server_item = None
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/seed/')
def seed():
    global server_item
    if not server_item:
      server_item = Server(os.getcwd())
    recipe_tree = server_item.recipe_tree.tree
    from pprint import pprint
    pprint(recipe_tree)
    return render_template('seed.html', recipe_tree=recipe_tree)

@app.route('/shoppinglist/')
def shoppinglist():
    global server_item
    if not server_item:
        server_item = Server(os.getcwd())
    shoppinglist="Hej"
    return render_template('shopping_list.html', shoppinglist=shoppinglist)

@app.route('/recipe/')
def recipe():
    import pdb; pdb.set_trace()
    path = request.GET.get('recipe_path')
    recipe = Recipe(path)
    ingredients = []
    for item in recipe.ingredients:
      ingredients.append(f'{item["name"]} {item["quantity"]}{item["units"]}')
    for item in recipe.steps:
      import pdb; pdb.set_trace()
    return render_template('recipe.html', path=path, metadata=metadata, ingredients=ingredients, steps=steps)


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

