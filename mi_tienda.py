import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique", layout="wide")

# ESTILO LUXURY GRAFITO (MÁS LUZ Y ELEGANCIA)
st.markdown("""
    <style>
    .main { 
        background-color: #111111;
        background-image: radial-gradient(circle, #1c1c1c 0%, #0a0a0a 100%);
        color: #e0e0e0; 
    }
    [data-testid="stAppViewContainer"] { background-color: #111111; }
    
    .logo-main {
        font-family: 'serif';
        text-align: center;
        font-size: 3.5rem;
        letter-spacing: 12px;
        background: linear-gradient(145deg, #fdfcfb 0%, #d4af37 50%, #aa8a2e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin: 0;
    }

    .product-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 20px;
        text-align: center;
        border-radius: 15px;
        transition: 0.4s ease;
    }
    
    .product-card:hover {
        border-color: #d4af37;
        background: rgba(212, 175, 55, 0.08);
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.2);
    }

    .product-title {
        color: #d4af37;
        font-size: 1.1rem;
        font-family: 'serif';
        letter-spacing: 2px;
        margin-top: 15px;
    }
    
    .price-tag {
        color: #ffffff;
        font-size: 1.3rem;
        margin-bottom: 15px;
    }

    .stButton>button {
        background: #d4af37 !important;
        color: #000000 !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        letter-spacing: 2px;
        border: none !important;
        height: 42px;
        width: 100%;
    }
    
    .stButton>button:hover {
        background: #ffffff !important;
        box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.5);
    }

    .stTabs [data-baseweb="tab"] { color: #888; font-size: 0.9rem; font-weight: bold; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<h1 class="logo-main">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#d4af37; letter-spacing:8px; font-size:0.8rem; margin-bottom:40px;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# --- PRODUCTOS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=190)
    st.markdown('<div class="product-title">ORÁCULO</div><div class="price-tag">25€</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=190)
    st.markdown('<div class="product-title">RIDER LUXE</div><div class="price-tag">45€</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", width=190)
    st.markdown('<div class="product-title">AMATISTA</div><div class="price-tag">15€</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

# --- HORÓSCOPO ---
st.markdown("---")
st.markdown('<h2 style="text-align:center
