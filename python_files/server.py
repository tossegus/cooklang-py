from recipe_tree import RecipeTree
from shoppinglist import ShoppingList
import subprocess, os

class Server():
  def __init__(self, path):
      # Create a recipe tree and shopping list at the start.
      self.recipe_tree = RecipeTree(path)
      self.shopping_list = ShoppingList()
      self.recipes_in_list = []

  def start(self):
      ## DESIGN
      # Two menu items in the top: "Recipes" and "Shopping list"
      # Below, the currently selected page is visible.
      # The starting page is Recipes.
      path = os.getcwd()
      website_dir = 'cookcliwebsite'
      website_dir = 'mywebsite'
      if os.path.exists(path + os.sep + website_dir):
        # website exists
        # Now we want to start it from here.
        command = f'python {website_dir}{os.sep}manage.py runserver'
        subprocess.call(command, shell=True)

      ## IMPLEMENTATION DETAILS
      # Should this run in a seperate thread?
      # All pages shall be scrollable.
      # * Recipe page:
      #   1. Clicking a recipe should load that recipe and display it
      #   2. Clicking a folder should collapse it, 
      #      hiding recipes located beneath
      #   3. There should be a button "Add to shopping list" on the
      #       recipe page
      # * Shopping list page:
      #   1. The recipes in the shopping list should be added to the top.
      #      Should it be possible to remove them? I guess so.
      #      That should just remove them from the class list of recipes
      #   2. All items from currently added recipes should be displayed
      #      when we enter this page
      
  def add_to_shopping_list(self, path):
      # Load recipe
      recipe = Recipe(path)
      # Add to shopping list
      self.shopping_list.add_recipe(recipe)
