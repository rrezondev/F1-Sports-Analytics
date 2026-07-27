import pandas as pd

# Leximi i dataset-it
df = pd.read_csv('../data/f1_2025_results.csv')

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET INFO:")
print(df.info())

print("\nSTATISTICS:")
print(df.describe())

print("\nMISSING VALUES:")
print(df.isnull().sum())