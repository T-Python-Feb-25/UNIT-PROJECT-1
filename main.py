from users import User
from recipes import Recipe
from calorie_tracker import log_meal, view_meal

def main():
    user_m = User()
    while True:
        try:

            print("\nWelcome to RecipeFit!")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                user_m.register()
            elif choice == '2':
                if user_m.login():
                    current_user = user_m.current_user

                    recipe_manager = Recipe(current_user)

                    while True:
                        print("\nWhat would you like to do?")
                        print("1. Add a recipe")
                        print("2. display all recipes")
                        print("3. display my recipes")
                        print("4. search for a recipe")
                        print("5. edit or delete a recipe")
                        print("6. log your meals for today to track your calories")
                        print("7. view your meals")
                        print("8. exit ")

                        action = input("Enter your choice: ")

                        if action == '1':
                            recipe_manager.add_recipe()
                        elif action == '2':
                            recipe_manager.Display_AllRecipes()

                        elif action == '3':
                            recipe_manager.Display_MyRecipes()
                        elif action == '4':
                            recipe_manager.search_for_recipes()
                        elif action == '5':
                            recipe_manager.edit_delete_recipe()
                        elif action == '6':
                            log_meal(current_user)
                        elif action == '7':
                            view_meal(current_user)
                        elif action == '8':
                            print("Goodbye!")
                            break
                        else:
                            print("Invalid choice. Please choose again.")
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose again.")
        except ValueError as e:
            print(e)
if __name__ == "__main__":
    main()

