import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "modules")))

from risk_manager import add_risk, list_risks, search_risk
from safety_recommendations import get_recommendations
from report_generator import generate_report
from graph_generator import plot_risks

def main_options():
    while True:
        print("\nCivil Defence Safety Tracker - Menu")
        print("1. Add a new risk")
        print("2. List all recorded risks")
        print("3. Search for a risk by location")
        print("4. Get safety recommendations")
        print("5. Generate a report")
        print("6. Plot risks chart")
        print("0. Exit")
        
        choice = input("\n Enter your choice: ").strip()
        if not choice :
            print("Error: no input providid . Please enter a vaild option  ")
            continue
        
        try:
            if choice == "1":
                risk_type = input("Enter risk type (e.g., fire, flood, earthquake): ")
                level = input("Enter risk level (high, medium, low): ")
                location = input("Enter location: ")
                date = input("Enter date (YYYY-MM-DD): ")
                add_risk(risk_type, level, location, date)
                print("Risk added successfully!")

            elif choice == "2":
                print("\nRecorded Risks:")
                list_risks()

            elif choice == "3":
                location = input("Enter location to search for risks: ")
                search_risk(location)

            elif choice == "4":
                risk_type = input("Enter risk type to get recommendations: ")
                recommendations = get_recommendations(risk_type)
                print("\nSafety Recommendations:")
                for rec in recommendations:
                    print(f"- {rec}")

            elif choice == "5":
                print("Generating report...")
                generate_report()
                print("Report generated successfully!")

            elif choice == "6":
                print("Generating risk chart...")
                plot_risks()
                print("Risk chart displayed successfully!")

            elif choice == "0":
                print("Exiting program. Have a safe day!")
                break

            else:
                print("Invalid choice! Please select a valid option.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_options()
