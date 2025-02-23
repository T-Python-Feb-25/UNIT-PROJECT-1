import getpass
from colorama import Fore, Style
from users import Users
from calorie_tracker import CalorieTracker
from rcipeAPI import generate_recipe
import emoji
import sys

def show_recipe_suggestion(username):
    choice = (
        input(
            "Would you like a recipe suggestion based on the ingredients you have? (yes/no): "
        )
        .strip()
        .lower()
    )

    if choice == "yes":
        user_ingredients = input(
            "Enter the components you have available separated by commas: "
        )
        recipe = generate_recipe(user_ingredients, username)
        print("\nSuggested Recipe:\n", recipe)
    else:
        print(
            emoji.emojize(
                ":wave: Exiting... Have a nice day! :star2:", language="alias"
            )
        )


def show_calorie_tracker(username):
    tracker = CalorieTracker(username)

    while True:
        menu = """
1: Add meal
2: View remaining calories
3: View consumed calories
4: Exit
5: Suggest meal recipe
        """
        print(f"\n Menu:\n {menu}")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                meal_name = input(
                    "Enter meal name (e.g., Breakfast, Lunch, Dinner): "
                ).strip()

                if not meal_name:
                    raise ValueError(
                        Fore.RED
                        + "You did not enter a valid meal name. Please provide a meal name."
                        + Style.RESET_ALL
                    )

                while True:  
                    calorie_input = input(
                        f"Enter your calorie for {meal_name}: "
                    ).strip()

                    if not calorie_input:
                        raise ValueError(
                            Fore.RED
                            + "You did not enter valid calories. Please provide a valid number."
                            + Style.RESET_ALL
                        )

                    try:
                        calorie = int(calorie_input)
                        if calorie <= 0:
                            raise ValueError(
                                Fore.RED
                                + "Calories must be greater than 0."
                                + Style.RESET_ALL
                            )
                        break  

                    except ValueError as e:
                        print(e)  
                        continue  

                tracker.track_meal(meal_name, calorie)

            except ValueError as e:
                print(e)  

        elif choice == "2":
            tracker.remaining_calories()

        elif choice == "3":
            print(f"Consumed calories so far: {tracker.consumed_calories} Kcal")

        elif choice == "4":
            print(emoji.emojize(f"Thank you for using the app! :thumbs_up:"))
            break

        elif choice == "5":
            show_recipe_suggestion(username)
            tracker.update_calories_after_recipe()

        else:
            print(
                Fore.RED
                + "Invalid choice. Please enter a valid option."
                + Style.RESET_ALL
            )  


if __name__ == "__main__":
    print(
        emoji.emojize(
            f"Welcome to the Calorie Tracker and Recipe Generator! :smiling_face_with_smiling_eyes:"
        )
    )
    try:
        
        while True:
                
            choice = input("Do you want to register (1) or login (2)? ").strip()
    
            if choice == "1":
                username = input("Enter username: ").strip()
                name = input("Enter your name: ").strip()
                password = getpass.getpass("Enter your password: ")
                user = Users(username, name, password)
                if user is None or not hasattr(user, "username"):
                    print(Fore.RED + "Registration failed. Please try again." + Style.RESET_ALL)
                    continue
                else:
                    print(Fore.GREEN + "Registration successful!" + Style.RESET_ALL)
                    print(Fore.GREEN + f"Welcome, {name}!" + Style.RESET_ALL)
                    show_calorie_tracker(username)  
                    continue  
    
    
            elif choice == "2":
                username = Users.login()
                if username:
                    print(Fore.GREEN + f"Welcome back, {username}!" + Style.RESET_ALL)
                    show_calorie_tracker(username)
                else:
                    print("Invalid username or password. Try again.")
                    choice = input("Do you want to register (1) or login (2)? ").strip()
                    if choice == "1":
                        username = input("Enter username: ").strip()
                        name = input("Enter your name: ").strip()
                        password = getpass.getpass("Enter your password: ")
                        user = Users(username, name, password)
                        if user is None: 
                            print(Fore.RED + "Registration failed. Please try again." + Style.RESET_ALL)
                            continue
                        else:
                            print(Fore.GREEN + "Registration successful!" + Style.RESET_ALL)
                    elif choice == "2":
                        username = Users.login()
                        if username:
                            print(Fore.GREEN + f"Welcome back, {username}!" + Style.RESET_ALL)
                            show_calorie_tracker(username)
                        else:
                            print(
                                Fore.RED
                                + "Invalid username or password. Exiting..."
                                + Style.RESET_ALL
                            )
    
            else:
                print(Fore.RED + "Invalid choice. Exiting..." + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.RED + "\n❌ Program interrupted by user. Exiting..." + Style.RESET_ALL)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
    
        
    