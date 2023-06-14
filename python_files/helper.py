from pprint import pprint #remove this before commit
import re, math
from collections import namedtuple

Ingredient = namedtuple("Ingredient", "quantity unit")

def convert_str_to_int(string):
    m = re.match('(?P<match>.*)[\.]', string)
    if m:
        # This is some ugly washing of str -> float -> int via regex.
        quantity = m.group('match')
    else:
        quantity = string

    try:
      quantity = int(quantity)
    except Exception as e:
      pass

    return quantity

def standardize_units(quantity, unit):
    # This will return unit in ml or g
    match unit:
      case 'tbsp':
        return (quantity*5, 'ml')
      case 'tsp':
        return (quantity*15, 'ml')
      case ('cups' | 'cup'):
        return (quantity*235, 'ml')
      case 'dl':
        return (quantity*100, 'ml')
      case 'l':
        return (quantity*1000, 'ml')
      case 'pint':
        return (quantity*473, 'ml')
      case 'oz':
        return (quantity*29.5, 'ml')
      case 'kg':
        return (quantity*1000, 'g')
      case 'hg':
        return (quantity*100, 'g')
      case 'g':
        return (quantity, 'g')
      case _:
        import pdb; pdb.set_trace()
        print("Hm?")

def combine_units(units, form):
  # Get X ml or g
  if form == 'g':
    # Combine to kg and g
    kg = math.floor(units/1000)
    units = units - 1000*kg
    g = units
    string = ''
    if kg > 0:
        string = f'{kg}kg'
        if g:
            string = string + ', '
    if g > 0:
        string = string + f'{g}g'
    return string
  elif form == 'ml':
    # Combine to l, dl, tbsp, tsp
    liters = math.floor(units/1000)
    units = units-1000*liters
    dl = math.floor(units/100)
    units = units-100*dl
    tbsp = math.floor(units/15)
    units = units-tbsp*15
    tsp = math.floor(units/5)
    units = units-tsp*5
    pinch = units

    string = ""
    if liters > 0:
      string = f'{liters}l'
      if any([dl, tbsp, tsp, pinch]):
        string = string + ", "
    if dl > 0:
      string = string + f'{dl}dl'
      if any([tbsp, tsp, pinch]):
        string = string + ", "
    if tbsp > 0:
      string = string + f'{tbsp}tbsp'
      if any([tsp, pinch]):
        string = string + ", "
    if tsp > 0:
      string = string + f'{tsp}tsp'
      if pinch > 0:
        string = string + ", "
    if pinch > 0:
      string = string + f'{pinch}pinch'
    
    return string
  else:
    return f'{units} {form}'

# This one should be put into the ShoppingList class
def merge_ingredients(ingredients_list):
    for item in ingredients_list:
        if len(ingredients_list[item]) > 1:
            # There are multiple elements here
            sum_units = 0
            form = ''
            for quantity, unit in ingredients_list[item]:
                if unit:
                    sum_units = sum_units + standardize_units(quantity, unit)
                if form != '' and unit in ['l', 'dl', 'tbsp', 'tsp', 'cups', 'pint', 'oz']:
                    form = 'ml'
                elif form != '':
                    form = 'g'
            ingredients_list[item] = (sum_units, form)
        else:
          ingredients_list[item] = ingredients_list[item][0]


def get_ingredients(recipe):
    ingredients = {}
    for item in recipe['ingredients']:
        if item['type'] == 'ingredient':
            quantity = convert_str_to_int(item['quantity'])
            name = item['name']
            if name not in ingredients:
                ingredients[item['name']] = [(quantity, item['units'])]
            else:
                ingredients[item['name']].append((quantity, item['units']))

    return merge_ingredients(ingredients)


class RecipeTree():
  def find_recipes():
    # Do a tree walk and list all .cook files and what folders they are located in.
    # This should perhaps be turned into a structure of some sort, so that it is
    # easy to take a look at it in the webbrowser?
    print("Hej")

  def __repr__(self):
    # Print the tree
    print("Hej")

  def _populate_tree(self):
    # Populate items in this class
    print("Hej")


class CookCLI():
  def __init__(self):
    # Do something
    print("Hej")
  def __enter(self):
    # If you want to use a contextmanager style
    print("Hej")
  def __exit__(self):
    # If you want to use a contextmanager style
    print("Hej")
