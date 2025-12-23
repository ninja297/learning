import streamlit as st
from config.app_config import PRIMARY_COLOR, SECONDARY_COLOR
import requests
import time


def show_footer(in_sidebar=False):
    base_styles = f"""
        text-align: center;
        padding: 0.5rem;
        background: linear-gradient(to right, 
            rgba(25, 118, 210, 0.03), 
            rgba(100, 181, 246, 0.05), 
            rgba(25, 118, 210, 0.03)
        );
        border-top: 1px solid rgba(100, 181, 246, 0.15);
        margin-top: {'0' if in_sidebar else '2rem'};
        {'width: 100%' if not in_sidebar else ''};
        box-shadow: 0 -2px 10px rgba(100, 181, 246, 0.05);
    """

    st.markdown(
        f"""
        <div style="{base_styles}"></div>
        """,
        unsafe_allow_html=True
    )
