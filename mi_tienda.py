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
        height: 45px;
    }
    .mystick-icon {
        font-size: 80px;
        color: #d4af37;
        text-align: center;
        display: block;
        margin-bottom: 10px;
    }
    h1, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    p { text-align: center; }
    .footer { text-align: center; color: #555555; margin-top: 50px; font-size: 0.8rem; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.markdown("# 🌙 OPHAY TAROT")
st.markdown("<p>Alta Clarividencia & Boutique Esotérica</p>", unsafe_allow_html=True)
st.markdown("---")

# PRODUCTOS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<span class="mystick-icon">👁️‍🗨️</span>', unsafe_allow_html=True)
    st.markdown("### ORÁCULO DEL DESTINO")
    st.markdown("<p><b>25 €</b></p>", unsafe_allow_html=True)
    st.markdown("<p>Sesión profunda de clarividencia evolutiva.</p>", unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", "https://wa.me/34684668398")

with col2:
    st.markdown('<span class="mystick-icon">🃏</span>', unsafe_allow_html=True)
    st.markdown("### MAZO RIDER LUXE")
    st.markdown("<p><b>45 €</b></p>", unsafe_allow_html=True)
    st.markdown("<p>Edición premium con detalles artísticos.</p>", unsafe_allow_html=True)
    st.link_button("LO QUIERO", "https://wa.me/34684668398")

with col3:
    st.markdown('<span class="mystick-icon">💎</span>', unsafe_allow_html=True)
    st.markdown("### AMATISTA SAGRADA")
    st.markdown("<p><b>15 €</b></p>", unsafe_allow_html=True)
    st.markdown("<p>Cristal purificado para transmutación.</p>", unsafe_allow_html=True)
    st.link_button("COMPRAR", "https://wa.me/34684668398")

st.markdown("---")
st.markdown("<p class='footer'>OPHAY • MMXXVI | El destino no se espera, se construye.</p>", unsafe_allow_html=True)
