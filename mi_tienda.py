import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "BOUTIQUE LUXURY"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }

/* Tipografías */
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 15px; min-height: 80px; }

/* BOTONES DE COMPRA */
div[data-testid="stLinkButton"] > a {
    background-color: #1e7e34 !important; /* Un verde más elegante, tipo bosque/lujo */
    color: white !important;
    border: 1px solid #f1c40f !important;
    border-radius: 5px !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    transition: 0.4s;
}

/* WHATSAPP FLOTANTE - POSICIÓN MAESTRA */
.wa-wrap {
    position: fixed;
    bottom: 40px;
    right: 20%; /* Aquí está el truco para que NO se corte nunca */
    z-index: 999999;
    display: flex;
    align-items: center;
    gap: 15px;
}
.wa-bubble {
    background: linear-gradient(135deg, #ffffff 0%, #f1f1f1 100%);
    color: #000;
    padding: 10px 20px;
    border-radius: 30px 30px 5px 30px;
    font-weight: 600;
    font-family: 'Montserrat';
    font-size: 0.85rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    border: 1px solid #f1c40f;
}
.wa-btn {
    background-color: #25d366;
    color: white !important;
    border-radius: 50% !important;
    width: 65px;
    height: 65px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.6);
    text-decoration: none !important;
    border: 2px solid #ffffff33;
}
</style>

<div class="wa-wrap">
    <div class="wa-bubble">Asesoramiento Private Boutique ✨</div>
    <a href="https://wa.me/34684668398" class="wa-btn" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem; margin-top:-40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:7px; font-size:0.8rem; margin-bottom:40px; opacity:0.8;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"
c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2><p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia. Sesión exclusiva.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR CITA", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2><p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal de alta gama. Edición limitada Oro.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2><p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada de alta pureza. Protección espiritual.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. HORÓSCOPO ELITE
st.markdown('<br><hr style="border-color:#f1c40f44;"><br>', unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2.2rem; margin-bottom:30px;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

sig = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),
       ("♉ TAURO","Éxito"),("♍ VIRGO","Orden"),("♑ CAPRICORNIO","Rigor"),
       (" Gemini GÉMINIS","Mente"),(" Libra LIBRA","Paz"),(" Aquarius ACUARIO","Visión"),
       (" Cancer CÁNCER","Luna"),(" Scorpio ESCORPIO","Poder"),(" Pisces PISCIS","Unión")]

hz = st.columns(4)
for i, (n, t) in enumerate(sig):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin:0; font-weight:bold; font-size:1rem;">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#888; text-align:center; font-size:0.75rem; margin-bottom:20px;">{t}</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#555; font-size:0.7rem; letter-spacing:2px;'>© MMXXVI OPHAY BARCELONA</p>", unsafe_allow_html=True)
