import streamlit as st

# Configuración de la página para aprovechar todo el espacio
st.set_page_config(page_title="Ophay Tarot", layout="wide", initial_sidebar_state="collapsed")

# ESTILO "TODO A LA VISTA" (Compacto y Elegante)
st.markdown("""
    <style>
    /* Eliminar espacios blancos de arriba */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    
    /* Centrar imágenes y reducir su margen inferior */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin-bottom: -10px;
    }
    
    h1 { color: #d4af37 !important; text-align: center; font-size: 1.8rem !important; margin-bottom: 0px; }
    h3 { color: #d4af37 !important; text-align: center; font-size: 1.1rem !important; margin-top: 5px; }
    .precio-oro { color: #d4af37 !important; text-align: center; font-weight: bold; font-size: 1.2rem; margin-top: -10px; }
    
    .descripcion-texto {
        color: #b0b0b0 !important;
        text-align: center;
        font-style: italic;
        font-size: 0.85rem;
        margin: 5px auto 10px auto;
        line-height: 1.2;
    }

    /* BOTONES MÁS COMPACTOS */
    .stButton>button {
        background: linear-gradient(145deg, #d4af37, #b8962e) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 20px !important;
        border: none !important;
        width: 90%;
        height: 35px;
        font-size: 0.8rem !important;
        margin: 0 auto;
        display: block;
    }
    
    hr { margin: 0.5rem 0; }
    </style>
    """, unsafe_allow_html=True)

# Título muy compacto
st.markdown("<h1>🌙 OPHAY TAROT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #d4af37; font-size: 0.7rem; letter-spacing: 2px;'>ALTA CLARIVIDENCIA</p>", unsafe_allow_html=True)
st.markdown("---")

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# Usamos columnas que en móvil se apilan pero ocupan poco espacio
col1, col2, col3 = st.columns(3)

with col1:
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=140)
    st.markdown("### ORÁCULO")
    st.markdown("<p class='precio-oro'>25 €</p>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Inmersión profunda en tu energía personal.\"</div>", unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")

with col2:
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=140)
    st.markdown("### MAZO RIDER")
    st.markdown("<p class='precio-oro'>45 €</p>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Arte sagrado para conectar con tu intuición.\"</div>", unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")

with col3:
    st.image(f"{base_url}/Amatista.png", width=140)
    st.markdown("### AMATISTA")
    st.markdown("<p class='precio-oro'>15 €</p>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Gema lunar para protección y paz espiritual.\"</div>", unsafe_allow_html=True)
    st.link_button("SOLICITAR", "https://wa.me/34684668398")

st.markdown("<p style='text-align: center; color: #444444; font-size: 0.6rem; margin-top: 20px;'>OPHAY • BARCELONA</p>", unsafe_allow_html=True)
