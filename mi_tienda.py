import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS COMPACTO
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@400;900&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.plata{font-family:'Montserrat';font-weight:900;font-size:1.2rem;color:#eee;text-transform:uppercase;text-align:center;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:3px solid #d4af37;text-align:center;}
.desc{color:#777;font-family:'Montserrat';font-size:0.8rem;margin:10px 0;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:8px;font-weight:900;text-decoration:none;font-size:0.7rem;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:0.6rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. RUTAS Y COLUMNAS
B="https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W="https://wa.me/34684668398?text="
c1,c2,c3=st.columns(3)

with c1:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">ORACULO</p><p class="desc">Guia espiritual absoluta.</p><p class="oro" style="font-size:1.8rem;">25€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Cita%20Oraculo" class="btn">RESERVAR</a></div>',unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">RIDER LUXE</p><p class="desc">Edicion oro premium.</p><p class="oro" style="font-size:1.8rem;">45€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Mazo%20Rider" class="btn">ADQUIRIR</a></div>',unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">AMATISTA</p><p class="desc">Proteccion energetica.</p><p class="oro" style="font-size:1.8rem;">15€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Amatista" class="btn">CONSULTAR</a></div>',unsafe_allow_html=True)

# 5. DESTINO (FORMATO ULTRA SEGURO)
st.markdown("<br><h2 class='oro' style='font-size:2rem;'>DESTINO</h2>",unsafe_allow_html=True)
txt = """
TIERRA: EXITO ECONOMICO.
FUEGO: ACCION DIRECTA.
AIRE: CLARIDAD MENTAL.
AGUA: INTUICION PURA.
"""
st.markdown('<p class="plata">'+txt+'</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#333;font-size:0.5rem;'>OPHAY BCN</p>",unsafe_allow_html=True)
