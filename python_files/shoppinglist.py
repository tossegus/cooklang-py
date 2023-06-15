from helper import combine_units, standardize_units, Ingredient, convert_str_to_int


class ShoppingList:
    def __init__(self):
        self.shopping_list = {}

    def __str__(self):
        string = "Items:\n"
        for item in self.shopping_list:
            elem = self.shopping_list[item]
            new_units = combine_units(elem.quantity, elem.unit)
            string = string + f"{item}: {new_units}\n"
        return string

    def __repr__(self):
        print()
        print(self.__str__)

    @property
    def items(self):
        return self.shopping_list

    def add_recipe(self, recipe):
        self.fill_ingredients(recipe)

    def add_ingredient(self, item, quantity, unit):
        if unit:
            (int_q, int_unit) = standardize_units(quantity, unit)
        else:
            int_q = quantity
            int_unit = unit
        if item not in self.shopping_list:
            self.shopping_list[item] = Ingredient(int_q, int_unit)
        else:
            current = self.shopping_list[item]
            self.shopping_list[item] = Ingredient(
                current.quantity + int_q, current.unit
            )

    def fill_ingredients(self, recipe):
        for item in recipe["ingredients"]:
            if item["type"] == "ingredient":
                quantity = convert_str_to_int(item["quantity"])
                self.add_ingredient(item["name"], quantity, item["units"])
