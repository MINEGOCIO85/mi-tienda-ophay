import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO LUXURY
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@100;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.sig{color:#d4af37;font-family:'Cinzel';font-weight:700;margin-top:15px;font-size:1.1rem;text-align:center;}
.txt{color:#ccc;font-family:'Montserrat';font-size:0.8rem;text-align:center;font-weight:100;margin-bottom:20px;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:2px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:8px;font-weight:900;text-decoration:none;font-size:0.7rem;margin-top:10px;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-size:0.6rem;letter-spacing:8px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B="https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W="https://wa.me/34684668398?text="
c1,c2,c3=st.columns(3)

with c1:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">ORACULO</p><a href="'+W+'Cita" class="btn">RESERVAR</a></div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">RIDER LUXE</p><a href="'+W+'Mazo" class="btn">ADQUIRIR</a></div>',unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">AMATISTA</p><a href="'+W+'Piedra" class="btn">CONSULTAR</a></div>',unsafe_allow_html=True)

# 5. HORÓSCOPO CON LOGOS MÍSTICOS
st.markdown("<br><h2 class='oro' style='font-size:2.2rem;'>HOROSCOPO</h2>",unsafe_allow_html=True)

# Fila 1
f1, f2, f3, f4 = st.columns(4)
f1.markdown('<p class="sig">♈ ARIES</p><p class="txt">Lidera con fuerza.</p>', unsafe_allow_html=True)
f2.markdown('<p class="sig">♉ TAURO</p><p class="txt">Exito financiero.</p>', unsafe_allow_html=True)
f3.markdown('<p class="sig">♊ GEMINIS</p><p class="txt">Claridad mental.</p>', unsafe_allow_html=True)
f4.markdown('<p class="sig">♋ CANCER</p><p class="txt">Paz en tu hogar.</p>', unsafe_allow_html=True)

# Fila 2
f5, f6, f7, f8 = st.columns(4)
f5.markdown('<p class="sig">♌ LEO</p><p class="txt">Brilla con tu luz.</p>', unsafe_allow_html=True)
f6.markdown('<p class="sig">♍ VIRGO</p><p class="txt">Orden y abundancia.</p>', unsafe_allow_html=True)
f7.markdown('<p class="sig">♎ LIBRA</p><p
