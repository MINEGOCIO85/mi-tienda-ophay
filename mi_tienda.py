import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique", layout="wide")

# ESTILO LUXE VIBRANTE (CORREGIDO)
st.markdown("""
    <style>
    .main { background-color: #050505; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    /* Título con degradado de oro */
    .logo-main {
        background: linear-gradient(to bottom, #fcf6ba 0%, #d4af37 40%, #aa8a2e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.2rem;
        letter-spacing: 10px;
        font-family: 'serif';
        text-align: center;
        margin: 0;
        font-weight: bold;
    }

    /* Tarjetas con resplandor suave */
    .product-card {
        background: #0a0a0a;
        border: 1px solid #221d14;
        padding: 25px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(212, 175, 55, 0.1);
        transition: all 0.4s ease;
    }
    
    .product-card:hover {
        box-shadow: 0px 0px 25px rgba(212, 175, 55, 0.3);
        border-color: #d4af37;
    }

    .product-title {
        color: #d4af37;
        font-size: 1.1rem;
        letter-spacing: 2px;
        margin: 15px 0 5px 0;
        font-family: 'serif';
    }

    /* Botón Dorado */
    .stButton>button {
        background: linear-gradient(145deg, #d4af37, #b8962e) !important;
        color: #000000 !important;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        border: none !important;
        border-radius: 4px !important;
        width: 100%;
        height: 45px;
    }
    
    .stButton>button:hover {
        background: #ffffff !important;
        box-shadow: 0px 0px 15px #d4af37;
    }

    [data-testid="stImage"] img {
        border-radius: 5px;
        border: 1px solid #332b1a;
    }
    </style>
    """, unsafe_allow_html=True)

# CABECERA
st.markdown('<div style="text-align:center; padding: 30px 0;"><h1 class="logo-main">OPHAY</h1><p style="color: #d4af37; letter-spacing: 5px; font-size: 0.8rem; opacity: 0.7;">ALTA CLARIVIDENCIA • BARCELONA</p></div>', unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=200)
    st.markdown('<div class="product-title">ORÁCULO</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:white; font-size:1.1rem; margin-bottom:15px;">25 €</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=200)
    st.markdown('<div class="product-title">RIDER LUXE</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:white; font-size:1.1rem; margin-bottom:15px;">45 €</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", width=200)
    st.markdown('<div class="product-title">AMATISTA</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:white; font-size:1.1rem; margin-bottom:15px;">15 €</div>', unsafe_allow_html=True)
    st.link_button("COMPRAR", "https://wa.me/34684668398")
    st.markdown('</div>
