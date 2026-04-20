import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS LUXURY TOP
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@400;900&display=swap');
.main {background-color:#000;}
[data-testid="stAppViewContainer"] {background-color:#000;}
.oro {font-family:'Cinzel'; background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:900; text-align:center;}
.plata {font-family:'Montserrat'; font-weight:900; font-size:1.6rem; background:linear-gradient(to bottom,#fff,#888,#fff,#444); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-transform:uppercase; line-height:1.2;}
.card {background:#050505; border:1px solid #1a1a1a; padding:25px; border-top:5px solid #d4af37; text-align:center; min-height:500px;}
.desc {color:#888; font-family:'Montserrat'; font-size:0.8rem; line-height:1.4; margin:15px 0;}
.btn {display:block; border:1px solid #bf953f; color:#bf953f!important; padding:12px; font-weight:900; text-decoration:none; border-radius:2px; font-size:0.7rem; letter-spacing:2px; transition: 0.3s;}
.btn:hover {background:#bf953f; color:#000!important;}
.h-d {color:#d4af37; font-size:0.8rem; letter-spacing:5px; font-weight:900; margin-top:20px; text-align:center;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:15px;font-weight:900;font-size:0.8rem;margin-bottom:50px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA CON WHATSAPP CORRECTO (34684668398)
b = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
wa = "https://wa.me/34684668398?text="
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.8rem;">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">CANALIZACIÓN PRIVADA DE 45 MINUTOS. CLARIDAD TOTAL SOBRE TU DESTINO Y GUÍA ESPIRITUAL.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2.2rem;">25€</p>', unsafe_allow_html=True)
    st.markdown('<a href="'+wa+'Hola%20OPHAY,%20quiero%20reservar%20el%20Oraculo" class="btn">SOLICITAR ACCESO</a></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.8rem;">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">MAZO DE COLECCIONISTA CON CANTOS EN ORO. UNA HERRAMIENTA SAGRADA DE ALTA GAMA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2.2rem;">45€</p>', unsafe_allow_html=True)
    st.markdown('<a href="'+wa+'Hola%20OPHAY,%20quiero%20el%20Tarot%20Rider%20Luxe" class="btn">ADQUIRIR PIEZA</a></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.8rem;">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">GEODA NATURAL DE ALTA VIBRACIÓN. TRANSMUTACIÓN ENERGÉTICA Y PROTECCIÓN DEL HOGAR.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2.2rem;">15€</p>', unsafe_allow_html=True)
    st.markdown('<a href="'+wa+'Hola%20OPHAY,%20me%20interesa%20la%20Amatista" class="btn">SOLICITAR PIEZA</a></div>', unsafe_allow_html=True)

# 5. DESTINO
st.markdown("<br><br><h2 class='oro' style='font-size:3.5rem;'>✨ DESTINO ✨</h2>", unsafe_allow_html=True)
st.markdown('<p class="h-d">🌱 TIERRA</p><p class="plata" style="text-align:center;">ÉXITO ECONÓMICO. PAGO CONFIRMADO.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">🔥 FUEGO</p><p class="plata" style="text-align:center;">MARTE TE IMPULSA. ACCIÓN DIRECTA.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">💨 AIRE</p><p class="plata" style="text-align:center;">MERCURIO ACLARA TUS IDEAS HOY.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">💧 AGUA</p><p class="plata" style="text-align:center;">SUEÑOS VÍVIDOS. TU VOZ MANDA.</p>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center;color:#444;font-weight:900;'>© MMXXVI OPHAY BOUTIQUE • BCN</p>", unsafe_allow_html=True)
