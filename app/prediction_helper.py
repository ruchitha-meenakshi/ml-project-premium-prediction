# codebasics ML course: codebasics.io, all rights reserverd

from pathlib import Path
import pandas as pd
import joblib

# ---------------------------------------------------------
# Fix paths after moving into app/ folder
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent      # .../ml-project-premium-prediction/app
REPO_ROOT = BASE_DIR.parent                     # .../ml-project-premium-prediction
ARTIFACTS_DIR = REPO_ROOT / "artifacts"

model_young = joblib.load(ARTIFACTS_DIR / "model_young.joblib")
model_rest = joblib.load(ARTIFACTS_DIR / "model_rest.joblib")
scaler_young = joblib.load(ARTIFACTS_DIR / "scaler_young.joblib")
scaler_rest = joblib.load(ARTIFACTS_DIR / "scaler_rest.joblib")
#model_young = joblib.load("artifacts/model_young.joblib")
#model_rest = joblib.load("artifacts/model_rest.joblib")
#scaler_young = joblib.load("artifacts/scaler_young.joblib")
#scaler_rest = joblib.load("artifacts/scaler_rest.joblib")

def calculate_normalized_risk(medical_history):
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    # Split the medical history into potential two parts and convert to lowercase
    diseases = medical_history.lower().split(" & ")

    # Calculate the total risk score by summing the risk scores for each part
    total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)  # Default to 0 if disease not found

    max_score = 14 # risk score for heart disease (8) + second max risk score (6) for diabetes or high blood pressure
    min_score = 0  # Since the minimum score is always 0

    # Normalize the total risk score
    normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)

    return normalized_risk_score

# def encode_bmi_category(category: str) -> int:
#     bmi_map = {
#         "Underweight": 1,
#         "Normal": 2,
#         "Overweight": 3,
#         "Obesity": 4
#     }
#     return bmi_map.get(category, 1)

def preprocess_input(input_dict):
    # Define the expected columns and initialize the DataFrame with zeros
    expected_columns = [
        'age', 'number_of_dependants', 'bmi_category', 'income_lakhs',
        'insurance_plan','genetical_risk','normalized_risk_score',
        'gender_male', 'region_northwest','region_southeast',
        'region_southwest','marital_status_unmarried','smoking_status_occasional',
        'smoking_status_regular','employment_status_salaried', 'employment_status_self-employed'
    ]
    bmi_category_encoding = {'Underweight': 1, 'Normal': 2, 'Overweight': 3,'Obesity': 4}
    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}

    df = pd.DataFrame(0, columns=expected_columns, index=[0])
    # df.fillna(0, inplace=True)

    # Manually assign values for each categorical input based on input_dict
    for key, value in input_dict.items():
        if key == 'Gender' and value == 'Male':
            df['gender_male'] = 1
        elif key == 'Region':
            if value == 'Northwest':
                df['region_northwest'] = 1
            elif value == 'Southeast':
                df['region_southeast'] = 1
            elif value == 'Southwest':
                df['region_southwest'] = 1
        elif key == 'Marital Status' and value == 'Unmarried':
            df['marital_status_unmarried'] = 1
        elif key == 'Smoking Status':
            if value == 'Occasional':
                df['smoking_status_occasional'] = 1
            elif value == 'Regular':
                df['smoking_status_regular'] = 1
        elif key == 'Employment Status':
            if value == 'Salaried':
                df['employment_status_salaried'] = 1
            elif value == 'Self-Employed':
                df['employment_status_self-employed'] = 1
        elif key == 'Insurance Plan':  # Correct key usage with case sensitivity
            df['insurance_plan'] = insurance_plan_encoding.get(value, 1)
        elif key == 'BMI Category':
            df['bmi_category'] = bmi_category_encoding.get(value, 1)
        elif key == 'Age':  # Correct key usage with case sensitivity
            df['age'] = value
        elif key == 'Number of Dependants':  # Correct key usage with case sensitivity
            df['number_of_dependants'] = value
        elif key == 'Income in Lakhs':  # Correct key usage with case sensitivity
            df['income_lakhs'] = value
        elif key == "Genetical Risk":
            df['genetical_risk'] = value

    # Assuming the 'normalized_risk_score' needs to be calculated based on the 'age'
    df['normalized_risk_score'] = calculate_normalized_risk(input_dict['Medical History'])
    df = handle_scaling(input_dict['Age'], df)

    return df

def handle_scaling(age, df):
    # scale age and income_lakhs column
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    df['income_level'] = None # since scaler object expects income_level supply it. This will have no impact on anything
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    df.drop('income_level', axis='columns', inplace=True)

    return df

def predict(input_dict):
    input_df = preprocess_input(input_dict)

    if input_dict['Age'] <= 25:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    return int(prediction[0])
