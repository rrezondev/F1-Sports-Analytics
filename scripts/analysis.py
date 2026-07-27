import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Leximi i dataset-it
df = pd.read_csv('../data/f1_2025_results.csv')

# =========================
# PERFORMANCE SCORE
# =========================

# Pikët maksimale në dataset
max_points = df['points'].max()

# Formula:
# performance_score = points / max_points * 100

df['performance_score'] = (
    df['points'] / max_points
) * 100

# =========================
# TOTAL POINTS
# =========================

driver_points = (
    df.groupby('driver')['points']
    .sum()
    .sort_values(ascending=False)
)

print("\nTOTAL POINTS:")
print(driver_points)

# =========================
# AVERAGE POSITION
# =========================

avg_position = (
    df.groupby('driver')['position']
    .mean()
    .sort_values()
)

print("\nAVERAGE POSITION:")
print(avg_position)

# =========================
# PODIUMS
# =========================

podiums = df[df['position'] <= 3]

podium_counts = (
    podiums.groupby('driver')
    .size()
    .sort_values(ascending=False)
)

print("\nPODIUMS:")
print(podium_counts)

# =========================
# WINS
# =========================

wins = df[df['position'] == 1]

win_counts = (
    wins.groupby('driver')
    .size()
    .sort_values(ascending=False)
)

print("\nWINS:")
print(win_counts)

# =========================
# SAVE ENRICHED DATASET
# =========================

df.to_csv('../data/f1_2025_enriched.csv', index=False)

print("\nEnriched dataset saved successfully!")

# =========================
# GRAPH 1 - TOTAL POINTS
# =========================

plt.figure(figsize=(12, 7))

driver_points.plot(kind='barh')

plt.title('Total Points by Driver - F1 2025')
plt.xlabel('Points')
plt.ylabel('Driver')

plt.tight_layout()

plt.savefig('../outputs/charts/total_points.png')

plt.show()

# =========================
# GRAPH 2 - AVERAGE POSITION
# =========================

plt.figure(figsize=(12, 7))

avg_position.plot(kind='bar')

plt.title('Average Finishing Position')
plt.xlabel('Driver')
plt.ylabel('Average Position')

plt.tight_layout()

plt.savefig('../outputs/charts/average_position.png')

plt.show()

# =========================
# GRAPH 3 - PERFORMANCE SCORE
# =========================

plt.figure(figsize=(12, 7))

sns.boxplot(
    x='driver',
    y='performance_score',
    data=df
)

plt.title('Performance Score Distribution')
plt.xlabel('Driver')
plt.ylabel('Performance Score')

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('../outputs/charts/performance_boxplot.png')

plt.show()

# =========================
# GRAPH 4 - HEATMAP
# =========================

heatmap_data = df.pivot_table(
    values='position',
    index='driver',
    columns='grand_prix'
)

plt.figure(figsize=(16, 8))

sns.heatmap(
    heatmap_data,
    annot=True,
    cmap='coolwarm'
)

plt.title('Driver Positions by Grand Prix')

plt.tight_layout()

plt.savefig('../outputs/charts/heatmap_positions.png')

plt.show()

# =========================
# TIRE STRATEGY
# =========================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x='tire_compound'
)

plt.title('Tire Compound Usage')
plt.xlabel('Tire Compound')
plt.ylabel('Count')

plt.tight_layout()

plt.savefig('../outputs/charts/tire_strategy.png')

plt.show()

# =========================
# PIT STOPS
# =========================

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=df,
    x='driver',
    y='pit_stops'
)

plt.title('Pit Stops by Driver')

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('../outputs/charts/pit_stops.png')

plt.show()

# =========================
# LAP TIME ANALYSIS
# =========================

import matplotlib.ticker as ticker

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=df,
    x='driver',
    y='avg_lap_time'
)

# Konvertimi në minuta:sekonda
def format_time(x, pos):

    minutes = int(x // 60)
    seconds = int(x % 60)

    return f"{minutes}:{seconds:02d}"

plt.gca().yaxis.set_major_formatter(
    ticker.FuncFormatter(format_time)
)

plt.title('Average Lap Time by Driver')

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('../outputs/charts/lap_times.png')

plt.show()