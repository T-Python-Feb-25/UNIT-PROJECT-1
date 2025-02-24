def generate_report():
    """
    Generates a risk report from the recorded risks.

    This function reads the risk data from `risks.txt` and generates a formatted
    report in `risk_report.txt`. If no risks are recorded, it displays a message.

    Returns:
        None

    Example:
         generate_report()
        # Output:
        # Risk Report
        # --------------
        # Fire, High, Jeddah, 2024-02-25
    """
    try:
        with open("risks.txt", "r", encoding="utf-8") as file:
            risks = file.readlines()
        if not risks:
            print("No risks recorded to generate a report.")
            return

        with open("risk_report.txt", "w", encoding="utf-8") as report_file:
            report_file.write("Risk Report\n")
            report_file.write("=" * 40 + "\n")
            for risk in risks:
                report_file.write(risk)
        
        print("Risk report has been generated successfully.")
    except FileNotFoundError:
        print("No recorded risks found to generate a report.")
