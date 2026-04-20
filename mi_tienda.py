import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique", layout="wide")

# ESTILO GALLERY LUXE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400&display=swap');

    .main { background-color: #050505; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    /* Cabecera Estilo Logo Real */
    .header-container {
        text-align: center;
        padding: 40px 0;
        border-bottom: 1px solid #1a150e;
        margin-bottom: 50px;
    }
    
    .logo-main {
        font-family: 'Cinzel', serif;
        color: #d4af37;
        font-size: 3rem;
        letter-spacing: 12px;
        margin: 0;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.5);
    }

    /* Tarjetas de Producto */
    .product-card {
        background: linear-gradient(145deg, #0a0a0a, #111111);
        border: 1px solid #1c1810;
        padding: 30px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .product-card:hover {
        border-color: #d4af37;
        transform: translateY(-5px);
    }

    .product-title {
        font-family: 'Cinzel', serif;
        color: #d4af37;
        font-size: 1.2rem;
        letter-spacing: 2px;
        margin: 20px 0 10px 0;
    }

    .product-price {
        font-family: 'Montserrat', sans-serif;
        color: #ffffff;
        font-size: 1rem;
        font-weight: 300;
        margin-bottom: 25px;
        opacity: 0.8;
    }

    /* Botón de Acción */
    .stButton>button {
        background-color: #d4af37 !important;
        color: #000000 !important;
        font-family: 'Montserrat', sans-serif;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        border: none !important;
        border-radius: 0px !important;
        width: 100%;
        height: 45px;
        transition: 0.4s;
    }
    
    .stButton>button:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* Ajuste de imagen con marco */
    [data-testid="stImage"] img {
        border: 1px solid #d4af37;
        padding: 5px;
        background-color: #000;
    }
    </style>
    """, unsafe_allow_html=True)

# CABECERA
st.markdown('<div class="header-container"><h1 class="logo-main">OPHAY</h1><p style="color: #665c40; letter-spacing: 5px; font-size: 0.8rem; margin-top: 10px;">TAROT BOUTIQUE • BARCELONA</p></div>', unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=220)
    st.markdown('<div class="product-title">ORÁCULO DEL DESTINO</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">25 €</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR LECTURA", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=220)
    st.markdown('<div class="product-title">MAZO RIDER LUXE</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">45 €</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR PIEZA", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", width=220)
    st.markdown('<div class="product-title">AMATISTA SAGRADA</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">15 €</div>', unsafe_allow_html=True)
    st.link_button("COMPRAR CRISTAL", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br><br><p style='text-align: center; color: #
