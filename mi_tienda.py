import streamlit as st

# Configuración
st.set_page_config(page_title="Ophay Tarot", layout="wide")

# Estilo Negro y Dorado (Lujo)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    h1, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    p { text-align: center; }
    .stButton>button {
        background-color: #d4af37;
        color: black;
        width: 100%;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# 🌙 OPHAY TAROT")
st.markdown("<p>Alta Clarividencia & Boutique Esotérica</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns(3)

# PRODUCTO 1
with col1:
    # Si la foto se llama distinto, cámbialo entre las comillas
    st.image("primera foto isoterica.png", caption="ORÁCULO DEL DESTINO")
    st.markdown("### 25 €")
    st.link_button("RESERVAR SESIÓN", "https://wa.me/34684668398")

# PRODUCTO 2
with col2:
    st.image("FOTOMAZO.png", caption="MAZO RIDER LUXE")
    st.markdown("### 45 €")
    st.link_button("LO QUIERO", "https://wa.me/34684668398")

# PRODUCTO 3
with col3:
    st.image("fotoamatista.png", caption="AMATISTA SAGRADA")
    st.markdown("### 15 €")
    st.link_button("COMPRAR", "https://wa.me/34684668398")

st.markdown("---")
st.markdown("<p style='color: #555;'>OPHAY • MMXXVI</p>", unsafe_allow_html=True)
