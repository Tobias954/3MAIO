from app.model import load_model
from app.schemas import DiabetesFeatures
import numpy as np

def test_model_predicts():
    model, version = load_model("v0.1")
    x = DiabetesFeatures(age=0.02, sex=-0.044, bmi=0.06, bp=-0.03, s1=-0.02, s2=0.03, s3=-0.02, s4=0.02, s5=0.02, s6=-0.001)
    X = [[x.age, x.sex, x.bmi, x.bp, x.s1, x.s2, x.s3, x.s4, x.s5, x.s6]]
    pred = float(model.predict(X)[0])
    assert isinstance(pred, float)
