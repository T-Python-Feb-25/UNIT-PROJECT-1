
from users import User
from recipes import Recipe
from calorie_tracker import log_meal, view_meal, edit_delete_meal, plot_calories
from colorama import Fore
import pyfiglet





def main():
    user_m = User()
    while True:
        try:
            banner = pyfiglet.figlet_format("RecipeFit")
            print(Fore.MAGENTA + banner+ Fore.RESET)

            print("=" * 40)
            print(Fore.MAGENTA + "Welcome to RecipeFit! Choose an option:"+Fore.RESET)
            print("=" * 40)
            print(Fore.BLUE + "1. Register")
            print(Fore.BLUE + "2. Login")
            print(Fore.RED + "3. Exit")

            choice = input(Fore.CYAN + "Enter your choice: " + Fore.RESET)

            if choice == '1':
                user_m.register()
            elif choice == '2':
                if user_m.login():
                    current_user = user_m.current_user
                    recipe_manager = Recipe(current_user)

                    while True:
                        try:
                            print("\n" + Fore.MAGENTA + "-" * 40)
                            print(Fore.YELLOW + "What would you like to do?")
                            print(Fore.MAGENTA + "-" * 40)
                            print(Fore.CYAN + "1. Add a recipe")
                            print(Fore.CYAN + "2. Display all recipes")
                            print(Fore.CYAN + "3. Display my recipes")
                            print(Fore.CYAN + "4. Search for a recipe")
                            print(Fore.CYAN + "5. Edit or delete a recipe")
                            print(Fore.CYAN + "6. Log your meals for today")
                            print(Fore.CYAN + "7. View your meals")
                            print(Fore.CYAN + "8. Edit or delete a meal")
                            print(Fore.CYAN + "9. View calorie intake (past week)")
                            print(Fore.RED + "10. Exit")

                            action = input(Fore.YELLOW + "Enter your choice: " + Fore.RESET)

                            if action == '1':
                                recipe_manager.add_recipe()
                                continue
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
                                edit_delete_meal(current_user)
                            elif action == '9':
                                plot_calories(current_user)
                            elif action == '10':
                                print(Fore.RED + "Goodbye!")
                                break
                            else:
                                print(Fore.RED + "Invalid choice. Please choose again.")

                            input(Fore.YELLOW + "\nPress enter to continue..." + Fore.RESET)
                        except ValueError as e:
                            print(Fore.RED + f"An error occurred: {str(e)}")
                            continue

            elif choice == '3':
                print(Fore.RED + "Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please choose again.")
        except ValueError as e:
            print(Fore.RED + str(e))
            continue

if __name__ == "__main__":
    main()
