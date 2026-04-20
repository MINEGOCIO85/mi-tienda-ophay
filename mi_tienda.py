import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", layout="wide")

# ESTILO DE ALTA GAMA
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    
    h1, h3, .precio-oro { 
        color: #d4af37 !important; 
        text-align: center; 
        font-family: 'serif'; 
        letter-spacing: 2px;
    }
    
    .descripcion-texto {
        color: #e0e0e0 !important;
        text-align: center;
        font-style: italic;
        font-size: 1rem;
        margin-bottom: 25px;
        min-height: 60px;
        line-height: 1.5;
    }

    .stButton>button {
        background: linear-gradient(145deg, #d4af37, #b8962e) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 30px !important;
        border: 1px solid #aa8a24 !important;
        width: 100%;
        height: 50px;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
    }
    
    .stButton>button:hover {
        background: #ffffff !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# 🌙 OPHAY TAROT")
st.markdown("<p style='text-align: center; color: #d4af37; font-size: 1.1rem; letter-spacing: 3px;'>ALTA CLARIVIDENCIA • BOUTIQUE MÍSTICA</p>", unsafe_allow_html=True)
st.markdown("---")

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

with col1:
    st.image(f"{base_url}/primera%20foto%20isoterica.png")
    st.markdown("### ORÁCULO DEL DESTINO")
    st.markdown("<h2 class='precio-oro'>25 €</h2>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Desvela los hilos invisibles de tu camino. Una inmersión profunda en tu energía para hallar respuestas claras y guía espiritual.\"</div>", unsafe_allow_html=True)
    st.link_button("RESERVAR MI SESIÓN", "https://wa.me/34684668398")

with col2:
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown("### MAZO RIDER LUXE")
    st.markdown("<h2 class='precio-oro'>45 €</h2>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Edición de coleccionista. Un mazo sagrado diseñado para conectar con tu intuición a través de un arte sublime y vibración elevada.\"</div>", unsafe_allow_html=True)
    st.link_button("ADQUIRIR TESORO", "https://wa.me/34684668398")

with col3:
    st.image(f"{base_url}/Amatista.png")
    st.markdown("### AMATISTA SAGRADA")
    st.markdown("<h2 class='precio-oro'>15 €</h2>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>\"Gema de transmutación y paz interna. Purificada bajo el influjo lunar para proteger tu hogar y elevar tu frecuencia personal.\"</div>", unsafe_allow_html=True)
    st.link_button("SOLICITAR CRISTAL", "https://wa.me/34684668398")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #555555; font-size: 0.8rem; letter-spacing: 2px;'>OPHAY • MMXXVI | EL DESTINO NO SE ESPERA, SE CONSTRUYE.</p>", unsafe_allow_html=True)
