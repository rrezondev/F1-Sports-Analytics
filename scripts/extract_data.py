import fastf1
import pandas as pd

# Cache
fastf1.Cache.enable_cache('../f1_cache')

all_results = []

# Sezonet
seasons = [2021, 2022, 2023, 2024, 2025]

for year in seasons:

    print(f"\nLoading season {year}")

    # Kalendari
    schedule = fastf1.get_event_schedule(year)

    # Hiq testing
    races = schedule[schedule['EventFormat'] != 'testing']

    for _, event in races.iterrows():

        try:

            gp_name = event['EventName']

            print(f"Loading {year} - {gp_name}")

            # Race session
            session = fastf1.get_session(year, gp_name, 'R')
            session.load()

            results = session.results

            top10 = results.head(10)

            for _, row in top10.iterrows():

                # Laps
                laps = session.laps.pick_drivers(
                    row['Abbreviation']
                )

                # Tire compound
                if not laps.empty and 'Compound' in laps.columns:
                    tire_compound = laps['Compound'].mode()[0]
                else:
                    tire_compound = "Unknown"

                # Pit stops
                if not laps.empty and 'PitOutTime' in laps.columns:
                    pit_stops = laps['PitOutTime'].notna().sum()
                else:
                    pit_stops = 0

                # Avg lap time
                if not laps.empty and 'LapTime' in laps.columns:
                    avg_lap_time = (
                        laps['LapTime']
                        .dt.total_seconds()
                        .mean()
                    )
                else:
                    avg_lap_time = None

                driver_data = {
                    'season': year,
                    'grand_prix': gp_name,
                    'driver': row['Abbreviation'],
                    'team': row['TeamName'],
                    'position': row['Position'],
                    'points': row['Points'],
                    'status': row['Status'],
                    'tire_compound': tire_compound,
                    'pit_stops': pit_stops,
                    'avg_lap_time': avg_lap_time
                }

                all_results.append(driver_data)

        except Exception as e:

            print(f"Error loading {gp_name}: {e}")

# DataFrame
df = pd.DataFrame(all_results)

# Save
df.to_csv('../data/f1_2021_2025.csv', index=False)

print("\nExtraction completed!")
print(df.head())