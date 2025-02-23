from logging import exception
from file_manager import load_data, save_data
from tabulate import tabulate
from colorama import Fore, Style,Back

class Recipe:
    def __init__(self,user):
        self.recipes=load_data("dataStorage/recipes.json")
        self.user = user

    def add_recipe(self):
        """
            Allows the user to add a new recipe.
            Parameters:
                None
            Returns:
                None: The function adds a new recipe with the provided details and updates the recipes list.

            """
        print(Fore.YELLOW + "=" * 40)
        print("--- Add a New Recipe ---")
        print(Fore.YELLOW + "=" * 40)

        name = input(Fore.BLUE+"Enter recipe name: ").lower()
        for r in self.recipes:
            if r["name"] == name:
                raise ValueError(Fore.RED+"Recipe Name Already Exists")

        ingredients = input(Fore.BLUE+"Enter ingredients (comma-separated): ").lower().split(",")
        steps = input(Fore.BLUE+"Enter steps: ")
        calories = input(Fore.BLUE+"Enter calories: ")
        print(Fore.YELLOW + "=" * 40)

        new_recipe = {
            "name": name,
            "ingredients": [i for i in ingredients],
            "steps": steps,
            "calories": calories,
            "user": self.user
        }

        self.recipes.append(new_recipe)
        save_data("dataStorage/recipes.json", self.recipes)

        print(Fore.GREEN+f"'{name}' Recipe is added successfully!")


    def Display_AllRecipes(self):
        """
            Displays all recipes stored in the system.
            Parameters:
                None
            Returns:
                None: If recipes are available, they are displayed in a table format.
                      If no recipes are available, a message is shown.
            """

        if not self.recipes:
            print(Fore.RED+"No recipes available to delete.")
            return

        print(Fore.MAGENTA + "=" * 40)

        print("--- Displaying All Recipes ---")
        print(Fore.MAGENTA + "=" * 40)

        table = []

        header = ["#", "Name", "Ingredients", "Steps", "Calories", "User"]

        for i, recipe in enumerate(self.recipes, start=1):
            table.append([
                Fore.MAGENTA + str(i) + Style.RESET_ALL,
                Fore.MAGENTA + recipe['name'] + Style.RESET_ALL,
                Fore.MAGENTA + ", ".join(recipe['ingredients']) + Style.RESET_ALL,
                Fore.MAGENTA + recipe['steps'] + Style.RESET_ALL,
                Fore.MAGENTA + str(recipe['calories']) + Style.RESET_ALL,
                Fore.MAGENTA + recipe['user'] + Style.RESET_ALL
            ])
        print(tabulate(table, headers=header, tablefmt="fancy_grid"))


    def Display_MyRecipes(self):
        """
            Displays the recipes added by the current user.
            Parameters:
                None
            Returns:
                None: If the user has recipes, they are displayed in a table format.
                      If no recipes are found for the user, an error is raised.
            """
        if not self.recipes:
            print(Fore.RED+"No recipes available to delete.")
            return
        found = False
        print(Fore.MAGENTA + "=" * 40)
        print("--- Displaying My Recipes ---")
        print(Fore.MAGENTA + "=" * 40)

        table = []
        header = ["#", "Name", "Ingredients", "Steps", "Calories", "User"]

        for i, r in enumerate(self.recipes, start=1):
            if r['user'] == self.user:
                found = True
                table.append([
                    Fore.MAGENTA + str(i) + Style.RESET_ALL,
                    Fore.MAGENTA + r['name'] + Style.RESET_ALL,
                    Fore.MAGENTA + ", ".join(r['ingredients']) + Style.RESET_ALL,
                    Fore.MAGENTA + r['steps'] + Style.RESET_ALL,
                    Fore.MAGENTA + str(r['calories']) + Style.RESET_ALL,
                    Fore.MAGENTA + r['user'] + Style.RESET_ALL
                ])
        if found:
            print(tabulate(table, headers=header, tablefmt="fancy_grid"))
        else:
            raise ValueError(Fore.LIGHTRED_EX+"You have not added any recipes yet.")





    def search_for_recipes(self):
        """
           Allows the user to search for recipes by name or ingredients.
           Parameters:
               None
           Returns:
               None: If recipes are found matching the search criteria, they are displayed in a table format.
                     If no recipes match the search, an error is raised.
           """
        if not self.recipes:
            print(Fore.RED+"No recipes available .")
            return

        try:
            c = int(input(Fore.BLUE+"Do you want to search by (1) the name of the recipe or (2) by ingredient: "))
        except ValueError:
            print(Fore.RED+"You did not enter a number.")
            return

        if c == 1:
            name_of_recipe = input(Fore.BLUE+"Enter recipe name: ").lower()

            found = False
            table = []
            header = ["#", "Name", "Ingredients", "Steps", "Calories", "User"]
            for i, r in enumerate(self.recipes, start=1):
                if name_of_recipe in r["name"].lower():
                    found = True
                    table.append([
                    Fore.MAGENTA + str(i) + Style.RESET_ALL,
                    Fore.MAGENTA + r['name'] + Style.RESET_ALL,
                    Fore.MAGENTA + ", ".join(r['ingredients']) + Style.RESET_ALL,
                    Fore.MAGENTA + r['steps'] + Style.RESET_ALL,
                    Fore.MAGENTA + str(r['calories']) + Style.RESET_ALL,
                    Fore.MAGENTA + r['user'] + Style.RESET_ALL
                ])

            if found:
                print(tabulate(table, headers=header, tablefmt="fancy_grid"))
            else:
                raise ValueError(Fore.RED+"no recipes yet.")

        elif c == 2:
            ingredients = [ingredient.strip().lower() for ingredient in
                           input("Enter ingredient: ").split(",")]

            found = False
            table = []
            header = ["#", "Name", "Ingredients", "Steps", "Calories", "User"]
            for i, r in enumerate(self.recipes, start=1):
                if any(ingredient in ' '.join([i.lower() for i in r["ingredients"]]) for ingredient in ingredients):
                    found = True
                    table.append([
                    Fore.MAGENTA + str(i) + Style.RESET_ALL,
                    Fore.MAGENTA + r['name'] + Style.RESET_ALL,
                    Fore.MAGENTA + ", ".join(r['ingredients']) + Style.RESET_ALL,
                    Fore.MAGENTA + r['steps'] + Style.RESET_ALL,
                    Fore.MAGENTA + str(r['calories']) + Style.RESET_ALL,
                    Fore.MAGENTA + r['user'] + Style.RESET_ALL
                ])

            if found:
                print(tabulate(table, headers=header, tablefmt="fancy_grid"))
            else:
                raise ValueError(Fore.RED+"no recipes yet.")

            if not found:
                raise exception(Fore.RED+"No recipes found with those ingredients.")

        else:
            raise ValueError(Fore.RED+"Invalid choice. Please enter 1 or 2.")


    def edit_delete_recipe(self):
        """
            Allows the user to edit or delete an existing recipe.

            Parameters:
                None

            Returns:
                None: The user can edit or delete a recipe. If editing, the user can update various details like the name, ingredients, steps, and calories. If deleting, the recipe is removed from the list.
                """
        print(Fore.MAGENTA + "=" * 40)
        print("\n--- Editing Recipe ---")
        print(Fore.MAGENTA + "=" * 40)

        e = int(input(Fore.BLUE+"Do you want to edit or delete a recipe?\n(1) Edit\n(2) Delete\nChoice: "))

        if e == 1:
            name = input(Fore.BLUE+"Enter the name of the recipe you want to edit: ").strip().lower()
            found = False

            for r in self.recipes:
                if r["name"].lower() == name:
                    found = True
                    c = int(input(Fore.BLUE+"What do you want to change:\n"
                                  "(1) Name\n"
                                  "(2) Ingredients\n"
                                  "(3) Steps\n"
                                  "(4) Calories\n"
                                  "(5) Edit Everything\n"
                                  "Choice: "))

                    if c == 1:
                        r["name"] = input(Fore.BLUE+"Enter new recipe name: ").strip().title()
                    elif c == 2:
                        r["ingredients"] = [i.strip().title() for i in
                                            input(Fore.BLUE+"Enter new ingredients (comma-separated): ").split(",")]
                    elif c == 3:
                        r["steps"] = input(Fore.BLUE+"Enter new steps: ")
                    elif c == 4:
                        r["calories"] = input(Fore.BLUE+"Enter new calories: ")
                    elif c == 5:
                        r["name"] = input(Fore.BLUE+"Enter new recipe name: ")
                        r["ingredients"] = [i.strip().title() for i in
                                            input(Fore.BLUE+"Enter new ingredients (comma-separated): ").split(",")]
                        r["steps"] = input(Fore.BLUE+"Enter new steps: ")
                        r["calories"] = input(Fore.BLUE+"Enter new calories: ")

                    save_data("dataStorage/recipes.json", self.recipes)
                    print(Fore.GREEN+f"Recipe '{r['name']}' updated successfully!\n")
                    break

            if not found:
                print(Fore.RED+"Recipe not found.")

        elif e == 2:
            if not self.recipes:
                print(Fore.RED+"No recipes available to delete.")
                return

            name = input("Enter the name of the recipe you want to delete: ").lower()
            found_recipe = None

            for r in self.recipes:
                if r["name"].lower() == name:
                    found_recipe = r
                    break
            if found_recipe:
                confirm = input(Fore.YELLOW+f"Are you sure you want to delete '{found_recipe['name']}'? (yes/no): ").lower()
                if confirm == "yes":
                    self.recipes.remove(found_recipe)
                    save_data("dataStorage/recipes.json", self.recipes)
                    print(Fore.GREEN+f"Recipe '{found_recipe['name']}' deleted successfully!\n")
                else:
                    print(Fore.RED+"Deletion cancelled. ")


            else:
                print(Fore.RED+"Recipe not found.")





