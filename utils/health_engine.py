# ============================================================
# utils/health_engine.py
# ============================================================
import numpy as np

def compute_health_score(churn_probability, loyalty_score, engagement_score, complaint_risk):
    health = (1 - churn_probability) * 50
    health += (loyalty_score / 100) * 20
    health += (engagement_score / 100) * 20
    health -= (complaint_risk / 100) * 10
    return np.clip(health, 0, 100)

def get_health_category(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
    elif score >= 20:
        return "Poor"
    else:
        return "Critical"

def get_health_color(score):
    if score >= 80:
        return "#10B981"
    elif score >= 60:
        return "#3B82F6"
    elif score >= 40:
        return "#F59E0B"
    elif score >= 20:
        return "#EF4444"
    else:
        return "#7F1D1D"