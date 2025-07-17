import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# Set page layout
st.set_page_config(page_title="AI Dam Manager", layout="centered")

# Load model
try:
    model = joblib.load("dam_release_model.pkl")
except FileNotFoundError:
    st.error("❌ Model file not found!")
    st.stop()

# Load dataset
try:
    df = pd.read_csv("dataset.csv")
    df['date'] = pd.to_datetime(df['date'])
except FileNotFoundError:
    st.warning("⚠ dataset.csv not found — historical charts won’t appear.")
    df = None

# Title
st.title("🌊 DAMVISION AI")

# Sidebar: User input
st.sidebar.header("⚙ Simulation Controls")
rainfall = st.sidebar.slider("🌧 Rainfall (mm)", 0, 200, 50)
capacity = st.sidebar.slider("🏞 Reservoir Capacity (m)", 10, 100, 40)

# Predict release
input_data = [[rainfall, capacity]]
release = model.predict(input_data)[0]

# AI Decision
if release > 1500:
    decision = "🔓 Open gates to 100%"
    gate_level = 100
elif release > 1000:
    decision = "🔓 Open gates to 80%"
    gate_level = 80
elif release > 500:
    decision = "🔓 Open gates to 50%"
    gate_level = 50
else:
    decision = "🔒 Keep gates closed"
    gate_level = 0

# ------------------------------
# 1. Live Rainfall Animation
# ------------------------------
st.subheader("🌧 Live Rainfall Animation")
rain_drops = "💧" * (rainfall // 10)
st.markdown(f"<div style='font-size:40px'>{rain_drops}</div>", unsafe_allow_html=True)

# ------------------------------
# 2. Dam Gate Simulation
# ------------------------------
st.subheader("🚢 Dam Gate Simulation")
st.progress(gate_level / 100)
st.markdown(f"*Gate Open Level:* {gate_level}%")

# ⚠ High-Risk Warning with Sound
if gate_level >= 80:
    st.error("⚠ High Risk of Flooding! Immediate Attention Required.")
    
    # 🔊 Danger alarm sound (auto plays in supported browsers)
    st.markdown("""
    <audio autoplay>
      <source src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" type="audio/ogg">
    </audio>
    """, unsafe_allow_html=True)

# ------------------------------
# 3. AI Prediction & Control
# ------------------------------
st.subheader("📍 AI Prediction & Control")
st.success(f"Predicted Release: {release:.2f} cusec")
st.info(f"Decision: {decision}")

# ------------------------------
# 4. Rainfall vs Predicted Release
# ------------------------------
st.subheader("📊 Rainfall vs Predicted Release")
fig1 = go.Figure(data=[
    go.Bar(name='Rainfall (mm)', x=['Rainfall'], y=[rainfall], marker_color='skyblue'),
    go.Bar(name='Release (cusec)', x=['Release'], y=[release], marker_color='orange')
])
fig1.update_layout(barmode='group', height=400)
st.plotly_chart(fig1)

# ------------------------------
# 5. Historical Rainfall & Release
# ------------------------------
if df is not None:
    st.subheader("📉 Historical Rainfall & Release Trend")
    fig2 = px.line(df, x='date', y=['rainfall_mm', 'release_cusec'],
                   labels={'value': 'Measurement', 'date': 'Date'},
                   title='Rainfall and Water Release Over Time')
    fig2.update_layout(legend_title_text='Metric', template="plotly_dark")
    st.plotly_chart(fig2)

    # ------------------------------
    # 6. Water Level Over Time
    # ------------------------------
    st.subheader("💧 Water Level Over Time")
    fig3 = px.area(df, x='date', y='water_level_m',
                   title='Reservoir Water Level (m)', template="plotly_dark",
                   color_discrete_sequence=['deepskyblue'])
    st.plotly_chart(fig3)

# Footer
st.markdown("---")
st.markdown("🛠 Made with ❤ by [Kamanshi Saini] | Internship based DAM Project | B.Tech (2nd Year)")