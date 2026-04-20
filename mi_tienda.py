import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", layout="wide")

# ESTILO NEGRO Y DORADO PROFESIONAL
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    .stButton>button {
        background-color: #d4af37;
        color: #000000;
        font-weight: bold;
        border-radius: 5px;
        border: none;
        width: 100%;
    }
    h1, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    p { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# 🌙 OPHAY TAROT")
st.markdown("<p>Alta Clarividencia & Boutique Esotérica</p>", unsafe_allow_html=True)
st.markdown("---")

# Ruta base de tus fotos en GitHub
user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

with col1:
    # Foto: primera foto isoterica.png
    st.image(f"{base_url}/primera%20foto%20isoterica.png")
    st.markdown("### ORÁCULO DEL DESTINO")
    st.markdown("<p><b>25 €</b></p>", unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", "https://wa.me/34684668398")

with col2:
    # Foto: SEGUNDA FOTO ESOTERICA.png
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown("### MAZO RIDER LUXE")
    st.markdown("<p><b>45 €</b></p>", unsafe_allow_html=True)
    st.link_button("LO QUIERO", "https://wa.me/34684668398")

with col3:
    # Foto: Amatista.png
    st.image(f"{base_url}/Amatista.png")
    st.markdown("### AMATISTA SAGRADA")
    st.markdown("<p><b>15 €</b></p>", unsafe_allow_html=True)
    st.link_button("COMPRAR", "https://wa.me/34684668398")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #555555;'>OPHAY • MMXXVI</p>", unsafe_allow_html=True)
