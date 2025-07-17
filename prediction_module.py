import joblib
import numpy as np

def predict_release(rainfall, capacity):
    model = joblib.load('dam_release_model.pkl')
    prediction = model.predict(np.array([[rainfall, capacity]]))
    return prediction[0]