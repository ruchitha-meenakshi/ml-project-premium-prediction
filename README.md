# 🛡️ **Healthcare Premium Prediction (Regression Model)**

*A portfolio project built as part of the CodeBasics Gen AI & Data Science Bootcamp*

---

## 🚀 **Project Overview**

This project is a complete end-to-end **machine learning application** that predicts annual health insurance premiums based on customer demographics, lifestyle patterns, medical history, and insurance plan details.

It was built as part of a simulated industry project with **AtliQ.ai**, where I take on the role of a Data Scientist contributing to the organisation’s flagship AI initiative for **S.H.I.E.L.D. Insurance**.

The final solution includes:
* A full data pipeline
* Exploratory data analysis
* Feature engineering and model development
* Model packaging & deployment artifacts
* A fully functional **Streamlit web app** for premium estimation

📌 **Live App:** [*health_premium_prediction_app*](https://ml-premium-prediction-project-cb.streamlit.app/)

📌 **GitHub Repo:** [https://github.com/ruchitha-meenakshi/ml-project-premium-prediction](https://github.com/ruchitha-meenakshi/ml-project-premium-prediction)

---

#  **Business Story: The Rise of AtliQ AI**

In 2024, the rise of AI technologies disrupted the traditional IT sector, leading to a slowdown in funding.
**Bruce Harley**, facing this shift, transformed his struggling IT company into a forward-thinking AI firm — **AtliQ.ai**.

AtliQ.ai’s mission:

> ⚡ *“To position Bruce Harley as a leading AI innovator in India, delivering high-impact AI solutions to real businesses.”*

As part of this vision, AtliQ.ai partnered with **S.H.I.E.L.D. Insurance** to develop a machine-learning model that predicts health insurance premiums more intelligently using customer risk factors.

The project team:

* **Bruce Harley** — Founder & CEO, AtliQ.ai
* **Tony Sharma** — Lead Data Scientist
* **Peter Pande** — Junior Data Scientist
* **Nick Puri** — Senior Product Owner (client stakeholder)

This project reflects real-world challenges including scope definition, model building, risk management, and deploying an end-user application.

---

# **Project Objectives**

### **Primary Goal**

Build an AI model to estimate annual health insurance premiums and integrate it into a user-friendly application.

### **Success KPIs (from Project Superstar – Shield 001)**

* Increase S.H.I.E.L.D’s revenue by **15%**
* Reduce customer churn by **10%**
* Improve pricing accuracy using machine learning
* Reduce claims ratio by **5%**
* Increase market share by **3%**

---

# **Project Structure**

```

ml-project-premium-prediction
│
├── app/                             # Streamlit web application
│   ├── main.py
│   └── prediction_helper.py
│
├── artifacts/                       # Final models & scalers for deployment
│   ├── model_rest.joblib
│   ├── model_young.joblib
│   ├── scaler_rest.joblib
│   └── scaler_young.joblib
│
├── data/
│   ├── raw/                         # NOT uploaded (proprietary) – contains .gitkeep
│   └── processed/                   # Cleaned & processed dataset NOT uploaded (proprietary)
│
├── outputs/                         # Analysis outputs from notebooks/scripts
│   ├── figures/                     # All visualizations, plots, charts
│   ├── models/                      # Exported .pkl files (EDA/model exploration)
│   │   ├── cols_to_scale.pkl
│   │   ├── minmax_scaler.pkl
│   │   └── xgb_best_model.pkl
│   └── tables/                      # Summary tables, metrics, reports
│
├── scripts/                         # Jupyter notebooks & Python scripts
│   ├── 01_data_cleaning_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04a_segmentation_rest.ipynb
│   ├── 04b_segmentation_young.ipynb
│   ├── 05a_premium_model_rest.ipynb
│   ├── 05b_premium_model_young.ipynb
│   ├── 06a_model_evaluation_young.ipynb
│   ├── 06b_model_evaluation_rest.ipynb
│   └── imports.py
│
│
├── .gitignore                       # Excludes raw data, cache & temp files
├── LICENSE
├── README.md
└── requirements.txt

```
---

# **Technical Stack**

### **Languages & Libraries**

* Python 3.10
* Pandas, NumPy
* Scikit-Learn
* Linear Model, XGBoost, Random Forest
* RandomizedSearchCV
* Matplotlib, Seaborn
* Joblib (model persistence)
* Streamlit (deployment UI)

---

# **Model Overview**

Two ML models were developed based on age segmentation:

| **Age Group**  | **Best Model**                     | 
| -------------- | ---------------------------------- | 
| **≤ 25 years** | Linear Regression-based model      | 
| **> 25 years** | Gradient boosting / ensemble model | 

Preprocessing includes:

* Categorical encoding
* Normalization via age-specific scalers
* Medical history risk scoring
* Manual and automated feature engineering

All models & scalers are saved inside `artifacts/`.

---

# **Streamlit App**

The Streamlit app provides:

✔ A clean, modern UI with custom CSS

✔ Input fields for demographics, lifestyle, medical history, and plan choice

✔ Real-time premium prediction

✔ Visual differentiation between customer segments

✔ Clear explanation of the pricing logic

Users enter their details and receive an instant premium estimate.

📌 **Live App:** [*health_premium_prediction_app*](https://ml-premium-prediction-project-cb.streamlit.app/)

## Application Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/de360055-c3dd-4967-b76f-d416213204a8" 
       width="90%" 
       alt="Health Insurance Premium Estimator App Preview"/>
</p>

*A clean, modern Streamlit interface for estimating annual health insurance premiums.*


---

# **Data Privacy Notice**

The **dataset from CodeBasics Bootcamp is proprietary** and is **NOT included in this repository**.

To comply with licensing:

* `data/raw/` and `data/processed/` are included in `.gitignore`
* A placeholder `.gitkeep` file preserves the folder structure
* No real data (raw or processed) is included in this repository
* Only code, documentation, and synthetic or sample placeholder files are stored here
---

# **How to Run Locally**

### 1. Clone the repo

```bash
git clone https://github.com/ruchitha-meenakshi/ml-project-premium-prediction.git
cd ml-project-premium-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app/main.py
```

---

# **Learnings from the Project**

* Realistic project planning with Jira-style task breakdown
* Feature engineering for health insurance datasets
* Model segmentation and scaler management
* Data versioning and safe handling of proprietary datasets
* Building and deploying a full machine learning solution
* Writing production-ready Streamlit apps with custom UI

---

# **Acknowledgements**

* **CodeBasics Bootcamp** for project structure and storyline
* **Dhaval Patel, Hemanand Vadivel & team** for industry-oriented guidance
* The fictional **AtliQ.ai** team for the project narrative

---

# **Author**

**Ruchitha Uppuluri**

Aspiring Data Scientist · CodeBasics Bootcamp

🔗 *www.linkedin.com/in/ruchithauppuluri*

---

