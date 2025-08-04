# goat_score_calculator.py
# Load goat_top_10_full_data.json and calculate final scores
# Fill in your analysis or visualization logic here
import json

with open("goat_top_10_full_data.json") as f:
    data = json.load(f)

for player in data:
    print(f"{player['name']}: Context Adjusted Data Available")
