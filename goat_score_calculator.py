import json

def normalize(val, max_val):
    return round((val / max_val) * 10, 2)

def calculate_goat_score(player):
    # 1. Career Contribution (25 pts)
    career = min((player["vorp"] * 1.25) + (player["ws"] * 1.0) + (player["games"] / 100), 25)

    # 2. Peak Performance (20 pts)
    peak = min(((player["peak_per"] - 15) * 1.5) + ((player["peak_ts"] - 0.55) * 100), 20)

    # 3. Playoff Dominance (30 pts)
    playoffs = min((player["playoff_ws"] * 1.25) + (player["finals_mvps"] * 4) + (player["championships"] * 2.5), 30)

    # 4. Accolades (15 pts)
    accolades = min(
        player["mvp"] * 3 +
        player["dpoy"] * 1.5 +
        player["all_nba_1st"] * 1 +
        player["scoring_titles"] * 0.5, 15
    )

    # 5. Teammate Help Index (THI → Context Penalty)
    ast = normalize(player["AST"], 3.0)
    tai = normalize(player["TAI"], 20)
    lsi = normalize(player["LSI"], 6)
    thi = ast + tai + lsi  # Max 30

    # New: Era Difficulty Index (EDI) Adjustment
    edi = player.get("era_difficulty", 5)  # Default neutral era if not defined
    context = (player["opp_srs"] * 0.5) - (thi * 0.3) + ((edi - 5) * 0.75)
    context = max(min(context, 10), -10)

    total = round(career + peak + playoffs + accolades + context, 2)

    return {
        "name": player["name"],
        "GOAT Score": total,
        "Career": round(career, 2),
        "Peak": round(peak, 2),
        "Playoffs": round(playoffs, 2),
        "Accolades": round(accolades, 2),
        "THI": round(thi, 2),
        "Context Adj.": round(context, 2)
    }

# === MAIN EXECUTION ===
if __name__ == "__main__":
    with open("goat_top_10_full_data.json") as f:
        players = json.load(f)

    scores = [calculate_goat_score(p) for p in players]
    ranked = sorted(scores, key=lambda x: x["GOAT Score"], reverse=True)

    print("\n🏀 GOAT Rankings (Era-Adjusted):\n")
    for i, p in enumerate(ranked, 1):
        print(f"{i}. {p['name']} — {p['GOAT Score']}/100")
        print(f"   Career: {p['Career']}, Peak: {p['Peak']}, Playoffs: {p['Playoffs']}, "
              f"Accolades: {p['Accolades']}, Context: {p['Context Adj.']}, THI: {p['THI']}")
        print()
