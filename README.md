# 🎓 Student Performance Prediction System

<p align="center">
  <b>Machine Learning • FastAPI • Streamlit • Data Visualization</b><br>
  Predict student success and identify at-risk learners using data-driven insights.
</p>

---

## 🚀 Overview

This project builds a complete **end-to-end Machine Learning system** to predict student performance based on academic and behavioral data.

It helps identify:

* ✅ Students likely to pass
* ⚠️ Students at risk

The system combines:

* Data preprocessing
* Model training
* API deployment
* Interactive dashboard

---

## 🎯 Problem Statement

Educational institutions often identify struggling students too late.

This project solves that by:

* Predicting outcomes early
* Enabling timely intervention
* Improving overall academic performance

---

## 🧠 Machine Learning Approach

* **Model Used:** Random Forest Classifier
* **Type:** Classification (Pass / At Risk)
* **Dataset:** Synthetic (realistic simulation)

### Input Features

* Attendance %
* Study Hours
* Quiz Score
* Assignment Score
* Previous GPA

### Output

* Prediction (Pass / At Risk)
* Probability Score

---

## 🏗️ System Architecture

```text
User Input (Dashboard)
        ↓
Streamlit UI
        ↓
ML Model (Random Forest)
        ↓
FastAPI Backend
        ↓
Prediction + Probability
        ↓
Charts & Insights
```

---

## 💻 Tech Stack

| Category      | Tools Used    |
| ------------- | ------------- |
| Language      | Python        |
| Data Handling | Pandas, NumPy |
| ML Model      | Scikit-learn  |
| Backend API   | FastAPI       |
| Frontend UI   | Streamlit     |
| Visualization | Plotly        |

---

## 📊 Features

* 🎯 Real-time prediction
* 📈 Probability score visualization
* 📊 Interactive charts (Bar + Pie)
* ⚡ FastAPI backend integration
* 🧪 Synthetic dataset generation
* 🖥️ Clean dashboard interface

---

## 📸 Screenshots

### Dashboard UI 

<img width="1920" height="1080" alt="Screenshot (174)" src="https://github.com/user-attachments/assets/fa1bc91e-3d34-4110-8886-0d883dad6e82" />

### Prediction Result

# Likely Pass
<img width="1920" height="1080" alt="Screenshot (175)" src="https://github.com/user-attachments/assets/15eeb2fb-932d-43ca-8334-5abb5f74d344" />

<img width="1920" height="1080" alt="Screenshot (176)" src="https://github.com/user-attachments/assets/7a27fb6d-1669-4f18-915d-d73917cdfd78" />

<img width="1920" height="1080" alt="Screenshot (177)" src="https://github.com/user-attachments/assets/40ed669a-153b-4b25-946b-47d18144b7fc" />

# At Risk Student
<img width="1920" height="1080" alt="Screenshot (181)" src="https://github.com/user-attachments/assets/189d1c57-15a0-47f8-9f8f-389120b84a49" />

<img width="1920" height="1080" alt="Screenshot (182)" src="https://github.com/user-attachments/assets/e8cdf98c-a010-404f-8041-14302b05e03a" />

<img width="1920" height="1080" alt="Screenshot (183)" src="https://github.com/user-attachments/assets/a93cfb1c-2f4d-4aa8-8893-ac08c9928114" />


---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/challakishore-dev/student-performance-prediction-system.git
cd student-performance-prediction-system
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Train Model

```bash
python train.py
```

---

### 4. Run Backend API

```bash
uvicorn main:app --reload
```

---

### 5. Run Dashboard

```bash
streamlit run app.py
```

---

## 🧪 Example Predictions

| Scenario                      | Result     |
| ----------------------------- | ---------- |
| High attendance + high scores | ✅ Pass     |
| Low attendance + low scores   | ⚠️ At Risk |

---

## 📁 Project Structure

```text
student-performance-prediction-system/
│
├── app.py              # Streamlit UI
├── main.py             # FastAPI backend
├── train.py            # Model training
├── generate_data.py    # Synthetic dataset
├── students.csv        # Dataset
├── model.pkl           # Trained model
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

* 🔐 User login system
* 📂 CSV bulk upload
* 🧠 Advanced ML models (XGBoost)
* ☁️ Cloud deployment
* 📊 Advanced analytics dashboard

---

## 📌 Key Learnings

* End-to-end ML pipeline
* API integration with ML models
* Interactive dashboards
* Data simulation techniques
* Real-world problem solving

---

## 👨‍💻 Author

**Challa Kishore**

# GitHub: https://github.com/challakishore-dev

# LinkedIn: https://linkedin.com/in/challa-kishore-a817552b4


## ⭐ Support

If you found this project useful:

⭐ Star this repository
🍴 Fork it
📢 Share it

---

<p align="center">
  Built for learning • Designed for impact 🚀
</p>
