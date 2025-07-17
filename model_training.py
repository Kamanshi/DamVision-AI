import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

def train_model(df):
    X = df[['rainfall_mm', 'reservoir_capacity_m']]
    y = df['release_cusec']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'dam_release_model.pkl')  # save model
    print("Model trained and saved as dam_release_model.pkl")