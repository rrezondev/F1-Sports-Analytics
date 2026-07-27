import streamlit as st
import pandas as pd
import plotly.express as px

pred_df = pd.read_csv('data/predictions_2026.csv')

st.title("🤖 2026 AI Predictions")

# TOP 3
top3 = pred_df.head(3)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🥇 1st", top3.iloc[0]['driver'])

with col2:
    st.metric("🥈 2nd", top3.iloc[1]['driver'])

with col3:
    st.metric("🥉 3rd", top3.iloc[2]['driver'])

# CHART
fig = px.bar(
    pred_df.head(10),
    x='driver',
    y='predicted_points_2026',
    title='Predicted 2026 Championship Standings'
)

st.plotly_chart(fig, use_container_width=True)

# TABLE
st.subheader("Prediction Table")

st.dataframe(pred_df)