import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS LUXURY DIRECTO
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@400;900&display=swap');
.main {background-color:#000;}
[data-testid="stAppViewContainer"] {background-color:#000;}
.oro {font-family:'Cinzel'; background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:900; text-align:center; margin:0;}
.plata {font-family:'Montserrat'; font-weight:900; font-size:1.6rem; background:linear-gradient(to bottom,#fff,#888,#fff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-transform:uppercase; line-height:1.2;}
.card {background:#050505; border:1px solid #1a1a1a; padding:20px; border-top:4px solid #bf953f; text-align:center; min-height:500px;}
.desc {color:#888; font-family:'Montserrat'; font-size:0.8rem; margin:15px 0; font-weight:400;}
.btn {display:inline-block; border:1px solid #bf953f; color:#bf953f!important; padding:10px 20px; font-weight:900; text-decoration:none; border-radius:2px; font-size:0.7rem; letter-spacing:2px;}
.h-d {color:#d4af37; font-size:0.8rem; letter-spacing:5px; font-weight:900; margin-top:20px;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:5rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.7rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA (SIN BUCLES, SIN ERRORES)
b = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">CANALIZACIÓN PRIVADA DE 45 MINUTOS. CLARIDAD ABSOLUTA SOBRE TU DESTINO Y GUÍA ESPIRITUAL.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">25€</p><a href="https://wa.me/34600000000" class="btn">RESERVAR</a></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">MAZO PREMIUM CON BORDES DE ORO. CALIDAD DE COLECCIONISTA Y TEXTURA INIGUALABLE.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">45€</p><a href="https://wa.me/34600000000" class="btn">ADQUIRIR</a></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">GEODA NATURAL SELECCIONADA. PIEZA ÚNICA PARA TRANSMUTACIÓN Y PROTECCIÓN ENERGÉTICA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">15€</p><a href="https://wa.me/34600000000" class="btn">SOLICITAR</a></div>', unsafe_allow_html=True)

# 5. DESTINO
st.markdown("<br><h2 class='oro' style='font-size:3rem;'>✨ DESTINO ✨</h2>", unsafe_allow_html=True)
st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
st.markdown('<p class="h-d">🌱 TIERRA</p><p class="plata">FRUTOS DEL ESFUERZO. PAGO CONFIRMADO.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">🔥 FUEGO</p><p class="plata">MARTE IMPULSA TU NEGOCIO YA.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">💨 AIRE</p><p class="plata">MERCURIO TE DA LA PALABRA CLAVE.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">💧 AGUA</p><p class="plata">SUEÑOS VÍVIDOS. TU VOZ MANDA.</p></div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#444;font-size:0.6rem;'>© OPHAY BOUTIQUE • BCN</p>", unsafe_allow_html=True)
