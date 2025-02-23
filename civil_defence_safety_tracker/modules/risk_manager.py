

RISK_FILE = "risks.txt"

def add_risk(risk_type, level, location, date):
    """
    Adds a new risk entry to the risk file.

    Args:
        risk_type (str): The type of risk (e.g., "Fire", "Flood").
        level (str): The severity level of the risk (e.g., "High", "Medium", "Low").
        location (str): The location of the risk.
        date (str): The date of occurrence (format: YYYY-MM-DD).

    Returns:
        None

    Example:
        add_risk("Fire", "High", "jeddah", "2024-02-25")
    """



    with open(RISK_FILE, "a", encoding="utf-8") as file:
        file.write(f"{risk_type},{level},{location},{date}\n")
    print("Risk has been recorded successfully!")

def list_risks():
    """
    Lists all recorded risks from the risk file.

    Returns:
        None

    Example:
        list_risks()
        # Output:
        # Recorded Risks:
        # - Fire, High, jeddah, 2024-02-25
    """

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
    """
    Searches for risks recorded in a specific location.

    Args:
        location (str): The location to search for risks.

    Returns:
        None

    Example:
        search_risk("jeddah")
        # Output:
        # Risks found in jeddah:
        # - Fire, High, jeddah, 2024-02-25
    """
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
