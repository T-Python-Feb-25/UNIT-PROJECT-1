import matplotlib.pyplot as plt
from collections import Counter

def plot_risks():
    """
    Generates a bar chart displaying the distribution of recorded risks based on their severity levels.

    This function reads risk data from `risks.txt`, counts occurrences of each risk level,
    and plots a bar chart using Matplotlib.

    Returns:
        None

    Example:
        plot_risks()
        # Displays a bar chart with risk levels (Low, Medium, High) and their corresponding counts.
    """
    try:
        with open("risks.txt", "r", encoding="utf-8") as file:
            risks = [line.split(",")[1].strip() for line in file.readlines()]  
        if not risks:
            print("⚠ No risks available to create a chart.")
            return

        risk_counts = Counter(risks)  
        levels = list(set([level.strip().capitalize() for level in risk_counts.keys()]))

        plt.figure(figsize=(6, 4))
        colors = {"Low": "green", "Medium": "orange", "High": "red"} 

        plt.bar(risk_counts.keys(), risk_counts.values(), color=[colors.get(level, "blue") for level in risk_counts.keys()])
        plt.xlabel("Risk Level")
        plt.ylabel("Count")
        plt.title("Risk Distribution")
        plt.ylim(0, max(risk_counts.values()) + 1)  
        plt.show()

    except FileNotFoundError:
        print("No recorded risks found to plot.")
        


   