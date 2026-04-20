import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique", layout="wide")

# ESTILO "LUXURY OXFORD" (MÁXIMA ELEGANCIA Y VISIBILIDAD)
st.markdown("""
    <style>
    /* Fondo Gris Oxford con degradado sutil */
    .main { 
        background-color: #0f0f0f;
        background-image: radial-gradient(circle at center, #1a1a1a 0%, #0a0a0a 100%);
        color: #e0e0e0; 
    }
    [data-testid="stAppViewContainer"] { 
        background-color: #0f0f0f;
    }
    
    /* Logo Estilo Joyería */
    .logo-main {
        font-family: 'serif';
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: 15px;
        background: linear-gradient(145deg, #fdfcfb 0%, #e2d1c3 25%, #d4af37 50%, #aa8a2e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    /* Tarjetas de Cristal Esmerilado */
    .product-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 30px;
        text-align: center;
        border-radius: 20px;
        backdrop-filter: blur(15px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        transition: 0.5s ease;
    }
    
    .product-card:hover {
        border-color: #d4af37;
        background: rgba(212, 175, 55, 0.05);
        transform: translateY(-10px);
    }

    /* Textos nítidos */
    .product-title {
        color: #d4af37;
        font-size: 1.3rem;
        font-family: 'serif';
        letter-spacing: 3px;
        margin-top: 20px;
    }
    
    .price-tag {
        color: #ffffff;
        font-size: 1.5rem;
        font-weight: 200;
        margin: 10px 0 20px 0;
    }

    /* Botón de lujo */
    .stButton>button {
        background: #d4af37 !important;
        color: #000000 !important;
        border-radius: 50px !important; /* Estilo cápsula moderna */
        font-weight: bold !important;
        letter-spacing: 2px;
        border: none !important;
        height: 45px;
        width: 100%;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background: #ffffff !important;
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.6);
    }

    /* Horóscopo */
    .stTabs [data-baseweb="tab"] { color: #888; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; }
    
    /* Imágenes con sombra suave */
    [data-testid="stImage"] img {
        filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.8));
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<h1 class="logo-main">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #d4af37; letter-spacing: 8px; font-size: 0.7rem; margin-bottom: 50px;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# --- PRODUCTOS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=200)
    st.markdown('<div class="product-title">ORÁCULO</div><div class="
