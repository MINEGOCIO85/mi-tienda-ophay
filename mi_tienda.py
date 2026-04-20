import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS COMPACTO
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@100;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.sig{color:#d4af37;font-family:'Cinzel';font-weight:700;margin-top:15px;font-size:1rem;text-align:center;letter-spacing:2px;}
.txt{color:#ccc;font-family:'Montserrat';font-size:0.8rem;text-align:center;font-weight:100;line-height:1.4;margin-bottom:20px;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:2px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:8px;font-weight:900;text-decoration:none;font-size:0.7rem;margin-top:10px;}
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
    st.markdown('<p class="oro" style="font-size:1.4rem;">ORACULO</p><a href="'+W+'Cita" class="btn">RESERVAR</a></div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">RIDER LUXE</p><a href="'+W+'Mazo" class="btn">ADQUIRIR</a></div>',unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">AMATISTA</p><a href="'+W+'Piedra" class="btn">CONSULTAR</a></div>',unsafe_allow_html=True)

# 5. ZODIACO EN FILAS DE 4 (DISEÑO TOP)
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>HOROSCOPO</h2>",unsafe_allow_html=True)

# Fila 1
f1a, f1b, f1c, f1d = st.columns(4)
with f1a: st.markdown('<p class="sig">ARIES</p><p class="txt">Lidera con fuerza.<br>Marte te apoya.</p>',u=1)
with f1b: st.markdown('<p class="sig">TAURO</p><p class="txt">Paciencia y exito<br>financiero hoy.</p>',u=1)
with f1c: st.markdown('<p class="sig">GEMINIS</p><p class="txt">Claridad en tus<br>palabras finales.</p>',u=1)
with f1d: st.markdown('<p class="sig">CANCER</p><p class="txt">Cambios positivos<br>en tu hogar.</p>',u=1)

# Fila 2
f2a, f2b, f2c, f2d = st.columns(4)
with f2a: st.markdown('<p class="sig">LEO</p><p class="txt">Brilla con tu<br>propia luz divina.</p>',u=1)
with f2b: st.markdown('<p class="sig">VIRGO</p><p class="txt">Orden total para<br>la abundancia.</p>',u=1)
with f2c: st.markdown('<p class="sig">LIBRA</p><p class="txt">Equilibrio en tus<br>relaciones hoy.</p>',u=1)
with f2d: st.markdown('<p class="sig">ESCORPIO</p><p class="txt">Transformacion y<br>nuevo inicio.</p>',u=1)

# Fila 3
f3a, f3b, f3c, f3d = st.columns(4)
with f3a: st.markdown('<p class="sig">SAGITARIO</p><p class="txt">Nuevos horizontes<br>de libertad.</p>',u=1)
with f3b: st.markdown('<p class="sig">CAPRICORNIO</p><p class="txt">Tus esfuerzos traen<br>recompensas.</p>',u=1)
with f3c: st.markdown('<p class="sig">ACUARIO</p><p class="txt">Innovacion en tus<br>proyectos vip.</p>',u=1)
with f3d: st.markdown('<p class="sig">PISCIS</p><p class="txt">Confia en tu<br>intuicion sagrada.</p>',u=1)

st.markdown("<br><p style='text-align:center;color:#333;font-size:0.5rem;'>OPHAY BCN</p>",unsafe_allow_html=True)
