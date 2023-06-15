from recipe_tree import RecipeTree
from shoppinglist import ShoppingList


class DataWrapper:
    def __init__(self, path):
        # Create a recipe tree and shopping list at the start.
        self.recipe_tree = RecipeTree(path)
        self.shopping_list = ShoppingList()
        self.recipes_in_list = []
