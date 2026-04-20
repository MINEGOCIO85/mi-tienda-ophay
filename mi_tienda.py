import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique", layout="wide")

# ESTILO GALLERY LUXE (SIN ERRORES)
st.markdown("""
    <style>
    .main { background-color: #050505; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    /* Cabecera */
    .header-container {
        text-align: center;
        padding: 30px 0;
        border-bottom: 1px solid #1a150e;
        margin-bottom: 40px;
    }
    
    .logo-main {
        color: #d4af37;
        font-size: 2.8rem;
        letter-spacing: 10px;
        font-family: 'serif';
        margin: 0;
    }

    /* Tarjetas de Producto */
    .product-card {
        background: #0a0a0a;
        border: 1px solid #1c1810;
        padding: 25px;
        text-align: center;
        border-radius: 2px;
    }

    .product-title {
        color: #d4af37;
        font-size: 1.1rem;
        letter-spacing: 2px;
        margin: 15px 0 5px 0;
        font-family: 'serif';
    }

    .product-price {
        color: #ffffff;
        font-size: 1rem;
        margin-bottom: 20px;
        opacity: 0.8;
    }

    /* Botón Dorado */
    .stButton>button {
        background-color: #d4af37 !important;
        color: #000000 !important;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        border: none !important;
        border-radius: 0px !important;
        width: 100%;
        height: 45px;
    }
    
    .stButton>button:hover {
        background-color: #ffffff !important;
    }

    /* Marco para imágenes */
    [data-testid="stImage"] img {
        border: 1px solid #d4af37;
        padding: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# CABECERA
st.markdown('<div class="header-container"><h1 class="logo-main">OPHAY</h1><p style="color: #665c40; letter-spacing: 4px; font-size: 0.7rem;">TAROT BOUTIQUE • BARCELONA</p></div>', unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=210)
    st.markdown('<div class="product-title">ORÁCULO DEL DESTINO</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">25 €</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=210)
    st.markdown('<div class="product-title">MAZO RIDER LUXE</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">45 €</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", width=210)
    st.markdown('<div class="product-title">AMATISTA SAGRADA</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">15 €</div>', unsafe_allow_html=True)
    st.link_button("COMPRAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

# PIE DE PÁGINA (CORREGIDO)
st.markdown("<br><br><p style='text-align: center; color: #333; font-size: 0.6rem; letter-spacing: 3px;'>© MMXXVI OPHAY COLLECTION</p>", unsafe_allow_html=True)
