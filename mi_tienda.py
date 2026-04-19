import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury Boutique", page_icon="💎", layout="centered")

# 2. SISTEMA DE ESTILO "OPHAY LUXE"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@200;400;600&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

    .stApp {
        background-color: #ffffff;
    }
    
    .title-gold {
        font-family: 'Cinzel', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 400;
        font-size: 52px !important;
        letter-spacing: 12px;
        margin-top: 60px;
        margin-bottom: 5px;
    }

    .subtitle-luxury {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        text-align: center;
        letter-spacing: 5px;
        font-size: 10px;
        text-transform: uppercase;
        margin-bottom: 80px;
    }

    h3 {
        font-family: 'Inter', sans-serif !important;
        color: #111827 !important; 
        font-weight: 600 !important;
        letter-spacing: 2px;
        font-size: 16px !important;
        text-transform: uppercase;
        margin-bottom: 10px !important;
    }
    
    .desc {
        font-family: 'Playfair Display', serif !important;
        color: #4b5563 !important;
        font-size: 14px !important;
        font-style: italic;
        line-height: 2;
        font-weight: 300;
        margin-bottom: 20px !important;
    }

    .precio {
        font-family: 'Inter', sans-serif !important;
        color: #111827 !important; 
        font-weight: 400;
        font-size: 19px;
        letter-spacing: 1px;
        margin-bottom: 25px !important;
    }
    
    div.stButton > button {
        background-color: #ffffff !important;
        color: #111827 !important;
        font-family: 'Inter', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        font-weight: 400;
        font-size: 11px;
        border-radius: 0px !important;
        border: 1px solid #e5e7eb !important;
        padding: 20px 40px;
        width: 100%;
        transition: all 0.5s ease;
    }
    
    div.stButton > button:hover {
        background-color: #111827 !important;
        color: #ffffff !important;
        border-color: #111827 !important;
        letter-spacing: 6px;
    }

    [data-testid="stHorizontalBlock"] {
        padding: 60px 0px;
        border-bottom: 1px solid #f3f4f6;
        align-items: center;
