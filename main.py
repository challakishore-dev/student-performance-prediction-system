from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd, joblib, os
if not os.path.exists('model.pkl'):
    import train
app=FastAPI(title='Student Performance API')
model=joblib.load('model.pkl')
class Student(BaseModel):
    attendance:int
    study_hours:int
    quiz_score:int
    assignment_score:int
    previous_gpa:float
@app.get('/')
def root():
    return {'status':'running'}
@app.post('/predict')
def predict(s:Student):
    X=pd.DataFrame([s.model_dump()])
    prob=float(model.predict_proba(X)[0][1])
    return {'prediction':int(prob>=0.5),'probability':round(prob,4)}
