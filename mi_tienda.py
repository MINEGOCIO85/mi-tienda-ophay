import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "PERFECCIÓN"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.03); padding: 15px; border-radius: 15px; min-height: 80px; }

/* BOTONES TIENDA */
div[data-testid="stLinkButton"] > a {
    background-color: #25D366 !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    text-decoration: none !important;
}

/* WHATSAPP - REDONDA COMPLETA */
.wa-wrap {
    position: fixed;
    bottom: 30px;
    right: 20%; /* Margen de seguridad total */
    z-index: 999999;
    display: flex;
    align-items: center;
    gap: 15px;
}
.wa-box {
    background: white; color: black; padding: 8px 15px;
    border-radius: 20px 20px 0 20px; font-weight: 700;
    font-family: 'Montserrat'; font-size: 0.8rem;
}
.wa-btn {
    background-color: #25d366; color: white !important;
    border-radius: 50% !important; width: 60px; height: 60px;
    display: flex; align-items: center; justify-content: center;
    font-size: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    text-decoration: none !important; border: 2px solid #fff2;
}
</style>
<div class="wa-wrap">
    <div class="wa-box">TOP ELEGANTE ✨</div>
    <a href="https://wa.me/34684668398" class="wa-btn" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3rem; margin-top:-40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:5px; font-size:0.7rem; margin-bottom:30px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"
c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2><p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", W)

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
st.markdown('<br><hr style="border-color:#f1c40f33;"><br>', unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

sig = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),
       ("♉ TAURO","Éxito"),("♍ VIRGO","Orden"),("♑ CAPRICORNIO","Rigor"),
       ("♊ GÉMINIS","Mente"),("♎ LIBRA","Paz"),("♒ ACUARIO","Visión"),
       ("♋ CÁNCER","Luna"),("♏ ESCORPIO","Poder"),("♓ PISCIS","Unión")]

hz = st.columns(4)
for i, (n, t) in enumerate(sig):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin:0; font-weight:bold; font-size:0.9rem;">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#888; text-align:center; font-size:0.7rem; margin-bottom:10px;">{t}</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#444; font-size:0.6rem;'>© 2026 OPHAY BARCELONA</p>", unsafe_allow_html=True)
