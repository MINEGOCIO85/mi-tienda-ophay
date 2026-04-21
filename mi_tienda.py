import streamlit as st

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS REFORZADO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');

.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 15px; min-height: 100px; margin-bottom: 15px; }

/* BOTONES VERDES PRODUCTOS */
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

/* WHATSAPP FLOTANTE - POSICIÓN DE SEGURIDAD */
.wa-container {
    position: fixed;
    bottom: 30px;
    right: 10%; /* Usamos % para que nunca choque con el borde derecho */
    z-index: 999999;
    display: flex;
    align-items: center;
    gap: 12px;
}

.wa-bubble {
    background-color: white;
    color: #111;
    padding: 8px 15px;
    border-radius: 20px 20px 0px 20px;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    white-space: nowrap;
}

.wa-icon {
    background-color: #25d366;
    color: white !important;
    border-radius: 50% !important;
    width: 60px;
    height: 60px;
    min-width: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.7);
    text-decoration: none !important;
}
</style>

<div class="wa-container">
    <div class="wa-bubble">¿En qué puedo ayudarte? ✨</div>
    <a href="https://wa.me/34684668398" class="wa-icon" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem; margin-top:-40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:5px; font-size:0.8rem; margin-bottom:40px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

col1, col2, col3 = st.columns(3)

with col1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", W)

with col2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal de alta gama. Edición Oro.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)

with col3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada de alta pureza. Protección.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. HORÓSCOPO (NOMBRES CORREGIDOS)
st.markdown('<br><hr style="border-color:rgba(241,196,15,0.2);"><br>', unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

S = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),
     ("♉ TAURO","Éxito"),("♍ VIRGO","Orden"),("♑ CAPRICORNIO","Rigor"),
     (" Gemini GÉMINIS","Mente"),(" Libra LIBRA","Paz"),(" Aquarius ACUARIO","Visión"),
     (" Cancer CÁNCER","Luna"),(" Scorpio ESCORPIO","Poder"),(" Pisces PISCIS","Unión")]

hz = st.columns(4)
for i, (n, t) in enumerate(S):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin:0; font-weight:bold; font-size:0.95rem;">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#888; text-align:center; font-size:0.75rem; margin-bottom:15px;">{t}</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#444; font-size:0.7rem;'>© 2026 OPHAY BARCELONA</p>", unsafe_allow_html=True)
