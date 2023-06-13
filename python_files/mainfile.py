#!C:\Users\Gustaf\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe

from cooklang import *
import sys
from helper import print_recipe

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
    if  len(sys.argv) < 3 and command != 'server':
        print('Too few arguments')
        early_exit = True
        
    if early_exit:
        print()
        print_help()
        exit(-1)

    match command:
        case 'seed':
            # seed: populate the RecipeTree($PWD)'''
            print("Seed!")
            path = sys.argv[2]
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
            
            match sub_cmd:
                case 'read':
                    # Handle read
                    recipe = parseRecipe(sys.argv[3])
                    print_recipe(recipe)
                case _:
                    print("Everything except read")
        case 'shopping-list':
            '''
            shopping-list <any number of recipe paths>:
            Loops through the ingredients in the recipes and adds them to a shopping list
            Then prints how many of each item, and in what section
            '''
            print("Shopping list printing")
            recipe_paths = []
            index = 2
            while sys.argv[index]:
                recipe_paths.append(sys.argv[index])
                index = index + 1
            print(f'Got {index-2} recipes!')
        case 'server':
            '''
            server:
                Start a webserver. Find out if you want to use FLASK or if there exists something better.
            '''
            print("This is gonna be a tricky one. Starting server!")
    
    # Handle argparse here, and create basic structure
    # Use library files for read, shoppingcart etc for recipe. That should be linked to the recipe
