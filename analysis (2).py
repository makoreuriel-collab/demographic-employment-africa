# ============================================================
# Project: Demographics & Youth Employment in Africa
# Data:    World Bank WDI + ILO estimates
# Charts:  1. Population growth vs youth unemployment scatter
#          2. Youth population vs formal jobs gap (2000–2040)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# ── DATA ────────────────────────────────────────────────────
# Youth unemployment — World Bank: SL.UEM.1524.ZS (% of youth labour force)
# Population growth  — World Bank: SP.POP.GROW    (annual %)
# Reference year: approx. 2021–2022

country_data = {
    "Country": [
        "South Africa", "Nigeria", "Egypt", "Kenya", "Ethiopia",
        "Ghana", "Tanzania", "Algeria", "Morocco", "Senegal",
        "Rwanda", "Zambia",
        "India", "Brazil", "Germany"                   # benchmarks
    ],
    "Region": [
        "Africa", "Africa", "Africa", "Africa", "Africa",
        "Africa", "Africa", "Africa", "Africa", "Africa",
        "Africa", "Africa",
        "Benchmark", "Benchmark", "Benchmark"
    ],
    "Youth_Unemployment_pct": [
        63.9, 13.4, 27.3, 13.0,  3.5,
        13.3,  4.9, 28.1, 24.8,  8.5,
        20.7, 18.8,
        23.2, 18.0,  5.8
    ],
    "Pop_Growth_pct": [
        1.4, 2.5, 1.7, 2.2, 2.5,
        2.1, 3.0, 1.5, 1.0, 2.7,
        2.3, 2.8,
        0.7, 0.7, 0.1
    ]
}

# Time series: Sub-Saharan Africa youth population vs estimated formal jobs
# Sources: World Bank, ILO, UNDP projections
time_series = {
    "Year":               [2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040],
    "Youth_Population_mn":[195,  224,  261,  306,  360,  420,  486,  557,  630],
    "Formal_Jobs_mn":     [48,   58,   70,   83,   95,   109,  124,  139,  155]
}

df = pd.DataFrame(country_data)
ts = pd.DataFrame(time_series)

africa     = df[df["Region"] == "Africa"].copy()
benchmarks = df[df["Region"] == "Benchmark"].copy()

# ── CHART 1: Scatter — pop growth vs youth unemployment ──────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Demographics & Youth Employment Gap in Africa", fontsize=14, fontweight="bold")

ax1 = axes[0]

for _, row in africa.iterrows():
    ax1.scatter(row["Pop_Growth_pct"], row["Youth_Unemployment_pct"],
                color="#1a6e5c", s=80, zorder=3)
    ax1.annotate(row["Country"], (row["Pop_Growth_pct"], row["Youth_Unemployment_pct"]),
                 textcoords="offset points", xytext=(5, 3), fontsize=7, color="#1a6e5c")

for _, row in benchmarks.iterrows():
    ax1.scatter(row["Pop_Growth_pct"], row["Youth_Unemployment_pct"],
                color="#aaaaaa", s=80, marker="D", zorder=3)
    ax1.annotate(row["Country"], (row["Pop_Growth_pct"], row["Youth_Unemployment_pct"]),
                 textcoords="offset points", xytext=(5, 3), fontsize=7, color="#888888")

# Reference lines to create quadrants
ax1.axhline(15, color="#e05c2a", linestyle="--", linewidth=1.0, alpha=0.6, label="15% unemployment")
ax1.axvline(2.0, color="#e8a838", linestyle=":",  linewidth=1.0, alpha=0.6, label="2% pop. growth")

ax1.set_xlabel("Annual Population Growth Rate (%)")
ax1.set_ylabel("Youth Unemployment Rate (%)")
ax1.set_title("Population Growth vs.\nYouth Unemployment", fontweight="bold")
ax1.legend(fontsize=8)
ax1.spines[["top", "right"]].set_visible(False)

# ── CHART 2: Area chart — youth population vs jobs gap ───────
ax2 = axes[1]

ax2.fill_between(ts["Year"], ts["Youth_Population_mn"],
                 color="#1a6e5c", alpha=0.25, label="Youth Population (15–24)")
ax2.plot(ts["Year"], ts["Youth_Population_mn"], color="#1a6e5c", linewidth=2)

ax2.fill_between(ts["Year"], ts["Formal_Jobs_mn"],
                 color="#e05c2a", alpha=0.35, label="Estimated Formal Jobs")
ax2.plot(ts["Year"], ts["Formal_Jobs_mn"], color="#e05c2a", linewidth=2, linestyle="--")

# Label the gap at 2040
gap = ts.iloc[-1]["Youth_Population_mn"] - ts.iloc[-1]["Formal_Jobs_mn"]
ax2.annotate(
    f"~{gap:.0f}M gap\nby 2040",
    xy=(2040, ts.iloc[-1]["Formal_Jobs_mn"] + gap / 2),
    xytext=(2026, 430),
    arrowprops=dict(arrowstyle="->", color="#333"),
    fontsize=8.5, color="#333"
)

# Shade projected years
ax2.axvspan(2024, 2040, alpha=0.05, color="#888888")
ax2.text(2025, 20, "Projected →", fontsize=7.5, color="#888888", style="italic")

ax2.set_xlabel("Year")
ax2.set_ylabel("Millions of People")
ax2.set_title("Africa's Youth Population vs.\nFormal Jobs Created", fontweight="bold")
ax2.legend(fontsize=9)
ax2.set_xlim(2000, 2040)
ax2.spines[["top", "right"]].set_visible(False)

plt.tight_layout()

# ── SAVE ────────────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/demographic_employment_analysis.png", dpi=150, bbox_inches="tight")
print("Saved: outputs/demographic_employment_analysis.png")
plt.show()

# ── SUMMARY ─────────────────────────────────────────────────
print("\n── Key Numbers ─────────────────────────────────────")
print(f"Avg youth unemployment (Africa):   {africa['Youth_Unemployment_pct'].mean():.1f}%")
print(f"Avg population growth  (Africa):   {africa['Pop_Growth_pct'].mean():.1f}%")
print(f"Projected youth-jobs gap by 2040:  ~{gap:.0f} million people")
worst = africa.loc[africa["Youth_Unemployment_pct"].idxmax()]
print(f"Highest youth unemployment:        {worst['Country']} ({worst['Youth_Unemployment_pct']:.1f}%)")
