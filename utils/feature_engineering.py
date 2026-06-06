# ============================================================
# utils/feature_engineering.py
# ============================================================
import pandas as pd
import numpy as np

def add_engineered_features(df):
    df = df.copy()
    
    if 'Tenure' in df.columns and 'OrderCount' in df.columns and 'SatisfactionScore' in df.columns:
        df['LoyaltyScore'] = (df['Tenure'].clip(0, 12) / 12 * 30 +
                              df['OrderCount'].clip(0, 20) / 20 * 40 +
                              df['SatisfactionScore'].clip(1, 5) / 5 * 30)
        df['LoyaltyScore'] = df['LoyaltyScore'].clip(0, 100)
    
    if 'HourSpendOnApp' in df.columns and 'NumberOfDeviceRegistered' in df.columns:
        df['EngagementScore'] = (df['HourSpendOnApp'].clip(0, 100) / 100 * 60 +
                                 df['NumberOfDeviceRegistered'].clip(0, 5) / 5 * 40)
        df['EngagementScore'] = df['EngagementScore'].clip(0, 100)
    
    if 'Complain' in df.columns and 'SatisfactionScore' in df.columns:
        df['ComplaintRiskScore'] = df['Complain'] * 70 + (5 - df['SatisfactionScore']) * 6
        df['ComplaintRiskScore'] = df['ComplaintRiskScore'].clip(0, 100)
    
    if 'CouponUsed' in df.columns and 'CashbackAmount' in df.columns:
        df['DiscountDependencyScore'] = (df['CouponUsed'].clip(0, 10) / 10 * 50 +
                                         df['CashbackAmount'].clip(0, 500) / 500 * 50)
        df['DiscountDependencyScore'] = df['DiscountDependencyScore'].clip(0, 100)
    
    if 'DaySinceLastOrder' in df.columns:
        df['RecencyScore'] = np.where(df['DaySinceLastOrder'] <= 7, 100,
                                      np.where(df['DaySinceLastOrder'] <= 30, 70,
                                               np.where(df['DaySinceLastOrder'] <= 90, 40, 10)))
    
    if 'OrderAmountHikeFromlastYear' in df.columns and 'CashbackAmount' in df.columns and 'OrderCount' in df.columns:
        df['CustomerValueScore'] = (df['OrderAmountHikeFromlastYear'].clip(0, 100) / 100 * 40 +
                                    df['CashbackAmount'].clip(0, 500) / 500 * 30 +
                                    df['OrderCount'].clip(0, 20) / 20 * 30)
        df['CustomerValueScore'] = df['CustomerValueScore'].clip(0, 100)
    
    return df

def get_feature_columns():
    base_cols = ['Tenure', 'PreferredLoginDevice', 'CityTier', 'WarehouseToHome',
                 'PreferredPaymentMode', 'Gender', 'HourSpendOnApp', 'NumberOfDeviceRegistered',
                 'PreferredOrderCat', 'SatisfactionScore', 'MaritalStatus', 'NumberOfAddress',
                 'Complain', 'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount',
                 'DaySinceLastOrder', 'CashbackAmount']
    engineered = ['CustomerValueScore', 'LoyaltyScore', 'EngagementScore',
                  'ComplaintRiskScore', 'DiscountDependencyScore', 'RecencyScore']
    return base_cols + engineered