
# 🏀 Undisputed GOAT Score — A Data-Driven Formula to Settle the Debate

This project ranks the Top 10 Greatest NBA Players of All Time using a transparent, stat-based scoring system.

## 🧠 What Makes This Different?

Unlike most debates, this formula removes bias by combining **advanced stats**, **playoff performance**, and a **context-aware teammate help index**.

### 🧮 The Formula Breakdown

| Category             | Max Points | Description |
|----------------------|------------|-------------|
| 🧱 Career Contribution | 25 pts     | Longevity, VORP, Win Shares, Games |
| 🚀 Peak Performance    | 20 pts     | Best 5-year average PER & TS% |
| 🔥 Playoff Dominance   | 30 pts     | Playoff WS, Finals MVPs, Championships |
| 🏅 Accolades           | 15 pts     | MVPs, All-NBA, Scoring Titles, DPOY |
| ⚖️ Context Adjustment  | ±10 pts    | Opponent SRS, Teammate Help Index (THI), Era Bonus |

### 🧩 Teammate Help Index (THI)

THI combines:
- **AST**: Avg. All-Star Teammates per playoff year
- **TAI**: Avg. Win Shares of top teammates
- **LSI**: Hall of Fame / Top 75 / All-NBA teammate legacy

## 📊 Top 10 GOATs (Context Adjusted)

All calculations are in [`goat_top_10_full_data.json`](./goat_top_10_full_data.json). You can use the included scripts to generate:

- 🟩 Score breakdowns
- 📈 Charts
- 🧾 Player comparisons

## 🛠 Files Included

- `goat_top_10_full_data.json` – all scoring inputs per player
- `goat_score_calculator.py` – script to generate scores
- `README.md` – this file

## 📜 License

MIT — Open source, modify freely.
