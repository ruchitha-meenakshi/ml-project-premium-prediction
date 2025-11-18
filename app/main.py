# codebasics ML course: codebasics.io, all rights reserverd

import streamlit as st
from prediction_helper import predict

# -------------------------
# Page configuration
# -------------------------
st.set_page_config(
    page_title="S.H.I.E.L.D Insurance | Premium Health Insurance Estimator",
    page_icon="🛡️",
    layout="wide",
)

# -------------------------
# Global CSS – layout, theme, animations
# -------------------------
st.markdown(
    """
<style>
:root {
    --primary: #1d4ed8;          /* deep blue */
    --primary-dark: #1e3a8a;
    --accent: #0ea5e9;           /* light blue */
    --bg: #f3f4f6;               /* light gray */
    --card-bg: #ffffff;
    --border: #e5e7eb;
    --text-main: #111827;
    --text-muted: #6b7280;
}

/* Global background */
body, .main {
    background-color: var(--bg);
}

/* Center app content */
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1100px !important;
}

/* Top navigation bar */
.navbar {
    width: 100%;
    padding: 0.75rem 1.5rem;
    background: linear-gradient(90deg, #111827, #1f2933);
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 0 0 12px 12px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    margin-bottom: 1.5rem;
}
.nav-left {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.03em;
}
.nav-badge {
    font-size: 0.75rem;
    padding: 0.15rem 0.5rem;
    border-radius: 999px;
    background-color: rgba(255,255,255,0.12);
}
.nav-right {
    font-size: 0.8rem;
    opacity: 0.85;
}

/* Hero section */
.hero {
    display: flex;
    gap: 2rem;
    margin-bottom: 1.5rem;
}
.hero-left {
    flex: 2;
}
.hero-title {
    font-size: 2.1rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 0.5rem;
}
.hero-subtitle {
    font-size: 0.98rem;
    color: var(--text-muted);
    max-width: 32rem;
}
.hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.8rem;
    padding: 0.25rem 0.7rem;
    border-radius: 999px;
    background-color: #e0f2fe;
    color: #0369a1;
    margin-bottom: 0.6rem;
}

/* Hero right card */
.hero-right {
    flex: 1.4;
}
.hero-card {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 1.25rem 1.4rem;
    border: 1px solid var(--border);
    box-shadow: 0 10px 25px rgba(15,23,42,0.12);
}
.hero-card-title {
    font-size: 0.88rem;
    color: var(--text-muted);
    margin-bottom: 0.6rem;
}
.hero-card-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--primary);
}
.hero-card-note {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-top: 0.5rem;
}

/* Section containers now act as thin dividers */
.section-card {
    padding: 0.4rem 0 1rem 0;
    border-radius: 0;
    background: transparent;
    border: none;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1rem;
    animation: fadeIn 0.5s ease;
}
.section-title {
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 0.2rem;
}
.section-subtitle {
    font-size: 0.85rem;
    color: var(--text-muted);
    margin-bottom: 0.9rem;
}

/* Predict button */
.stButton>button {
    background: linear-gradient(90deg, var(--primary), var(--accent));
    color: #ffffff;
    font-size: 1.02rem;
    font-weight: 600;
    padding: 0.65rem 1.6rem;
    border-radius: 999px;
    border: none;
    box-shadow: 0 8px 20px rgba(37,99,235,0.45);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.stButton>button:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 25px rgba(37,99,235,0.6);
}

/* Prediction result box */
.pred-box {
    padding: 1.5rem;
    border-radius: 14px;
    background: #ecfdf5;
    border-left: 5px solid #10b981;
    box-shadow: 0 6px 14px rgba(5,150,105,0.2);
    animation: popIn 0.35s ease;
}

/* Animations */
@keyframes fadeIn {
    from {opacity:0; transform: translateY(6px);}
    to {opacity:1; transform: translateY(0);}
}
@keyframes popIn {
    0% {opacity:0; transform: scale(0.97);}
    100% {opacity:1; transform: scale(1);}
}
</style>
""",
    unsafe_allow_html=True,
)

