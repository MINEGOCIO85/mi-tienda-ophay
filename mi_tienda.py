import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", layout="wide")

# ESTILO MINIMALISTA DE LUJO
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    
    /* Centrar imágenes y darles un toque elegante */
    [data-testid="stImage"] {
        text-align: center;
        display: flex;
        justify-content: center;
    }
    
    h1, h3, .precio-oro { 
        color: #d4af37 !important; 
        text-align: center; 
        font-family: 'serif'; 
        letter-spacing: 2px;
        margin-top: 10px;
    }
    
    .descripcion-texto {
        color: #b0b0b0 !important;
        text-align: center;
        font-style: italic;
        font-size: 0.95rem;
        margin: 10px auto 25px auto;
        max-width: 80%;
        min-height: 70px;
        line-height: 1.4;
    }

    .stButton>button {
        background: linear-gradient(145deg, #d4af37, #b8962e) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 30px !important;
        border: none !important;
        width: 80%; /* Botón algo más corto para que se vea más fino */
        margin: 0 auto;
        display: block;
        height: 45px;
        letter-spacing: 1px;
        font-size: 0.9rem !important;
    }
    
    .stButton>button:hover {
        background: #ffffff !important;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# 🌙 OPHAY TAROT")
st.markdown("<p style='text-align: center; color: #d4af37; font-size: 0.9rem; letter-spacing: 4px; opacity: 0.8;'>ALTA CLARIVIDENCIA</p>", unsafe_allow_html=True)
st.markdown("---")

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

with col1:
    # He reducido el ancho a 220 para que se vea más tipo "boutique"
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=220)
    st.markdown("### ORÁCULO")
    st.markdown("<h3 class='precio-oro'>25 €</h3>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Desvela los hilos invisibles de tu camino. Una inmersión profunda en tu energía.\"</div>", unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", "https://wa.me/34684668398")

with col2:
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=220)
    st.markdown("### MAZO RIDER")
    st.markdown("<h3 class='precio-oro'>45 €</h3>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Edición sagrada para conectar con tu intuición a través de un arte sublime.\"</div>", unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")

with col3:
    st.image(f"{base_url}/Amatista.png", width=220)
    st.markdown("### AMATISTA")
    st.markdown("<h3 class='precio-oro'>15 €</h3>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Gema de transmutación purificada bajo el influjo lunar para proteger tu hogar.\"</div>", unsafe_allow_html=True)
    st.link_button("SOLICITAR", "https://wa.me/34684668398")

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444444; font-size: 0.7rem; letter-
