@echo off
pip install -r requirements.txt
python train.py
start cmd /k uvicorn main:app --reload
start cmd /k streamlit run app.py
