import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS DE ALTA COSTURA
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@700;900&display=swap');
.main {background-color:#000;}
[data-testid="stAppViewContainer"] {background-color:#000;}
.oro {font-family:'Cinzel'; background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:900; text-align:center;}
.plata {font-family:'Montserrat'; font-weight:900; font-size:1.6rem; background:linear-gradient(to bottom,#fff,#888,#fff,#444); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-transform:uppercase; line-height:1.2;}
.card {background:#050505; border:1px solid #1a1a1a; padding:25px; border-top:5px solid #d4af37; text-align:center; min-height:550px;}
.desc {color:#ccc; font-family:'Montserrat'; font-size:0.85rem; line-height:1.4; margin:15px 0; font-weight:700;}
.btn {display:inline-block; background:linear-gradient(#bf953f,#aa8232); color:#000!important; padding:12px 25px; font-weight:900; text-decoration:none; border-radius:2px; font-size:0.8rem; text-transform:uppercase;}
.h-d {color:#d4af37; font-size:0.9rem; letter-spacing:5px; font-weight:900; margin-top:25px;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:5.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:15px;font-weight:900;font-size:0.8rem;margin-bottom:50px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA CON DESCRIPCIONES POTENTES
b = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
c = st.columns(3)

with c[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.8rem;">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">CANALIZACIÓN PRIVADA DE 45 MINUTOS. ACCEDE A UNA CLARIDAD ABSOLUTA SOBRE TU DESTINO. DESBLOQUEA CAMINOS Y RECIBE LA GUÍA ESPIRITUAL QUE TU ALMA RECOLECTA EN ESTE MOMENTO VITAL.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2.2rem;">25€</p><a href="https://wa.me/34600000000" class="btn">RESERVAR SESIÓN</a></div>', unsafe_allow_html=True)

with c[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.8rem;">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">EL MAZO DEFINITIVO. UNA OBRA MAESTRA DE COLECCIONISTA CON BORDES EN PAN DE ORO Y ACABADO PREMIUM. CADA CARTA ES UNA PUERTA AL SUBCONSCIENTE CON UNA CALIDAD TÁCTIL INIGUALABLE.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2.2rem;">45€</p><a href="https://wa.me/34600000000" class="btn">ADQUIRIR MAZO</a></div>', unsafe_allow_html=True)

with c[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.8rem;">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">GEODA NATURAL SELECCIONADA POR SU VIBRACIÓN. PIEZA ÚNICA DE TRANSMUTACIÓN ENERGÉTICA. ELEVA LA FRECUENCIA DE TU ESPACIO Y FILTRA CUALQUIER NEGATIVIDAD CON EL PODER DEL CUARZO PÚRPURA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2.2rem;">15€</p><a href="https://wa.me/34600000000" class="btn">SOLICITAR PIEZA</a></div>', unsafe_allow_html=True)

# 5. DESTINO
st.markdown("<br><br><h2 class='oro' style='font-size:4rem;'>✨ DESTINO ✨</h2>", unsafe_allow_html=True)
st.markdown('<p class="h-d">🌱 TIERRA</p><p class="plata">RECOGE LOS FRUTOS DEL ESFUERZO.<br>PAGO CONFIRMADO Y ESTABILIDAD.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">🔥 FUEGO</p><p class="plata">LA ENERGÍA DE MARTE TE IMPULSA.<br>ACCIÓN DIRECTA. CIERRA ESE TRATO.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">💨 AIRE</p><p class="plata">MERCURIO ACLARA TUS IDEAS.<br>LA PALABRA ES TU PODER HOY.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">💧 AGUA</p><p class="plata">SUEÑOS VÍVIDOS QUE REVELAN VERDADES.<br>CONFÍA CIEGAMENTE EN TU INTUICIÓN.</p>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center;color:#444;font-weight:900;'>© MMXXVI OPHAY BOUTIQUE • BARCELONA</p>", unsafe_allow_html=True)
