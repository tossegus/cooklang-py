from helper import *

class Recipe():
    def __init__(self, recipe):
        self.metadata = recipe['metadata']
        self.ingredients = recipe['ingredients']
        self.steps = recipe['steps']
        pass

    def __str__(self):
        string = ""
        tmp_str = self.get_metadata_str()
        if tmp_str != "":
            string = string + tmp_str + "\n"
        tmp_str = self.get_ingredients_str()
        if tmp_str != "":
            string = string + tmp_str + "\n"
        tmp_str = self.get_steps_str()
        if tmp_str != "":
            string = string + tmp_str + "\n"
        return string

    def __repr__(self):
        return self.__str__

    def get_metadata_str(self):
        if not self.metadata:
            return ""
        # Print header
        string = "Metadata:\n"

        for key in self.metadata:
            string = string + f'    {key}: {metadata[key]}\n'
        return string

    def get_ingredients_str(self):
        if not self.ingredients:
            return ""
        # Print header
        string= "Ingredients:\n"

        # Find longest name, so that formatting can be based on that
        max_len_name = max([len(item['name']) for item in self.ingredients])
        for item in self.ingredients:
            if item['type'] == 'ingredient':
                quantity = convert_str_to_int(item['quantity'])
                string = string + f'    {item["name"].ljust(max_len_name, " ")}    {quantity} {item["units"]}\n'
            else:
                # This is unexpected. Log this occurance!
                string = string + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
                string += f'Problem with {item["type"]}'
                with open('log.log') as file:
                    file.write(self.ingredients, encoding='UTF-8')
        return string

    def get_steps_str(self):
        if not self.steps:
             return ""
            
        string = "Steps:\n"
        index = 1
        time = 0
        for step in self.steps:
            text = []
            cookware = []
            ingredient = []
            timer = []
    
            for sub_step in step:
                match sub_step['type']:
                    case 'text':
                        text.append(sub_step['value'])
                    case 'cookware':
                        # Strip trailing commas since the followign type of writing is to be expected
                        # "mix [...] with a #blender, allow to settle"
                        text.append(sub_step['name'])
                        quantity = sub_step.get("quantity", None)
                        if quantity:
                            cookware.append(f'{sub_step["name"].strip(",")}: {quantity}')
                        else:
                            cookware.append(sub_step["name"].strip(","))
                    case 'ingredient':
                        text.append(sub_step['name'])
                        quantity = convert_str_to_int(sub_step['quantity'])
                        ingredient.append(f'{sub_step["name"].strip(",")}: {quantity} {sub_step["units"]}')
                    case 'timer':
                        quantity = convert_str_to_int(sub_step['quantity'])
                        time = time + quantity
                        text.append(f'{quantity} {sub_step["units"]}')
                        timer.append((quantity, sub_step['units']))
    
            # Print step
            string= string + f'     {index}. {"".join(text)}\n'
            # Print cookware
            if cookware:
                string = string + f'        [{"; ".join(cookware)}]\n'
            # Print ingredients
            if ingredient:
                string = string + f'        [{"; ".join(ingredient)}]\n'
            else:
                string = string + f'        [-]\n'
            index = index + 1

        string = string + f'\nEstimated time: {time}\n'
        return string
