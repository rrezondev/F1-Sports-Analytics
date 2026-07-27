import pandas as pd

# Leximi i dataset-it
df = pd.read_csv('../data/f1_2021_2025.csv')

# Shfaq 20 rreshtat e parë
print("\nFIRST 20 ROWS:\n")

print(df.head(20))

# Info
print("\nDATASET INFO:\n")

print(df.info())

# Sezonet
print("\nSEASONS:\n")

print(df['season'].unique())

# Numri i garave
print("\nTOTAL ROWS:\n")

print(len(df))

# Standings për çdo sezon

season_standings = (
    df.groupby(['season', 'driver'])['points']
    .sum()
    .reset_index()
)

print("\nSEASON STANDINGS:\n")

print(season_standings)