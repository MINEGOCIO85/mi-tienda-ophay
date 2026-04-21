import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "LUXURY, LEGAL & BOTONES VISIBLES"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }

/* Tipografías */
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 15px; min-height: 80px; }

/* REPARACIÓN DE BOTONES DE SERVICIO */
div[data-testid="stLinkButton"] > a {
    background-color: #25D366 !important; /* Verde WhatsApp */
    color: white !important; /* Texto Blanco siempre visible */
    border-radius: 10px !important;
    font-family: 'Montserrat' !important;
    font-weight: 700 !important;
    display: flex !important;
    justify-content: center !important;
    text-decoration: none !important;
    border: 1px solid #ffffff33 !important;
}

/* WHATSAPP FLOTANTE - REDONDA PERFECTA */
.wa-wrap {
    position: fixed;
    bottom: 40px;
    right: 22%; 
    z-index: 999999;
    display: flex;
    align-items: center;
    gap: 15px;
}
.wa-bubble {
    background: #fff; color: #000; padding: 10px 20px;
    border-radius: 30px 30px 5px 30px; font-weight: 600;
    font-family: 'Montserrat'; font-size: 0.85rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    border: 1px solid #f1c40f;
}
.wa-btn {
    background-color: #25d366; color: white !important;
    border-radius: 50% !important; width: 65px; height: 65px;
    display: flex; align-items: center; justify-content: center;
    font-size: 35px; box-shadow: 0 8px 20px rgba(0,0,0,0.6);
    text-decoration: none !important;
}

/* TEXTO LEGAL */
.legal-text {
    color: #888; font-family: 'Montserrat'; font-size: 0.75rem;
    text-align: justify; line-height: 1.4; background: #111;
    padding: 20px; border-radius: 10px;
}
</style>

<div class="wa-wrap">
    <div class="wa-bubble">Atención Personalizada Boutique ✨</div>
    <a href="https://wa.me/34684668398" class="wa-btn" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem; margin-top:-40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:7px; font-size:0.8rem; margin-bottom:40px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"
c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2><p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR CITA", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2><p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal de alta gama. Edición Oro.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2><p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada de alta pureza. Protección.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. HORÓSCOPO
st.markdown('<br><hr style="border-color:#f1c40f44;"><br>', unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2rem; margin-bottom:30px;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

signos = [
    ("♈ ARIES", "Fuego"), ("♌ LEO", "Sol"), ("♐ SAGITARIO", "Suerte"),
    ("♉ TAURO", "Éxito"), ("♍ VIRGO", "Orden"), ("♑ CAPRICORNIO", "Rigor"),
    ("♊ GÉMINIS", "Mente"), ("♎ LIBRA", "Paz"), ("♒ ACUARIO", "Visión"),
    ("♋ CÁNCER", "Luna"), ("♏ ESCORPIO", "Poder"), ("♓ PISCIS", "Unión")
]

hz = st.columns(4)
for i, (n, t) in enumerate(signos):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin:0; font-weight:bold;">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#888; text-align:center; font-size:0.75rem; margin-bottom:20px;">{t}</p>', unsafe_allow_html=True)

# 6. SECCIÓN LEGAL
st.markdown('<br><br>', unsafe_allow_html=True)
with st.expander("⚖️ INFORMACIÓN LEGAL Y PRIVACIDAD"):
    t1, t2, t3 = st.tabs(["Aviso Legal", "Privacidad", "Cookies"])
    with t1:
        st.markdown('<div class="legal-text"><b>Responsable:</b> OPHAY BARCELONA.<br>Los servicios son para mayores de 18 años. Guía espiritual y entretenimiento.</div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="legal-text">Sus datos solo se usan para gestionar su cita vía WhatsApp de forma privada.</div>', unsafe_allow_html=True)
    with t3:
        st.markdown('<div class="legal-text">Usamos cookies técnicas para la estabilidad de la web y el botón de contacto.</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#444; font-size:0.7rem; margin-top:50px;'>© MMXXVI OPHAY BARCELONA • LUXURY SPIRITUALITY</p>", unsafe_allow_html=True)
