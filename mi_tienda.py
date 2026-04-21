import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS DEFINITIVO (PARA CÍRCULO PERFECTO)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');

.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 15px; min-height: 80px; margin-bottom: 15px; }

/* BOTONES VERDES */
div[data-testid="stLinkButton"] > a {
    background-color: #25D366 !important;
    color: white !important;
    border-radius: 10px !important;
    font-family: 'Montserrat' !important;
    font-weight: 700 !important;
    display: flex !important;
    justify-content: center !important;
    text-decoration: none !important;
}

/* WHATSAPP FLOTANTE - MARGEN DE SEGURIDAD TOTAL */
.wa-container {
    position: fixed;
    bottom: 30px;
    right: 15%; /* Lo alejamos bastante del borde para evitar recortes */
    z-index: 999999;
    display: flex;
    align-items: center;
    gap: 15px;
}

.wa-bubble {
    background-color: white;
    color: #111;
    padding: 10px 18px;
    border-radius: 25px 25px 0px 25px;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.5);
    white-space: nowrap;
}

.wa-icon {
    background-color: #25d366;
    color: white !important;
    border-radius: 50% !important;
    width: 65px;
    height: 65px;
    min-width: 65px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 38px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.8);
    text-decoration: none !important;
    border: 2px solid rgba(255,255,255,0.2);
}
</style>

<div class="wa-container">
    <div class="wa-bubble">¿Hablamos? ✨</div>
    <a href="https://wa.me/34684668398" class="wa-icon" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem; margin-top:-40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:5px; font-size:0.8rem; margin-bottom:40px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal de alta gama. Edición Oro.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada de alta pureza. Protección.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. HORÓSCOPO (ESTRUCTURA CORREGIDA)
st.markdown('<br><hr style="border-color:rgba(241,196,15,0.2);"><br>', unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

# Lista blindada para evitar el error de corchetes
signos = [
    ("♈ ARIES", "Fuego"), ("♌ LEO", "Sol"), ("♐ SAGITARIO", "Suerte"),
    ("♉ TAURO", "Éxito"), ("♍ VIRGO", "Orden"), ("♑ CAPRICORNIO", "Rigor"),
    ("♊ GÉMINIS", "Mente"), ("♎ LIBRA", "Paz"), ("♒ ACUARIO", "Visión"),
    ("♋ CÁNCER", "Luna"), ("♏ ESCORPIO", "Poder"), (" Pisces PISCIS", "Unión")
]

hz = st.columns(4)
for idx, (nombre, tema) in enumerate(signos):
    with hz[idx % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin:0; font-weight:bold; font-size:1rem;">{nombre}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#888; text-align:center; font-size:0.75rem; margin-bottom:15px;">{tema}</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#444; font-size:0.7rem;'>© 2026 OPHAY BARCELONA</p>", unsafe_allow_html=True)
