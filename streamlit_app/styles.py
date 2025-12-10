import streamlit as st
import plotly.io as pio

def load_css():
    st.markdown("""
        <style>
            .main-header {
                text-align: center;
                padding: 2rem 0 1rem 0;
                background: linear-gradient(135deg, #FF0000 0%, #CC0000 100%);
                border-radius: 12px;
                margin-bottom: 2rem;
                box-shadow: 0 4px 20px rgba(255, 0, 0, 0.3);
            }
            .main-header h1 {
                color: white !important;
                font-size: 2.5rem !important;
                margin-bottom: 0.5rem !important;
                font-weight: 700 !important;
            }
            .main-header p {
                color: rgba(255, 255, 255, 0.9) !important;
                font-size: 1.1rem !important;
            }
            
            .metric-container {
                background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
                padding: 1.5rem;
                border-radius: 12px;
                text-align: center;
                border: 1px solid #333;
                transition: all 0.3s ease;
                height: 100%;
            }
            .metric-container:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 25px rgba(255, 0, 0, 0.4);
                border-color: #FF0000;
            }
            .metric-value {
                color: #FF0000;
                font-size: 2rem;
                font-weight: 700;
            }
            
            .section-header {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                margin: 2.5rem 0 1.5rem 0;
                padding-bottom: 0.75rem;
                border-bottom: 2px solid #FF0000;
            }
            .section-header h3 {
                color: #FAFAFA !important;
                font-size: 1.5rem !important;
                margin: 0 !important;
                font-weight: 600 !important;
            }
            
            .highlight-box {
                background: linear-gradient(135deg, #FF0000 0%, #CC0000 100%);
                color: white;
                padding: 2rem;
                border-radius: 16px;
                box-shadow: 0 8px 30px rgba(255, 0, 0, 0.4);
                transition: all 0.3s ease;
            }
            .highlight-box:hover {
                transform: scale(1.02);
                box-shadow: 0 12px 40px rgba(255, 0, 0, 0.5);
            }
            .highlight-box h3 {
                font-size: 1.3rem !important;
                margin-bottom: 1rem !important;
                font-weight: 600 !important;
                line-height: 1.4 !important;
            }
            .highlight-box h2 {
                font-size: 2.5rem !important;
                margin: 1rem 0 1.5rem 0 !important;
                font-weight: 700 !important;
            }
            
            .watch-button {
                background: white !important;
                color: #FF0000 !important;
                padding: 12px 32px !important;
                border: none !important;
                border-radius: 30px !important;
                font-weight: 700 !important;
                transition: all 0.3s ease !important;
            }
            .watch-button:hover {
                background: #FFEBEB !important;
                transform: translateY(-2px) !important;
            }
        </style>
    """, unsafe_allow_html=True)

def apply_plotly_theme():
    pio.templates["youtube_red"] = pio.templates["plotly_dark"]

    pio.templates["youtube_red"].layout.update(
        {
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "font": {"color": "#FAFAFA"},
            "colorway": [
                "#FF0000", "#CC0000", "#FF4D4D", "#FF6666",
                "#B30000", "#990000", "#FF1A1A"
            ],
            "xaxis": {"gridcolor": "#333"},
            "yaxis": {"gridcolor": "#333"},
        }
    )

    pio.templates.default = "youtube_red"
