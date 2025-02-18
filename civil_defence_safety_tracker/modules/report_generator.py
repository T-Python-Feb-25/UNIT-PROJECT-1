def generate_report():
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
