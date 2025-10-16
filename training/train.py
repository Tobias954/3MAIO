import argparse, json, os, joblib
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def get_data(seed=42):
    Xy = load_diabetes(as_frame=True)
    X = Xy.frame.drop(columns=["target"])
    y = Xy.frame["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    return X_train, X_test, y_train, y_test

def train(version: str):
    if version == "v0.1":
        pipe = Pipeline([("scaler", StandardScaler()), ("reg", LinearRegression())])
    elif version == "v0.2":
        pipe = Pipeline([("scaler", StandardScaler()), ("reg", Ridge(alpha=1.0, random_state=42))])
    else:
        raise ValueError("version must be v0.1 or v0.2")

    X_train, X_test, y_train, y_test = get_data()
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    os.makedirs("models", exist_ok=True)
    out_path = os.path.join("models", f"model_{version}.joblib")
    joblib.dump(pipe, out_path)

    metrics_path = os.path.join("models", "metrics.json")
    metrics = {version: {"rmse": float(rmse)}}
    if os.path.exists(metrics_path):
        with open(metrics_path, "r") as f:
            current = json.load(f)
    else:
        current = {}
    current.update(metrics)
    with open(metrics_path, "w") as f:
        json.dump(current, f, indent=2)

    print(f"Saved {version} to {out_path} with RMSE={rmse:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", type=str, default="v0.1", choices=["v0.1", "v0.2"])
    args = parser.parse_args()
    train(args.version)
