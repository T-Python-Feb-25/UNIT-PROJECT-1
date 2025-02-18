import matplotlib.pyplot as plt
from collections import Counter

def plot_risks():
    try:
        with open("risks.txt", "r", encoding="utf-8") as file:
            risks = [line.split(",")[0] for line in file.readlines()]

        if not risks:
            print(" No risks available to create a chart.")
            return

        risk_counts = Counter(risks)
        plt.figure(figsize=(8, 5))
        plt.bar(risk_counts.keys(), risk_counts.values(), color='skyblue')
        plt.xlabel("Risk Type")
        plt.ylabel("Number of Cases")
        plt.title("Distribution of Recorded Risks")
        plt.show()
    except FileNotFoundError:
        print("No recorded risks found to plot.")
