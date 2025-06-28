import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Patch
import pandas as pd
from datetime import datetime

# Drupal core versions.
# "version", "release date", "active", "security"
# Some dates are estimates.
data = [
    ["10.3", "20/06/2024", "17/12/2024", "19/06/2025"],
    ["10.4", "17/12/2024", "19/06/2025", "11/12/2025"],
    ["10.5", "19/06/2025", "11/12/2025", "15/06/2026"],
    ["10.6", "11/12/2025", "15/06/2026", "15/12/2026"],
    ["11.0", "02/08/2024", "16/12/2024", "19/06/2025"],
    ["11.1", "16/12/2024", "19/06/2025", "11/12/2025"],
    ["11.2", "19/06/2025", "11/12/2025", "15/06/2026"],
    ["11.3", "11/12/2025", "15/06/2026", "15/12/2026"],
]

# DataFrame.
df = pd.DataFrame(data, columns=["Version", "release_date", "active", "security"])
df["release_date"] = pd.to_datetime(df["release_date"], dayfirst=True)
df["active"] = pd.to_datetime(df["active"], dayfirst=True)
df["security"] = pd.to_datetime(df["security"], dayfirst=True)

# Sort.
df = df.sort_values("release_date", ascending=True)

# Colors.
colors = {
    "active": "green",
    "security": "gold",
    "ended": "red",
    "not_active": "grey",
}
today = datetime.today()

# French month.
french_months = {
    1: "janv.", 2: "févr.", 3: "mars", 4: "avr.", 5: "mai", 6: "juin",
    7: "juil.", 8: "août", 9: "sept.", 10: "oct.", 11: "nov.", 12: "déc."
}
def french_date_formatter(x, pos):
    date = mdates.num2date(x)
    return f"{french_months[date.month]} {date.year}"

# Create graph.
fig, ax = plt.subplots(figsize=(14, 8))

# Create bars.
for _, row in df.iterrows():
    version = row["Version"]
    y_pos = version

    # Opacity.
    def bar_alpha(start, end):
        if end  < today:
            return 0.3
        elif start > today:
            return 0.7
        else:
            return 1.0

    # Green bar.
    ax.barh(
        y=y_pos,
        width=(row["active"] - row["release_date"]).days,
        left=row["release_date"],
        color=colors["active"],
        alpha=bar_alpha(row["release_date"], row["active"]),
    )

    # Yellow bar.
    ax.barh(
        y=y_pos,
        width=(row["security"] - row["active"]).days,
        left=row["active"],
        color=colors["security"],
        alpha=bar_alpha(row["active"], row["security"]),
    )

# Day line.
ax.axvline(today, color="black", linestyle="--", linewidth=2)

# Remove y ticks.
ax.set_yticks([])

# Version names.
for _, row in df.iterrows():
    version = row["Version"]
    if today < row["release_date"]:
        bgcolor = colors["not_active"]
    elif today <= row["active"]:
        bgcolor = colors["active"]
    elif today <= row["security"]:
        bgcolor = colors["security"]
    else:
        bgcolor = colors["ended"]

    ax.text(
        ax.get_xlim()[0],
        version,
        version,
        va='center',
        ha='left',
        fontsize=9,
        fontweight='bold',
        bbox=dict(facecolor=bgcolor, edgecolor='none', boxstyle='round,pad=0.3')
    )

# Date formatter.
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(plt.FuncFormatter(french_date_formatter))

# Invert y (oldest releases first).
ax.invert_yaxis()

# Set legend.
legend_elements = [
    Patch(facecolor=colors["active"], label="Version maintenue"),
    Patch(facecolor=colors["security"], label="Correctifs de sécurité uniquement"),
    Patch(facecolor=colors["ended"], label="Version non maintenue"),
]
ax.legend(handles=legend_elements, loc="upper right")

# Layout.
ax.set_title("Cycle de vie des versions Drupal 10.3 à 11.3", fontsize=14)
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()

# Export PNG
#plt.savefig("drupal_versions_lifecycle.png", dpi=300)
#print("✅ Fichier exporté : drupal_versions_lifecycle.png")

# Preview graph.
plt.show()
