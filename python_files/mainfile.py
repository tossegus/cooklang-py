#!/usr/bin/env python

from cooklang import *
import sys, os
from helper import get_ingredients
from recipe import Recipe
from shoppinglist import ShoppingList
from recipe_tree import RecipeTree
from server import Server

def print_help():
    print('Usage: mainfile.py [seed|recipe|shopping-list|server] <options>')
    print('seed: <root-path to .cook files>')
    print('recipe: read, ...')
    print('shopping-list: <file1.cook> <file2.cook> ...')
    print('server does not need any arguments')
    print()


if __name__ == "__main__":
    command = sys.argv[1]
    early_exit = False
    if command not in ['seed', 'recipe', 'shopping-list', 'server']:
        print(f'Command "{command}" not found.')
        early_exit = True
    if  len(sys.argv) < 3 and command != 'server' and command != 'seed':
        print('Too few arguments')
        early_exit = True
    if early_exit:
        print()
        print_help()
        exit(-1)

    # Path to this directory
    path = os.getcwd()

    match command:
        case 'seed':
            # seed: populate the RecipeTree($PWD)'''
            # DONE
            tree = RecipeTree(path)
            print(tree)
        case 'recipe':
            '''
            recipe <cmd>,
              read: Print information to terminal
                Metadata: ...

                Ingredients: ...

                Steps: ...
            '''
            if len(sys.argv) < 4:
                print(f'Wrong number of arguments for {command}')
                print_help()
                exit(-1)
            sub_cmd = sys.argv[2]

            recipe = Recipe(parseRecipe(sys.argv[3]))
            
            match sub_cmd:
                case 'read':
                    # Handle read
                    # There is problems with using % to define units in metadata. So don't do that!
                    print(recipe)
                    # DONE
                case _:
                    print("Everything except read")
        case 'shopping-list':
            '''
            shopping-list <any number of recipe paths>:
            Loops through the ingredients in the recipes and adds them to a shopping list
            Then prints how many of each item, and in what section
            '''
            # DONE
            recipe_paths = []
            index = 2
            while index < len(sys.argv):
                recipe_paths.append(sys.argv[index])
                index = index + 1
            print(f'Got {index-2} recipes!')
            ingredients = []
            shopping_list = ShoppingList()
            for path in recipe_paths:
                recipe = parseRecipe(path)
                shopping_list.add_recipe(recipe)
            print(shopping_list)
        case 'server':
            '''
            server:
                Start a webserver. Find out if you want to use FLASK or if there exists something better.
            '''
            print("Server!")
            server = Server(path)
            server.start()
