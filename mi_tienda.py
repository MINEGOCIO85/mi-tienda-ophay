import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY", layout="wide")

# 2. ESTILO BOUTIQUE
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@900&display=swap');
.main {background-color:#000;}
[data-testid="stAppViewContainer"] {background-color:#000;}
.oro {font-family:'Cinzel'; background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:900; text-align:center;}
.plata {font-family:'Montserrat'; font-weight:900; font-size:1.5rem; background:linear-gradient(to bottom,#fff,#888,#fff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-transform:uppercase;}
.card {background:#050505; border:1px solid #1a1a1a; padding:15px; border-top:4px solid #d4af37; text-align:center; margin-bottom:10px;}
.btn {display:inline-block; background:#d4af37; color:#000!important; padding:8px 15px; font-weight:900; text-decoration:none; border-radius:4px; font-size:0.8rem;}
.h-d {color:#d4af37; font-size:0.8rem; letter-spacing:4px; font-weight:900; margin-top:10px;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.7rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
b = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
c = st.columns(3)

with c[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.2rem;">ORÁCULO</p><p style="color:#fff;font-size:0.8rem;">45 MIN CLARIDAD</p><a href="https://wa.me/34600000000" class="btn">RESERVAR</a></div>', unsafe_allow_html=True)

with c[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.2rem;">TAROT</p><p style="color:#fff;font-size:0.8rem;">EDICIÓN ORO</p><a href="https://wa.me/34600000000" class="btn">COMPRAR</a></div>', unsafe_allow_html=True)

with c[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(b+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.2rem;">AMATISTA</p><p style="color:#fff;font-size:0.8rem;">PROTECCIÓN</p><a href="https://wa.me/34600000000" class="btn">COMPRAR</a></div>', unsafe_allow_html=True)

# 5. DESTINO (VERSION ULTRA ESTABLE)
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>✨ DESTINO ✨</h2>", unsafe_allow_html=True)

st.markdown('<p class="h-d">🌱 TIERRA</p><p class="plata">PAGO CONFIRMADO. ÉXITO.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">🔥 FUEGO</p><p class="plata">MARTE IMPULSA TU NEGOCIO.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">💨 AIRE</p><p class="plata">MERCURIO TE DA LA PALABRA.</p>', unsafe_allow_html=True)
st.markdown('<p class="h-d">💧 AGUA</p><p class="plata">SUEÑOS VÍVIDOS. VOZ INTERIOR.</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#444;font-size:0.6rem;'>© OPHAY BOUTIQUE</p>", unsafe_allow_html=True)
