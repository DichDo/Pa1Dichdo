# 𓃠 engagement_forecaster.py - Predicts best engagement times (mock)

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def train_forecaster(csv_path: str):
    df = pd.read_csv(csv_path, parse_dates=["timestamp"])
    df["hour"] = df["timestamp"].dt.hour
    X = df[["hour"]]
    y = df["engagement"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestRegressor().fit(X_train, y_train)
    return model

def predict_best_hour(model):
    hours = pd.DataFrame({"hour": list(range(24))})
    preds = model.predict(hours)
    best = hours.iloc[preds.argmax()]["hour"]
    return int(best)
