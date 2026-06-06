# ============================================================
# utils/retention_strategy.py
# ============================================================
def generate_retention_strategy(churn_probability, risk_category, segment):
    strategies = {
        'Critical': {
            'strategy': '🚨 Immediate High-Touch Intervention',
            'priority': 'P0 - Critical',
            'impact': 'Very High (70-90% recovery)',
            'justification': 'Customer likely to churn within 7 days. Requires immediate executive outreach.'
        },
        'High': {
            'strategy': '🎯 Personalized Win-Back Campaign',
            'priority': 'P1 - High',
            'impact': 'High (50-70% recovery)',
            'justification': 'High risk customers respond well to exclusive premium offers.'
        },
        'Medium': {
            'strategy': '📧 Automated Engagement Nurture',
            'priority': 'P2 - Medium',
            'impact': 'Medium (30-50% recovery)',
            'justification': 'Regular personalized communication with relevant offers.'
        },
        'Low': {
            'strategy': '⭐ Loyalty Program Incentives',
            'priority': 'P3 - Low',
            'impact': 'Low (10-30% recovery)',
            'justification': 'Maintain satisfaction through standard loyalty benefits.'
        },
        'Very Low': {
            'strategy': '📈 Cross-sell & Upsell Opportunities',
            'priority': 'P4 - Monitoring',
            'impact': 'Low (<10% recovery)',
            'justification': 'Focus on increasing customer lifetime value.'
        }
    }
    return strategies.get(risk_category, strategies['Medium'])

def get_strategy_priority_color(priority):
    colors = {
        'P0': '#EF4444',
        'P1': '#F59E0B',
        'P2': '#3B82F6',
        'P3': '#10B981',
        'P4': '#64748B'
    }
    return colors.get(priority.split('-')[0], '#64748B')