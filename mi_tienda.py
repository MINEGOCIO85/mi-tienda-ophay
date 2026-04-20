import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILOS (Líneas cortas para evitar cortes)
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@400;900&display=swap');
.main {background-color:#000;}
[data-testid="stAppViewContainer"] {background-color:#000;}
.oro {font-family:'Cinzel'; background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:900; text-align:center;}
.plata {font-family:'Montserrat'; font-weight:900; font-size:1.5rem; background:linear-gradient(to bottom,#fff,#888,#fff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-transform:uppercase; text-align:center;}
.card {background:#050505; border:1px solid #1a1a1a; padding:20px; border-top:4px solid #d4af37; text-align:center; min-height:480px;}
.desc {color:#888; font-family:'Montserrat'; font-size:0.8rem; margin:15px 0;}
.btn {display:block; border:1px solid #bf953f; color:#bf953f!important; padding:10px; font-weight:900; text-decoration:none; border-radius:2px; font-size:0.7rem; letter-spacing:2px;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.7rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. VARIABLES DE RUTA Y WHATSAPP
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

# 5. TIENDA
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">CANALIZACIÓN PRIVADA DE 45 MINUTOS. CLARIDAD Y GUÍA ESPIRITUAL.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">25€</p>', unsafe_allow_html=True)
    t1 = "Saludos%20OPHAY.%20Deseo%20consultar%20disponibilidad%20para%20una%20sesion%20de%20Oraculo."
    st.markdown('<a href="'+W+t1+'" class="btn">SOLICITAR CITA</a></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">MAZO DE COLECCIONISTA CON CANTOS EN ORO. CALIDAD PREMIUM.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">45€</p>', unsafe_allow_html=True)
    t2 = "Hola%20OPHAY.%20Me%20gustaria%20saber%20los%20pasos%20para%20adquirir%20el%20mazo%20Rider%20Luxe."
    st.markdown('<a href="'+W+t2+'" class="btn">ADQUIRIR PIEZA</a></div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">GEODA NATURAL DE ALTA VIBRACIÓN. PROTECCIÓN DEL HOGAR.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">15€</p>', unsafe_allow_html=True)
    t3 = "Saludos.%20Estoy%20interesado%20en%20adquirir%20la%20Amatista.%20¿Sigue%20disponible?"
    st.markdown('<a href="'+W+t3+'" class="btn">CONSULTAR PIEZA</a></div>', unsafe_allow_html=True)

# 6. DESTINO
st.markdown("<br><h2 class='oro' style='font-size:3rem;'>✨ DESTINO ✨</h2>", unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;margin-top:15px;">🌱 TIERRA</p><p class="plata">PAGO CONFIRMADO. ÉXITO.</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;margin-top:15px;">🔥 FUEGO</p><p class="plata">MARTE IMPULSA TU ACCIÓN.</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;margin-top:15px;">💨 AIRE</p><p class="plata">LA PALABRA ES TU PODER.</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;margin-top:15px;">💧 AGUA</p><p class="plata">INTUICIÓN Y SUEÑOS VÍVIDOS.</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#444;font-size:0.6rem;'>© MMXXVI OPHAY BOUTIQUE • BCN</p>", unsafe_allow_html=True)
