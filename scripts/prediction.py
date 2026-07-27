import pandas as pd
from sklearn.linear_model import LinearRegression

# Leximi i dataset-it
df = pd.read_csv('../data/f1_2021_2025.csv')

# Pikët totale për sezon
season_points = (
    df.groupby(['season', 'driver'])['points']
    .sum()
    .reset_index()
)

predictions = []

drivers = season_points['driver'].unique()

for driver in drivers:

    driver_data = season_points[
        season_points['driver'] == driver
    ]

    # X = seasons
    X = driver_data[['season']]

    # y = points
    y = driver_data['points']

    # Model
    model = LinearRegression()

    model.fit(X, y)

    # Predict 2026
    future_year = pd.DataFrame({
    'season': [2026]
    })

    pred_2026 = model.predict(future_year)[0]
    pred_2026 = max(pred_2026, 0)

    predictions.append({
        'driver': driver,
        'predicted_points_2026': round(pred_2026, 1)
    })

# DataFrame
pred_df = pd.DataFrame(predictions)

# Renditja finale
pred_df = pred_df.sort_values(
    by='predicted_points_2026',
    ascending=False
)

print("\nPREDICTED 2026 STANDINGS:\n")

print(pred_df)

import matplotlib.pyplot as plt

# TOP 10
top10 = pred_df.head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top10['driver'],
    top10['predicted_points_2026']
)

plt.xlabel("Predicted Points")
plt.ylabel("Driver")

plt.title("Predicted 2026 Driver Standings")

plt.tight_layout()

plt.show()

pred_df.to_csv(
    '../data/predictions_2026.csv',
    index=False
)