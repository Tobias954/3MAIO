from pydantic import BaseModel, Field
from typing import Optional

class DiabetesFeatures(BaseModel):
    age: float = Field(..., description="Normalized age feature from sklearn diabetes")
    sex: float = Field(..., description="Normalized sex feature from sklearn diabetes")
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

class PredictionResponse(BaseModel):
    prediction: float
    model_version: str
