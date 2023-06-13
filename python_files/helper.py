from pprint import pprint #remove this before commit
import re


def print_metadata(metadata):
    if not metadata:
        return
    print("Metadata!")

def print_ingredients(ingredients):
    if not ingredients:
        return
    
    # Print header
    print("Ingredients:")

    # Find longest name, so that formatting can be based on that
    max_len_name = max([len(item['name']) for item in ingredients])
    for item in ingredients:
        if item['type'] == 'ingredient':
            print(f'    {item["name"].ljust(max_len_name, " ")}    {item["quantity"]} {item["units"]}')
        else:
            # This is unexpected. Log this occurance!
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            with open('log.log') as file:
                file.write(ingredients, encoding='UTF-8')

def print_steps(steps):
    if not steps:
         return
    print("Steps:")
    index = 1
    time = 0
    for step in steps:
        text = []
        cookware = []
        ingredient = []
        timer = []

        for sub_step in step:
            #if index == 5:
             # import pdb; pdb.set_trace()
            match sub_step['type']:
                case 'text':
                    text.append(sub_step['value'])
                case 'cookware':
                    text.append(sub_step['name'])
                    quantity = sub_step.get("quantity", None)
                    if quantity:
                        cookware.append(f'{sub_step["name"]}: {quantity}')
                    else:
                        cookware.append(sub_step["name"])
                case 'ingredient':
                    text.append(sub_step['name'])
                    ingredient.append(f'{sub_step["name"]}: {sub_step["quantity"]} {sub_step["units"]}')
                case 'timer':
                    m = re.match('(?P<match>.*)[\.]', sub_step['quantity'])
                    if m:
                        # This is some ugly washing of str -> float -> int via regex.
                        quantity = m.group('match')
                    else:
                        quantity = sub_step['quantity']
                    time = time + int(quantity)
                    text.append(f'{quantity} {sub_step["units"]}')
                    timer.append((quantity, sub_step['units']))

        # Print step
        print(f'     {index}. {"".join(text)}')
        # Print cookware
        if cookware:
            print(f'        [{"; ".join(cookware)}]')
        # Print ingredients
        if ingredient:
            print(f'        [{"; ".join(ingredient)}]')
        else:
            print(f'        [-]')
        index = index + 1

    print()
    print(f'Estimated time: {time}')
    
    

def print_recipe(recipe):
    print_metadata(recipe['metadata'])
    print()
    print_ingredients(recipe['ingredients'])
    print()
    print_steps(recipe['steps'])
    print()

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
