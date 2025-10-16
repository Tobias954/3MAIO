from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from .schemas import DiabetesFeatures, PredictionResponse
from .model import load_model

app = FastAPI(title="Virtual Diabetes Clinic Triage Service", version="1.0.0")

# Load model at startup
model, model_version = load_model()

@app.get("/health")
def health():
    return {"status": "ok", "model_version": model_version}

@app.post("/predict", response_model=PredictionResponse)
def predict(features: DiabetesFeatures):
    try:
        # Order must match sklearn dataset columns
        X = [[
            features.age, features.sex, features.bmi, features.bp,
            features.s1, features.s2, features.s3, features.s4,
            features.s5, features.s6
        ]]
        pred = float(model.predict(X)[0])
        return PredictionResponse(prediction=pred, model_version=model_version)
    except ValidationError as ve:
        return JSONResponse(status_code=400, content={"error": "validation_error", "detail": ve.errors()})
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": "bad_request", "detail": str(e)})
