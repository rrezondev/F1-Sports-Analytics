import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('data/f1_2021_2025.csv')

st.title("📊 Analytics Dashboard")

# FILTER
season = st.selectbox(
    "Select Season",
    sorted(df['season'].unique())
)

filtered_df = df[df['season'] == season]

# TABS
tab1, tab2, tab3, tab4 = st.tabs([
    "Points",
    "Tire Strategy",
    "Pit Stops",
    "Lap Times"
])

# POINTS
with tab1:

    st.subheader("Top Drivers by Points")

    points = (
        filtered_df.groupby('driver')['points']
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        points,
        x='driver',
        y='points',
        title='Driver Points'
    )

    st.plotly_chart(fig, use_container_width=True)

# TIRE STRATEGY
with tab2:

    st.subheader("Tire Compound Usage")

    tire = (
        filtered_df['tire_compound']
        .value_counts()
        .reset_index()
    )

    tire.columns = ['compound', 'count']

    fig = px.pie(
        tire,
        names='compound',
        values='count',
        hole=0.4
    )

    st.plotly_chart(fig, use_container_width=True)

# PIT STOPS
with tab3:

    st.subheader("Average Pit Stops")

    pits = (
        filtered_df.groupby('driver')['pit_stops']
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        pits,
        x='driver',
        y='pit_stops'
    )

    st.plotly_chart(fig, use_container_width=True)

# LAP TIMES
with tab4:

    st.subheader("Average Lap Time")

    lap = (
        filtered_df.groupby('driver')['avg_lap_time']
        .mean()
        .sort_values()
        .reset_index()
    )

    fig = px.scatter(
        lap,
        x='driver',
        y='avg_lap_time',
        size='avg_lap_time',
        hover_name='driver'
    )

    st.plotly_chart(fig, use_container_width=True)