import streamlit as st
import pandas as pd
import plotly.express as px

# LOAD DATA
df = pd.read_csv("data/f1_2021_2025.csv")

# PAGE CONFIG
st.set_page_config(
    page_title="F1 Analytics",
    page_icon="🏎️",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

.metric-card {
    background: linear-gradient(135deg, #1F2937, #111827);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 0px 20px rgba(255,0,0,0.2);
}

.big-font {
    font-size: 40px !important;
    font-weight: bold;
    color: #FF1801;
}

.small-font {
    font-size: 18px !important;
    color: #9CA3AF;
}

.title {
    font-size: 55px;
    font-weight: bold;
    color: white;
}

.subtitle {
    color: #9CA3AF;
    font-size: 20px;
}

</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<div class='title'>
🏎️ Formula 1 Analytics Platform
</div>

<div class='subtitle'>
Advanced Sports Analytics & AI Predictions
</div>
""", unsafe_allow_html=True)

st.write("")

# KPI SECTION
total_races = df['grand_prix'].nunique()
total_drivers = df['driver'].nunique()
total_seasons = df['season'].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='big-font'>{total_races}</div>
        <div class='small-font'>Total Races</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='big-font'>{total_drivers}</div>
        <div class='small-font'>Drivers</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='metric-card'>
        <div class='big-font'>{total_seasons}</div>
        <div class='small-font'>Seasons</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# TOP DRIVERS
st.subheader("🔥 Top Drivers Overall")

driver_points = (
    df.groupby('driver')['points']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    driver_points,
    x='driver',
    y='points',
    text='points',
    template='plotly_dark'
)

fig.update_layout(
    paper_bgcolor='#0E1117',
    plot_bgcolor='#0E1117',
    font_color='white',
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# SEASON FILTER
st.subheader("📅 Season Analysis")

season = st.selectbox(
    "Select Season",
    sorted(df['season'].unique())
)

filtered = df[df['season'] == season]

# DRIVER TABLE
st.subheader(f"🏁 {season} Driver Standings")

standings = (
    filtered.groupby('driver')['points']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

st.dataframe(
    standings,
    use_container_width=True
)

# FOOTER
st.write("")
st.markdown("---")
st.caption("Built with Python • FastF1 • Pandas • Streamlit • Machine Learning")