import streamlit as st

def apply_premium_css():
    st.markdown("""
    <style>
    /* Reset and base */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
    }
    
    /* Main container padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
        border-right: 1px solid rgba(37,99,235,0.2);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdown"] {
        color: #F8FAFC;
    }
    
    /* Sidebar header */
    .sidebar-header {
        padding: 1.5rem 1rem;
        border-bottom: 1px solid rgba(37,99,235,0.3);
        margin-bottom: 1rem;
    }
    
    .logo-container {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .logo-icon {
        font-size: 2.5rem;
        filter: drop-shadow(0 0 10px rgba(37,99,235,0.5));
    }
    
    .logo-text {
        font-size: 1.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #2563EB, #7C3AED, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.3;
    }
    
    /* Sidebar footer */
    .sidebar-footer {
        position: fixed;
        bottom: 20px;
        left: 20px;
        padding: 1rem;
    }
    
    .status-indicator {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.75rem;
        color: #10B981;
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        background: #10B981;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
    }
    
    .version-info {
        font-size: 0.7rem;
        color: #64748B;
        margin-top: 8px;
    }
    
    /* Hero section */
    .hero-section {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(37,99,235,0.1), rgba(124,58,237,0.1));
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 1px solid rgba(37,99,235,0.2);
    }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #2563EB, #7C3AED, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #94A3B8;
    }
    
    /* KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, #1E293B, #0F172A);
        border-radius: 16px;
        padding: 1.2rem;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin: 0.5rem 0;
    }
    
    .kpi-card:hover {
        transform: translateY(-5px);
        border-color: #2563EB;
        box-shadow: 0 10px 30px rgba(37,99,235,0.2);
    }
    
    .kpi-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #94A3B8;
        margin-bottom: 0.5rem;
    }
    
    .kpi-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.25rem;
    }
    
    .kpi-trend {
        font-size: 0.7rem;
        color: #10B981;
    }
    
    .kpi-trend.danger {
        color: #EF4444;
    }
    
    .kpi-trend.warning {
        color: #F59E0B;
    }
    
    /* Page title */
    .page-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #2563EB, #7C3AED, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Premium cards */
    .premium-card {
        background: linear-gradient(135deg, rgba(30,41,59,0.9), rgba(15,23,42,0.9));
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.5rem;
        border: 1px solid rgba(37,99,235,0.3);
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .premium-card:hover {
        border-color: #7C3AED;
        box-shadow: 0 8px 32px rgba(124,58,237,0.2);
    }
    
    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #F8FAFC;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #1E293B;
        padding: 0.5rem;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.5rem 1rem;
        color: #94A3B8;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        color: white;
    }
    
    /* Metrics styling */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2563EB;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.8rem;
        color: #94A3B8;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        background: #1E293B;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #334155;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: 500;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(37,99,235,0.3);
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        background: #1E293B;
        border: 2px dashed #2563EB;
        border-radius: 12px;
        padding: 1rem;
    }
    
    /* Selectbox */
    .stSelectbox [data-baseweb="select"] {
        background: #1E293B;
        border-color: #334155;
    }
    
    /* Slider */
    .stSlider [data-baseweb="slider"] {
        background: #1E293B;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: #1E293B;
        border-radius: 8px;
    }
    
    /* Footer */
    .footer {
        margin-top: 3rem;
        padding: 1.5rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        text-align: center;
    }
    
    .footer-content {
        display: flex;
        justify-content: space-between;
        color: #64748B;
        font-size: 0.75rem;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 1.5rem;
        }
        .kpi-value {
            font-size: 1.2rem;
        }
        .footer-content {
            flex-direction: column;
            gap: 0.5rem;
            text-align: center;
        }
    }
    
    /* Health badges */
    .health-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.75rem;
    }
    
    .health-badge.Excellent {
        background: linear-gradient(135deg, #10B981, #059669);
        color: white;
    }
    
    .health-badge.Good {
        background: linear-gradient(135deg, #3B82F6, #2563EB);
        color: white;
    }
    
    .health-badge.Average {
        background: linear-gradient(135deg, #F59E0B, #D97706);
        color: white;
    }
    
    .health-badge.Poor {
        background: linear-gradient(135deg, #EF4444, #DC2626);
        color: white;
    }
    
    .health-badge.Critical {
        background: linear-gradient(135deg, #7F1D1D, #991B1B);
        color: white;
    }
    
    /* Loading spinner */
    .stSpinner > div {
        border-top-color: #2563EB !important;
    }
    
    /* Code blocks */
    .stCodeBlock {
        background: #1E293B;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

def apply_dark_theme():
    pass