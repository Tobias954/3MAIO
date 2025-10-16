import os
import joblib

DEFAULT_MODEL_VERSION = os.getenv("MODEL_VERSION", "v0.2")
MODEL_PATHS = {
    "v0.1": os.path.join(os.path.dirname(__file__), "..", "models", "model_v0.1.joblib"),
    "v0.2": os.path.join(os.path.dirname(__file__), "..", "models", "model_v0.2.joblib"),
}

def load_model(version: str = None):
    version = version or DEFAULT_MODEL_VERSION
    if version not in MODEL_PATHS:
        raise ValueError(f"Unknown model version: {version}")
    path = MODEL_PATHS[version]
    model = joblib.load(path)
    return model, version
