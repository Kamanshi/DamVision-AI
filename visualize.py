import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

matplotlib.use('TkAgg')  # Fix for WinPy users

# Load your dataset
df = pd.read_csv("dataset.csv")

# Convert date column to datetime if not already
df['date'] = pd.to_datetime(df['date'])

# Set the style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 10))

# Plot 1: Rainfall over time
plt.subplot(2, 1, 1)
sns.lineplot(data=df, x='date', y='rainfall_mm', marker='o', color='skyblue')
plt.title("🌧 Rainfall Over Time", fontsize=14)
plt.ylabel("Rainfall (mm)")

# Plot 2: Water Release and Level
plt.subplot(2, 1, 2)
sns.lineplot(data=df, x='date', y='release_cusec', label='Release (cusec)', marker='o', color='orange')
sns.lineplot(data=df, x='date', y='water_level_m', label='Water Level (m)', marker='x', color='green')
plt.title("💧 Water Release & Level Over Time", fontsize=14)
plt.ylabel("Value")
plt.xlabel("Date")
plt.legend()

# Improve layout
plt.tight_layout()
plt.show()