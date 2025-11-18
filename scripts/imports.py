# scripts/imports.py

# Common scientific libraries
import pandas as pd
import numpy as np
import math

# Visualization
from matplotlib import pyplot as plt
import seaborn as sns

# Preprocessing
from sklearn.preprocessing import MinMaxScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Model training
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

# Evaluation
from sklearn.metrics import r2_score, mean_squared_error

# File helpers
from joblib import dump, load

# Parquet helper
def load_parquet(path):
    """Load a parquet file safely."""
    return pd.read_parquet(path)

def save_parquet(df, path):
    """Save parquet with a consistent pattern."""
    df.to_parquet(path, index=False)

# Joblib helper
def load_model(path):
    """Uniform loader for joblib models."""
    return load(path)

def save_model(obj, path):
    """Uniform saver for joblib models."""
    dump(obj, path)
