import streamlit as st
import pandas as pd

df = pd.read_csv('data/f1_2021_2025.csv')

st.title("📁 Dataset Explorer")

# FILTERS
season = st.selectbox(
    "Season",
    sorted(df['season'].unique())
)

team = st.selectbox(
    "Team",
    sorted(df['team'].unique())
)

filtered = df[
    (df['season'] == season)
    &
    (df['team'] == team)
]

st.dataframe(filtered)

st.success(f"Rows Found: {len(filtered)}")