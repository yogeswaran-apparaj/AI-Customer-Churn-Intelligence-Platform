import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from utils.feature_engineering import add_engineered_features, get_feature_columns

def preprocess_uploaded_data(df, scaler, encoders):
    """Preprocess uploaded data for prediction"""
    df_processed = df.copy()
    
    # Extract CustomerID if exists
    if 'CustomerID' in df_processed.columns:
        customer_ids = df_processed['CustomerID']
        df_processed = df_processed.drop(columns=['CustomerID'])
    else:
        customer_ids = None
    
    # Handle missing values
    numeric_cols = df_processed.select_dtypes(include=[np.number]).columns
    categorical_cols = df_processed.select_dtypes(include=['object']).columns
    
    for col in numeric_cols:
        df_processed[col] = df_processed[col].fillna(df_processed[col].median() if not df_processed[col].isnull().all() else 0)
    
    for col in categorical_cols:
        df_processed[col] = df_processed[col].fillna(df_processed[col].mode()[0] if not df_processed[col].mode().empty else 'Unknown')
    
    # Encode categorical variables
    for col, encoder in encoders.items():
        if col in df_processed.columns:
            if hasattr(encoder, 'classes_'):
                # Map unknown categories to first class
                df_processed[col] = df_processed[col].apply(lambda x: x if x in encoder.classes_ else encoder.classes_[0])
                df_processed[col] = encoder.transform(df_processed[col])
    
    # Add engineered features
    df_processed = add_engineered_features(df_processed)
    
    # Ensure all required features exist
    required_features = get_feature_columns()
    for feat in required_features:
        if feat not in df_processed.columns:
            df_processed[feat] = 0
    
    # Select only required features
    df_processed = df_processed[required_features]
    
    # Scale features if scaler exists
    if scaler is not None:
        try:
            df_processed_scaled = pd.DataFrame(scaler.transform(df_processed), columns=required_features)
        except:
            df_processed_scaled = df_processed
    else:
        df_processed_scaled = df_processed
    
    return df_processed_scaled, customer_ids

def validate_dataset(df):
    """Validate dataset and return quality report"""
    report = {
        'shape': df.shape,
        'columns': list(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        'duplicates': df.duplicated().sum(),
        'data_types': df.dtypes.astype(str).to_dict(),
        'quality_score': 0
    }
    
    # Calculate quality score
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()
    missing_pct = (missing_cells / total_cells) * 100 if total_cells > 0 else 0
    duplicate_pct = (report['duplicates'] / df.shape[0]) * 100 if df.shape[0] > 0 else 0
    
    score = 100 - (missing_pct * 0.5) - (duplicate_pct * 0.5)
    report['quality_score'] = max(0, min(100, score))
    
    return report