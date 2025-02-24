# UNIT-PROJECT-1
# Civil Defense Safety Tracker

## Project Overview
Civil Defense Safety Tracker
Project Overview
The Civil Defense Safety Tracker is a command-line application designed to manage and analyze disaster risks. Users can record risks, visualize them in charts, generate reports, and export data to Excel. The program helps in decision-making by tracking and managing different risk types efficiently.


## Features
- **User Authentication**: Users can register and log in securely.
- **Risk Management**: Add, list, search, update, and delete recorded risks.
- **Automated Reports**: Generates risk reports in text and Excel formats.
- **Data Visualization**: Plots risk distributions using bar charts.
- **Email Notifications**: Sends alerts when a high-risk incident is recorded.



## Technologies and Libraries Used
The project is built using **Python** and relies on several key libraries:

- **SQLite3**: Used for storing and managing risk records in a database.
- **matplotlib**: Generates visual representations of risk data.
- **colorama**: Enhances console output with colored text.
- **smtplib & ssl**: Enables sending email notifications securely.
- **collections.Counter**:Data processing

## Installation
To run the project, follow these steps:

1. Clone the repository:
   ```sh
   git clone 
   ```
2. Navigate to the project directory:
   ```sh
   cd civil-defense-safety-tracker
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the application:
   ```sh
   python main.py
   ```

## File Structure
```
|-- civil_defense_safety_tracker/
    |-- modules/
        |-- risk_manager.py
        |-- report_generator.py
        |-- graph_generator.py
        |-- email_sender.py
        |-- safety_recommendations.py
        |-- export_excel.py
    |-- main.py
    |-- risk_data.xlsx
    |-- risk_report.txt
    |-- safety_tracker.db
    |-- risks.txt
    |-- README.md
```

## Usage
- Run `main.py` to start the program.
- Follow on-screen instructions to log in or register.
- Choose options from the menu to manage risks.
- View graphical representations of recorded risk levels.
- Export reports as text or Excel files.

🔹 Scenario for Demonstration 
- Login/Register as a user.
- Add a new risk (Example: "Fire", "High", "Jeddah", "2024-02-25").
- List risks to confirm the data is stored.
- Generate a report and check risk_report.txt.
- Export data to Excel and open risk_data.xlsx.
- Send an email alert about a new risk.
- Plot a risk chart to visualize recorded risk levels.


🔹 Additional Notes
Ensure SMTP settings are configured for email notifications.
The project is structured modularly for better maintainability.
The graph_generator.py uses matplotlib for visual representation.


🔹 Future Enhancements 

- Web-Based Interface for better accessibility.
- AI Risk Prediction based on historical data.
- Integration with APIs for real-time updates.








### NOTE: before submitting the final project, please do the following command:
`pip freeze > requirements.txt` to enable use to know & use the packages used in your project.
