import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique", layout="wide")

# ESTILO "LUXURY ANTRACITA" (MÁS LUZ Y SIN ERRORES)
st.markdown("""
    <style>
    .main { 
        background-color: #121212;
        background-image: radial-gradient(circle, #1f1f1f 0%, #0d0d0d 100%);
        color: #f0f0f0; 
    }
    [data-testid="stAppViewContainer"] { background-color: #121212; }
    
    .logo-main {
        font-family: 'serif';
        text-align: center;
        font-size: 3.5rem;
        letter-spacing: 12px;
        background: linear-gradient(145deg, #ffffff 0%, #d4af37 50%, #aa8a2e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin-bottom: 0px;
    }

    .product-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 20px;
        text-align: center;
        border-radius: 15px;
        transition: 0.3s;
    }
    
    .product-card:hover {
        border-color: #d4af37;
        background: rgba(212, 175, 55, 0.1);
    }

    .product-title {
        color: #d4af37;
        font-size: 1.2rem;
        letter-spacing: 2px;
        margin-top: 15px;
    }

    .stButton>button {
        background: #d4af37 !important;
        color: #000 !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        border: none !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        background: #fff !important;
        box-shadow: 0px 0px 15px #d4af37;
    }

    .stTabs [data-baseweb="tab"] { color: #aaa; font-weight: bold; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<h1 class="logo-main">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#d4af37; letter-spacing:8px; font-size:0.8rem; margin-bottom:30px;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# --- PRODUCTOS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=180)
    st.markdown('<div class="product-title">ORÁCULO</div><div style="font-size:1.3rem; margin-bottom:10px;">25€</div>', unsafe_allow_html=True)
    st.link_button
