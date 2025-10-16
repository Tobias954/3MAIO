import joblib, json, os
from pathlib import Path
from training.train import train

def test_smoke_training(tmp_path):
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        train("v0.1")
        assert Path("models/model_v0.1.joblib").exists()
        with open("models/metrics.json") as f:
            metrics = json.load(f)
        assert "v0.1" in metrics
        assert metrics["v0.1"]["rmse"] > 0
    finally:
        os.chdir(cwd)