# -------------------------
# Top nav bar (company style)
# -------------------------
st.markdown(
    """
<div class="navbar">
  <div class="nav-left">
    <span style="font-size:1.2rem;">🛡️</span>
    <span>S.H.I.E.L.D Insurance</span>
    <span class="nav-badge">Premium Estimator</span>
  </div>
  <div class="nav-right">
    Trusted pricing support for underwriting & advisory teams
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------
# Sidebar – company-style info
# -------------------------
with st.sidebar:
    st.markdown("### About this App")
    st.write(
        """
        The **Premium Estimator** uses a machine learning model trained on
        50,000+ anonymised policy records to provide indicative health
        insurance pricing.
        """
    )
    st.markdown("#### How it works")
    st.markdown(
        """
        - Enter your demographic and lifestyle details
        - Our AI model evaluates risk factors
        - You get an instant premium estimate
        """
    )
    st.markdown("---")
    st.caption("Portfolio Project · Built by Ruchitha as part of CodeBasics Bootcamp")
# -------------------------
# Hero section (metrics removed)
# -------------------------
st.markdown(
    """
<div class="hero">
  <div class="hero-left">
    <div class="hero-pill">
      <span>⚙️</span> 
      <span>Data-driven premium insights</span>
    </div>
    <div class="hero-title">Health Insurance Cost Predictor</div>
    <div class="hero-subtitle">
      Simulate annual premiums for individual policyholders based on 
      demographics, medical history and coverage selections.
    </div>
  </div>
  <div class="hero-right">
    <div class="hero-card">
      <div class="hero-card-title">Example premium (reference profile)</div>
      <div class="hero-card-value">₹ 14,500<span style="font-size:0.95rem; font-weight:500;"> / year</span></div>
      <div class="hero-card-note">
        Age 30 · Non-smoker · Normal BMI · Bronze plan · No pre-existing disease  
        <br/>
        <span style="font-size:0.8rem; color:#9ca3af;">Use the form below to simulate other profiles.</span>
      </div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------
# ORIGINAL business logic / inputs
# -------------------------
categorical_options = {
    "Gender": ["Male", "Female"],
    "Marital Status": ["Unmarried", "Married"],
    "BMI Category": ["Normal", "Obesity", "Overweight", "Underweight"],
    "Smoking Status": ["No Smoking", "Regular", "Occasional"],
    "Employment Status": ["Salaried", "Self-Employed", "Freelancer", ""],
    "Region": ["Northwest", "Southeast", "Northeast", "Southwest"],
    "Medical History": [
        "No Disease",
        "Diabetes",
        "High blood pressure",
        "Diabetes & High blood pressure",
        "Thyroid",
        "Heart disease",
        "High blood pressure & Heart disease",
        "Diabetes & Thyroid",
        "Diabetes & Heart disease",
    ],
    "Insurance Plan": ["Bronze", "Silver", "Gold"],
}

# -------------------------
# Section 1 – Customer profile (now includes Gender & Marital Status)
# -------------------------
st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-title">Customer Profile</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">Core demographic and income information for the policyholder.</div>',
    unsafe_allow_html=True,
)

row1 = st.columns(4)
with row1[0]:
    age = st.number_input("Age", min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input(
        "Number of Dependants", min_value=0, step=1, max_value=20
    )
with row1[2]:
    income_lakhs = st.number_input(
        "Income in Lakhs", step=1, min_value=0, max_value=200
    )
with row1[3]:
    region = st.selectbox("Region", categorical_options["Region"])

row1b = st.columns(3)
with row1b[0]:
    gender = st.selectbox("Gender", categorical_options["Gender"])
with row1b[1]:
    marital_status = st.selectbox(
        "Marital Status", categorical_options["Marital Status"]
    )
with row1b[2]:
    st.write("")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Section 2 – Health & lifestyle
# -------------------------
st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-title">Health & Lifestyle</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">Risk factors captured from BMI, smoking habits and medical history.</div>',
    unsafe_allow_html=True,
)

row2 = st.columns(4)
with row2[0]:
    bmi_category = st.selectbox("BMI Category", categorical_options["BMI Category"])
with row2[1]:
    smoking_status = st.selectbox(
        "Smoking Status", categorical_options["Smoking Status"]
    )
with row2[2]:
    genetical_risk = st.number_input(
        "Genetical Risk", step=1, min_value=0, max_value=5
    )
with row2[3]:
    medical_history = st.selectbox(
        "Medical History", categorical_options["Medical History"]
    )

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Section 3 – Employment details
# -------------------------
st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-title">Employment Details</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">Employment status used as part of pricing.</div>',
    unsafe_allow_html=True,
)

row3 = st.columns(3)
with row3[0]:
    employment_status = st.selectbox(
        "Employment Status", categorical_options["Employment Status"]
    )
with row3[1]:
    st.write("")
with row3[2]:
    st.write("")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Section 4 – Plan details
# -------------------------
st.markdown(
    '<div class="section-card">',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-title">Plan Details</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-subtitle">Coverage choice used for premium estimation.</div>',
    unsafe_allow_html=True,
)

row4 = st.columns(3)
with row4[0]:
    insurance_plan = st.selectbox(
        "Insurance Plan", categorical_options["Insurance Plan"]
    )
with row4[1]:
    st.write("")
with row4[2]:
    st.write("")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# input_dict (unchanged)
# -------------------------
input_dict = {
    "Age": age,
    "Number of Dependants": number_of_dependants,
    "Income in Lakhs": income_lakhs,
    "Genetical Risk": genetical_risk,
    "Insurance Plan": insurance_plan,
    "Employment Status": employment_status,
    "Gender": gender,
    "Marital Status": marital_status,
    "BMI Category": bmi_category,
    "Smoking Status": smoking_status,
    "Region": region,
    "Medical History": medical_history,
}

# -------------------------
# Prediction section
# -------------------------
st.markdown("---")

col_btn, col_result = st.columns([1, 3])

with col_btn:
    if st.button("Get Premium Estimate"):
        prediction = predict(input_dict)

        with col_result:
            st.markdown("#### Estimated Annual Premium")
            st.markdown(
                f"""
                <div class="pred-box">
                    <div style="font-size:0.95rem; color:#047857; margin-bottom:0.25rem;">
                        S.H.I.E.L.D model estimate
                    </div>
                    <div style="font-size:2.2rem; font-weight:700; color:#065f46;">
                        ₹ {prediction:,.0f}
                    </div>
                    <div style="font-size:0.9rem; color:#047857; margin-top:0.1rem;">
                        per year
                    </div>
                    <div style="font-size:0.78rem; color:#6b7280; margin-top:0.6rem;">
                        This is an estimated premium based on modelled risk factors and may differ 
                        from final quotes, which also reflect underwriting rules and current pricing.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
