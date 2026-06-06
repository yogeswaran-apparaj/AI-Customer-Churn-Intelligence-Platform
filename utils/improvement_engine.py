# ============================================================
# utils/improvement_engine.py
# ============================================================
def get_improvement_suggestions(customer_data, current_prob, current_risk):
    suggestions = []
    
    suggestions.append({
        'feature': 'SatisfactionScore',
        'current': customer_data.get('SatisfactionScore', 3),
        'suggested': min(5, customer_data.get('SatisfactionScore', 3) + 1),
        'expected_reduction': 0.15,
        'action': 'Proactive support calls & loyalty rewards program'
    })
    
    suggestions.append({
        'feature': 'DaySinceLastOrder',
        'current': customer_data.get('DaySinceLastOrder', 30),
        'suggested': max(5, customer_data.get('DaySinceLastOrder', 30) - 10),
        'expected_reduction': 0.10,
        'action': 'Send personalized promo with free shipping'
    })
    
    suggestions.append({
        'feature': 'CashbackAmount',
        'current': customer_data.get('CashbackAmount', 50),
        'suggested': customer_data.get('CashbackAmount', 50) + 100,
        'expected_reduction': 0.08,
        'action': 'Double cashback on next purchase'
    })
    
    return suggestions

def calculate_improvement_potential(suggestions):
    total_reduction = sum(s['expected_reduction'] for s in suggestions)
    return min(total_reduction, 0.8)  # Max 80% reduction