import os

RISK_FILE = "risks.txt"

def add_risk(risk_type, level, location, date):
    with open(RISK_FILE, "a", encoding="utf-8") as file:
        file.write(f"{risk_type},{level},{location},{date}\n")
    print("Risk has been recorded successfully!")

def list_risks():
    if not os.path.exists(RISK_FILE):
        print(" No recorded risks found.")
        return
    with open(RISK_FILE, "r", encoding="utf-8") as file:
        risks = file.readlines()
    if risks:
        print("\nRecorded Risks:")
        for risk in risks:
            print("- " + risk.strip())
    else:
        print(" No recorded risks found.")

def search_risk(location):
    if not os.path.exists(RISK_FILE):
        print(" No recorded risks found.")
        return
    with open(RISK_FILE, "r", encoding="utf-8") as file:
        risks = [risk.strip() for risk in file.readlines() if location in risk]
    if risks:
        print(f"\nRisks found in {location}:")
        for risk in risks:
            print(f"- {risk}")
    else:
        print(f"No risks found in {location}.")
