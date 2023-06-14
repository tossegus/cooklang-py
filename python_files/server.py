from recipe_tree import RecipeTree
from shoppinglist import ShoppingList

class Server():
  def __init__(self, path):
      # Only the 
      self.recipe_tree = RecipeTree(path)
      self.shopping_list = ShoppingList()

  def start(self):
      # Run everything from here
      # Populate web page
      # Should this run in a seperate thread?
      # > Main page should be the seed-view
      # > From main page:
      #   Click recipes to load them
      # > From recipe page:
      #   * Scrollable
      #   * Option to add to shopping list
      
  def add_to_shopping_list(self, path):
      # Load recipe
      recipe = Recipe(path)
      # Add to shopping list
      self.shopping_list.add_recipe(recipe)
