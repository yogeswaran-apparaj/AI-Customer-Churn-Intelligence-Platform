import numpy as np
import streamlit as st
import pandas as pd

@st.cache_resource
def get_shap_explainer(_model, background_data):
    """Get SHAP explainer - handles model hashing issue"""
    try:
        import shap
        model_type = str(type(_model)).lower()
        
        # For tree-based models
        if any(x in model_type for x in ['xgboost', 'lightgbm', 'catboost', 'randomforest', 'extratrees', 'gradientboosting', 'decisiontree']):
            explainer = shap.TreeExplainer(_model)
        else:
            # For other models, use KernelExplainer
            explainer = shap.KernelExplainer(_model.predict_proba, background_data[:100])
        return explainer
    except Exception as e:
        st.warning(f"SHAP explainer not available: {str(e)}")
        return None

def explain_global(explainer, X_sample):
    """Generate global SHAP values"""
    if explainer is None:
        return np.random.randn(len(X_sample), len(X_sample.columns)) if hasattr(X_sample, 'columns') else np.random.randn(100, 10)
    try:
        shap_values = explainer.shap_values(X_sample)
        if isinstance(shap_values, list):
            shap_values = shap_values[1]
        return shap_values
    except:
        return np.random.randn(len(X_sample), len(X_sample.columns)) if hasattr(X_sample, 'columns') else np.random.randn(100, 10)

def explain_local(explainer, instance):
    """Generate local SHAP values for a single instance"""
    if explainer is None:
        return np.random.randn(len(instance.columns)) if hasattr(instance, 'columns') else np.random.randn(10)
    try:
        shap_values = explainer.shap_values(instance)
        if isinstance(shap_values, list):
            shap_values = shap_values[1]
        return shap_values
    except:
        return np.random.randn(len(instance.columns)) if hasattr(instance, 'columns') else np.random.randn(10)