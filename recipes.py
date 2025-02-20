from logging import exception
from file_manager import load_data, save_data
from tabulate import tabulate

class Recipe:
    def __init__(self,user):
        self.recipes=load_data("dataStorage/recipes.json")
        self.user = user

    def add_recipe(self):


        print("\n--- Add a New Recipe ---")
        name = input("Enter recipe name: ").lower()
        for r in self.recipes:
            if r["name"] == name:
                raise ValueError("Recipe Name Already Exists")

        ingredients = input("Enter ingredients (comma-separated): ").lower().split(",")
        steps = input("Enter steps: ")
        calories = input("Enter calories: ")

        new_recipe = {
            "name": name,
            "ingredients": [i for i in ingredients],
            "steps": steps,
            "calories": calories,
            "user": self.user
        }

        self.recipes.append(new_recipe)
        save_data("dataStorage/recipes.json", self.recipes)

        print(f"'{name}' Recipe is added successfully!")

    def Display_AllRecipes(self):
        if not self.recipes:
            print("No recipes available to delete.")
            return

        print("\n--- Displaying All Recipes ---")
        table = []
        header = ["#", "Name", "Ingredients", "Steps", "Calories", "User"]

        for i, recipe in enumerate(self.recipes, start=1):
            table.append([i, recipe['name']
                             , ", ".join(recipe['ingredients'])
                             , recipe['steps']
                             , recipe['calories']
                             , recipe['user']])
        print(tabulate(table, headers=header, tablefmt="fancy_grid"))


    def Display_MyRecipes(self):
        if not self.recipes:
            print("No recipes available to delete.")
            return
        found = False
        print("\n--- Displaying My Recipes ---")
        table = []
        header = ["#", "Name", "Ingredients", "Steps", "Calories", "User"]
        for i, r in enumerate(self.recipes, start=1):
            if r['user'] == self.user:
                found = True
                table.append([i, r['name']
                                 , ", ".join(r['ingredients'])
                                 , r['steps']
                                 , r['calories']
                                 , r['user']])
        if found:
            print(tabulate(table, headers=header, tablefmt="fancy_grid"))
        else:
            raise ValueError("You have not added any recipes yet.")


    def search_for_recipes(self):
        if not self.recipes:
            print("No recipes available .")
            return

        try:
            c = int(input("Do you want to search by (1) the name of the recipe or (2) by ingredients (comma-separated): "))
        except ValueError:
            print("You did not enter a number.")
            return

        if c == 1:
            name_of_recipe = input("Enter recipe name: ").lower()

            found = False
            table = []
            header = ["#", "Name", "Ingredients", "Steps", "Calories", "User"]
            for i, r in enumerate(self.recipes, start=1):
                if name_of_recipe in r["name"].lower():
                    found = True
                    table.append([i, r['name']
                                     , ", ".join(r['ingredients'])
                                     , r['steps']
                                     , r['calories']
                                     , r['user']])

            if found:
                print(tabulate(table, headers=header, tablefmt="fancy_grid"))
            else:
                raise ValueError("no recipes yet.")

        elif c == 2:
            ingredients = [ingredient.strip().lower() for ingredient in
                           input("Enter ingredients (comma-separated): ").split(",")]

            found = False
            table = []
            header = ["#", "Name", "Ingredients", "Steps", "Calories", "User"]
            for i, r in enumerate(self.recipes, start=1):
                if any(ingredient in ' '.join([i.lower() for i in r["ingredients"]]) for ingredient in ingredients):
                    found = True
                    table.append([i, r['name']
                                     , ", ".join(r['ingredients'])
                                     , r['steps']
                                     , r['calories']
                                     , r['user']])

                if found:
                    print(tabulate(table, headers=header, tablefmt="fancy_grid"))
                else:
                    raise ValueError("no recipes yet.")

            if not found:
                raise exception("No recipes found with those ingredients.")

        else:
            raise ValueError("Invalid choice. Please enter 1 or 2.")


    def edit_delete_recipe(self):
            print("\n--- Editing Recipe ---")
            e = int(input("Do you want to edit or delete a recipe?\n(1) Edit\n(2) Delete\nChoice: "))

            if e == 1:
                name = input("Enter the name of the recipe you want to edit: ").strip().lower()
                found = False

                for r in self.recipes:
                    if r["name"].lower() == name:
                        found = True
                        c = int(input("What do you want to change:\n"
                                      "(1) Name\n"
                                      "(2) Ingredients\n"
                                      "(3) Steps\n"
                                      "(4) Calories\n"
                                      "(5) Edit Everything\n"
                                      "Choice: "))

                        if c == 1:
                            r["name"] = input("Enter new recipe name: ").strip().title()
                        elif c == 2:
                            r["ingredients"] = [i.strip().title() for i in
                                                input("Enter new ingredients (comma-separated): ").split(",")]
                        elif c == 3:
                            r["steps"] = input("Enter new steps: ")
                        elif c == 4:
                            r["calories"] = input("Enter new calories: ")
                        elif c == 5:
                            r["name"] = input("Enter new recipe name: ")
                            r["ingredients"] = [i.strip().title() for i in
                                                input("Enter new ingredients (comma-separated): ").split(",")]
                            r["steps"] = input("Enter new steps: ")
                            r["calories"] = input("Enter new calories: ")

                        save_data("dataStorage/recipes.json", self.recipes)
                        print(f" Recipe '{r['name']}' updated successfully!\n")
                        break

                if not found:
                    print("Recipe not found.")

            elif e == 2:
                if not self.recipes:
                    print("No recipes available to delete.")
                    return

                name = input("Enter the name of the recipe you want to delete: ").lower()
                found_recipe = None

                for r in self.recipes:
                    if r["name"].lower() == name:
                        found_recipe = r
                        break
                if found_recipe:
                    confirm = input(
                        f"Are you sure you want to delete '{found_recipe['name']}'? (yes/no): ").lower()
                    if confirm == "yes":
                        self.recipes.remove(found_recipe)
                        save_data("dataStorage/recipes.json", self.recipes)
                        print(f"Recipe '{found_recipe['name']}' deleted successfully!\n")
                    else:
                        print("Deletion cancelled. ")


                else:
                    print("Recipe not found.")





