import google.generativeai as genai
import sqlite3
import os
from dotenv import load_dotenv
import re
import time

load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    raise ValueError("API_KEY is missing. Please check your .env file.")

genai.configure(api_key=API_KEY)


previous_recipes = set()


def get_total_calories_from_recipe(recipe_text):
    """
    Extracting calories from a recipe using different patterns.
    """
    patterns = [
        r"Total Calories:\s*Approximately\s*(\d+)\s*calories",
        r"Total Calories:\s*(\d+)\s*calories",
        r"Total Calories:\s*Approximately\s*(\d+)\s*Kcal",
        r"Total Calories:\s*(\d+)\s*Kcal",
        r"Total Calories.*?(\d+)\s*(calories|Kcal)",
    ]

    for pattern in patterns:
        match = re.search(pattern, recipe_text, re.IGNORECASE)
        if match:
            return int(match.group(1))

    numbers = re.findall(r"\d+", recipe_text)
    if numbers:
        return int(numbers[-1])

    return 0


def generate_recipe(ingredients, username):
    """
    Create a new recipe for the user and suggest it until he accepts it.
    """
    global previous_recipes

    while True:
        prompt = f"Create a detailed recipe with the following ingredients: {ingredients}. Include the dish name, steps, cooking time, and estimated calories for each ingredient. After that, include the total calories of the dish, calculated based on the ingredients provided."

        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)

            if not response or not response.text:
                print("❌ Unable to create recipe, trying again...")
                continue

            recipe_text = response.text.strip()
            if recipe_text in previous_recipes:
                print("\n⚠️ Duplicate recipe detected, generating a new one...\n")
                continue

            previous_recipes.add(recipe_text)

            total_calories = get_total_calories_from_recipe(recipe_text)
            print(f"\nEstimated Calories from Recipe: {total_calories} Kcal")

            print("\n🍽️ Suggested Recipe:")
            print(recipe_text)

            # If extraction of calories fails, ask the user to enter them manually
            if total_calories == 0:
                try:
                    total_calories = int(
                        input(
                            "Could not automatically detect calories. Please enter the total calories manually: "
                        )
                    )
                except ValueError:
                    print("Invalid input. Calories set to 0.")
                    total_calories = 0

            confirm = (
                input(
                    "\nWould you like to apply this recipe to your calorie intake? (yes/no): "
                )
                .strip()
                .lower()
            )

            if confirm == "yes":
                update_user_calories(username, total_calories)
                print(
                    f"\n✅ Recipe applied! {total_calories} Kcal added to your total intake.\n"
                )
                time.sleep(1) 
                view_remaining_calories(username)
                break

            else:
                print("\n🔄 Suggesting a new recipe...\n")
                time.sleep(1)

        except Exception as e:
            print(f"❌ Error generating recipe: {str(e)}")
            return


def update_user_calories(username, total_calories):
    """
    Update the users consumed calories.
    """
    if total_calories == 0:
        print("⚠️ No calories detected. Skipping update.")
        return

    try:
        conn = sqlite3.connect("tutorial.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT total_calories, consumed_calories FROM users WHERE username = ?",
            (username,),
        )
        row = cursor.fetchone()

        if row is None:
            print(
                f"⚠️ User {username} not found. Make sure the user exists in the database."
            )
            return

        total_calories_db, consumed_calories = row
        consumed_calories = consumed_calories or 0

        new_consumed = consumed_calories + total_calories
        new_remaining = total_calories_db - new_consumed

        cursor.execute(
            """UPDATE users SET consumed_calories = ? WHERE username = ?""",
            (new_consumed, username),
        )

        conn.commit()
        conn.close()

        print(
            f"✅ Calories updated successfully! New consumed: {new_consumed} Kcal, Remaining: {new_remaining} Kcal"
        )

    except sqlite3.Error as e:
        print(f"❌ Database error: {str(e)}")


def view_remaining_calories(username):
    """
    Display the user's remaining calories
    """
    try:
        conn = sqlite3.connect("tutorial.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT total_calories, consumed_calories FROM users WHERE username = ?",
            (username,),
        )
        row = cursor.fetchone()

        if row:
            total_calories, consumed_calories = row
            remaining_calories = total_calories - (consumed_calories or 0)
            print(f"\n📊 You have {remaining_calories:.2f} Kcal remaining for today.\n")
        else:
            print("⚠️ User not found!")

        conn.close()
    except sqlite3.Error as e:
        print(f"❌ Database error: {str(e)}")
