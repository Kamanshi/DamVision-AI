import sys
import os
sys.path.append(os.path.dirname(__file__))
from data_preprocessing import load_and_clean_data
from model_training import train_model
from prediction_module import predict_release
from rainfall_simulator import simulate_rainfall
from dam_control_ai import control_dam

df = load_and_clean_data("dataset.csv")
train_model(df)

rainfall = simulate_rainfall()
capacity = 40  # constant for now

release = predict_release(rainfall, capacity)
decision = control_dam(release)

print(f"Simulated Rainfall: {rainfall:.2f} mm")
print(f"Predicted Release: {release:.2f} cusecs")
print(f"Dam Control Decision: {decision}")