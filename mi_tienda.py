import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique", layout="wide")

# ESTILO LUXE CON ILUMINACIÓN (VIBRANTE)
st.markdown("""
    <style>
    .main { background-color: #050505; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    /* Título con degradado de oro real */
    .logo-main {
        background: linear-gradient(to bottom, #fcf6ba 0%, #d4af37 40%, #aa8a2e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        letter-spacing: 12px;
        font-family: 'serif';
        text-align: center;
        margin: 0;
        font-weight: bold;
    }

    /* Tarjetas con resplandor (Glow) */
    .product-card {
        background: #0a0a0a;
        border: 1px solid #221d14;
        padding: 30px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.05); /* Luz ambiental suave */
        transition: all 0.5s ease;
    }
    
    .product-card:hover {
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.2); /* Brilla al acercarse */
        border-color: #d4af37;
    }

    .product-title {
        color: #d4af37;
        font-size: 1.2rem;
        letter-spacing: 3px;
        margin: 20px 0 10px 0;
        font-family: 'serif';
    }

    /* Botón con efecto de luz */
    .stButton>button {
        background: linear-gradient(145deg, #d4af37, #b8962e) !important;
        color: #000000 !important;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        border: none !important;
        border-radius: 4px !important;
        width: 100%;
        height: 48px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    
    .stButton>button:hover {
        background: #ffffff !important;
        box-shadow: 0px 0px 20px #d4af37; /* Destello dorado */
    }

    /* Imágenes con marco de luz */
    [data-testid="stImage"] img {
        border-radius: 5px;
        border: 1px solid #332b1a;
        transition: border 0.5s;
    }
    .product-card:hover img {
        border-color: #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

# CABECERA ILUMINADA
st.markdown('<div style="text-align:center; padding: 40px 0;"><h1 class="logo-main">OPHAY</h1><p style="color: #d4af37; letter-spacing: 6px; font-size: 0.8rem; opacity: 0.6;">ALTA CLARIVIDENCIA • BARCELONA</p></div>', unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=220)
    st.markdown('<div class="product-title">ORÁCULO</div>', unsafe_allow_html
