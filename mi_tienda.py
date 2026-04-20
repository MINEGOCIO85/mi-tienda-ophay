import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS COMPACTO (LÍNEAS CORTAS)
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@100;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.sig{color:#d4af37;font-family:'Cinzel';font-weight:700;margin-top:25px;font-size:1.2rem;text-align:center;letter-spacing:2px;}
.txt{color:#eee;font-family:'Montserrat';font-size:0.9rem;text-align:center;font-weight:100;line-height:1.6;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:2px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:10px;font-weight:900;text-decoration:none;font-size:0.7rem;margin-top:10px;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-size:0.6rem;">PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
B="https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W="https://wa.me/34684668398?text="
c1,c2,c3=st.columns(3)

with c1:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">ORACULO</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Cita" class="btn">RESERVAR</a></div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">RIDER LUXE</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Mazo" class="btn">ADQUIRIR</a></div>',unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">AMATISTA</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Piedra" class="btn">CONSULTAR</a></div>',unsafe_allow_html=True)

# 5. ZODIACO (ESTRUCTURA ANTI-ERROR)
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>ZODIACO</h2>",unsafe_allow_html=True)

# Separamos cada signo en su propia llamada para que no se corte
st.markdown('<p class="sig">ARIES</p><p class="txt">Lidera con fuerza. Marte te apoya.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">TAURO</p><p class="txt">Paciencia y exito financiero hoy.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">GEMINIS</p><p class="txt">Claridad en tus palabras finales.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">CANCER</p><p class="txt">Cambios positivos en tu hogar.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">LEO</p><p class="txt">Brilla con tu propia luz divina.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">VIRGO</p><p class="txt">Orden total para la abundancia.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">LIBRA</p><p class="txt">Equilibrio en tus relaciones hoy.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">ESCORPIO</p><p class="txt">Transformacion y nuevo inicio.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">SAGITARIO</p><p class="txt">Nuevos horizontes de libertad.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">CAPRICORNIO</p><p class="txt">Tus esfuerzos traen recompensas.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">ACUARIO</p><p class="txt">Innovacion en tus proyectos vip.</p>',unsafe_allow_html=True)
st.markdown('<p class="sig">PISCIS</p><p class="txt">Confia en tu intuicion sagrada.</p>',unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#333;font-size:0.5rem;'>OPHAY BCN</p>",unsafe_allow_html=True)
