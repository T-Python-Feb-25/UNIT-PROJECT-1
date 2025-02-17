import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "modules")))

from risk_manager import add_risk, list_risks, search_risk
from safety_recommendations import get_recommendations
from report_generator import generate_report
from graph_generator import plot_risks

parser = argparse.ArgumentParser(description="System for recording and analyzing civil defense risks")

parser.add_argument("--add_risk", nargs=4, metavar=("TYPE", "LEVEL", "LOCATION", "DATE"), help="Add new risks")
parser.add_argument("--list_risks", action="store_true", help="List recorded risks")
parser.add_argument("--search_risk", metavar="LOCATION", help="Find risks in a specific location")
parser.add_argument("--recommend", metavar="TYPE", help="Provide safety recommendations")
parser.add_argument("--generate_report", action="store_true", help="Generate a report for risks")
parser.add_argument("--plot_risks", action="store_true", help="Create a bar chart for risks")

args = parser.parse_args()

if args.add_risk:
    add_risk(*args.add_risk)
elif args.list_risks:
    list_risks()
elif args.search_risk:
    search_risk(args.search_risk)
elif args.recommend:
    print("\n".join(get_recommendations(args.recommend)))
elif args.generate_report:
    generate_report()
elif args.plot_risks:
    plot_risks()
