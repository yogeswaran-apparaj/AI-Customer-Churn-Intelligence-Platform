import pickle
import joblib
import os
from pathlib import Path
import streamlit as st
import numpy as np
import pandas as pd

MODEL_DIR = Path("models")

@st.cache_resource
def load_all_models():
    """Load all models from models directory"""
    models = {}
    if MODEL_DIR.exists():
        for pkl_file in MODEL_DIR.glob("*.pkl"):
            model_name = pkl_file.stem
            try:
                # Try loading with pickle first
                with open(pkl_file, 'rb') as f:
                    models[model_name] = pickle.load(f)
                print(f"✅ Loaded model: {model_name}")
            except Exception as e1:
                try:
                    # Try with joblib
                    models[model_name] = joblib.load(pkl_file)
                    print(f"✅ Loaded model (joblib): {model_name}")
                except Exception as e2:
                    print(f"❌ Failed to load {model_name}: {str(e1)}")
    else:
        st.warning(f"Models directory '{MODEL_DIR}' not found")
    return models

@st.cache_resource
def load_scaler():
    """Load scaler if exists"""
    scaler_path = MODEL_DIR / "scaler.pkl"
    if scaler_path.exists():
        try:
            with open(scaler_path, 'rb') as f:
                return pickle.load(f)
        except:
            try:
                return joblib.load(scaler_path)
            except:
                return None
    return None

@st.cache_resource
def load_encoders():
    """Load encoders if exists"""
    encoders_path = MODEL_DIR / "encoders.pkl"
    if encoders_path.exists():
        try:
            with open(encoders_path, 'rb') as f:
                return pickle.load(f)
        except:
            try:
                return joblib.load(encoders_path)
            except:
                return {}
    return {}

def get_available_models():
    """Get list of available model names"""
    models = load_all_models()
    return list(models.keys())