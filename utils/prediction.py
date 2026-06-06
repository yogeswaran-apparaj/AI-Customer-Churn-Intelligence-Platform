import pandas as pd
import numpy as np

def predict_churn(model, features_df, threshold=0.5):
    """Predict churn for a single or multiple customers"""
    try:
        if hasattr(model, 'predict_proba'):
            proba = model.predict_proba(features_df)[:, 1]
        else:
            proba = model.predict(features_df)
        
        predictions = (proba >= threshold).astype(int) if isinstance(proba, np.ndarray) else (int(proba >= threshold))
        return predictions, proba
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        # Return default values
        n_samples = len(features_df) if hasattr(features_df, '__len__') else 1
        return np.zeros(n_samples), np.ones(n_samples) * 0.5

def predict_bulk(model, features_df, threshold=0.5):
    """Bulk prediction with risk scores"""
    predictions, probabilities = predict_churn(model, features_df, threshold)
    
    # Ensure probabilities are 1D array
    if isinstance(probabilities, (float, int)):
        probabilities = np.array([probabilities])
    
    risk_scores = probabilities * 100
    
    # Create risk categories
    risk_categories = []
    for score in risk_scores:
        if score <= 20:
            risk_categories.append('Very Low')
        elif score <= 40:
            risk_categories.append('Low')
        elif score <= 60:
            risk_categories.append('Medium')
        elif score <= 80:
            risk_categories.append('High')
        else:
            risk_categories.append('Critical')
    
    return predictions, probabilities, risk_scores, risk_categories