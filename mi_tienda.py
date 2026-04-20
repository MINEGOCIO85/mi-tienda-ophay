import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", layout="wide")

# ESTILO CORREGIDO: TEXTO DE BOTÓN EN NEGRO PARA MÁXIMA VISIBILIDAD
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    
    /* Títulos y Precios en Oro */
    h1, h3, .precio-oro { 
        color: #d4af37 !important; 
        text-align: center; 
        font-family: 'serif'; 
        font-weight: bold;
    }
    
    /* Texto de descripción en Blanco */
    .descripcion-texto {
        color: #ffffff !important;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 15px;
    }

    /* BOTÓN: Fondo dorado, Letras NEGRAS */
    .stButton>button {
        background-color: #d4af37 !important;
        color: #000000 !important; /* FORZAMOS COLOR NEGRO */
        font-weight: bold !important;
        border-radius: 5px;
        border: none;
        width: 100%;
        height: 50px;
        font-size: 1.1rem !important;
    }
    
    /* Efecto al pasar el ratón */
    .stButton>button:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    p { text-align: center; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# 🌙 OPHAY TAROT")
st.markdown("<p style='color: #d4af37; font-size: 1.2rem;'>Alta Clarividencia & Boutique Esotérica</p>", unsafe_allow_html=True)
st.markdown("---")

# Ruta base de tus fotos
user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

with col1:
    st.image(f"{base_url}/primera%20foto%20isoterica.png")
    st.markdown("### ORÁCULO DEL DESTINO")
    st.markdown("<h2 class='precio-oro'>25 €</h2>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>Lectura profunda para despejar dudas sobre tu futuro.</div>", unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", "https://wa.me/34684668398")

with col2:
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown("### MAZO RIDER LUXE")
    st.markdown("<h2 class='precio-oro'>45 €</h2>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>Mazo de alta calidad con acabados profesionales.</div>", unsafe_allow_html=True)
    st.link_button("LO QUIERO", "https://wa.me/34684668398")

with col3:
    st.image(f"{base_url}/Amatista.png")
    st.markdown("### AMATISTA SAGRADA")
    st.markdown("<h2 class='precio-oro'>15 €</h2>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>Piedra natural cargada para protección energética.</div>", unsafe_allow_html=True)
