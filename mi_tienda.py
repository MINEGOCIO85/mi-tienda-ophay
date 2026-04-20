import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS LUXURY
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@400;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.signo{color:#d4af37;font-family:'Cinzel';font-weight:700;margin-top:20px;font-size:1.1rem;text-align:center;}
.prediccion{color:#eee;font-family:'Montserrat';font-size:0.9rem;text-align:center;margin-bottom:10px;line-height:1.4;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:3px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:8px;font-weight:900;text-decoration:none;font-size:0.7rem;margin-top:10px;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:0.6rem;letter-spacing:8px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B="https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W="https://wa.me/34684668398?text="
c1,c2,c3=st.columns(3)

with c1:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">ORACULO</p><p class="oro" style="font-size:1.5rem;">25€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Cita%20Oraculo" class="btn">RESERVAR SESION</a></div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">RIDER LUXE</p><p class="oro" style="font-size:1.5rem;">45€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Mazo%20Rider" class="btn">ADQUIRIR PIEZA</a></div>',unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">AMATISTA</p><p class="oro" style="font-size:1.5rem;">15€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Amatista" class="btn">CONSULTAR</a></div>',unsafe_allow_html=True)

# 5. HOROSCOPO SEMANAL (ESTRUCTURA SEGURA)
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>HOROSCOPO SEMANAL</h2>",unsafe_allow_html=True)

# Bloque 1
st.markdown('<p class="signo">ARIES</p><p class="prediccion">Momento de liderar proyectos estancados. La energia de Marte te favorece.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo">TAURO</p><p class="prediccion">La paciencia sera tu mejor aliada en temas financieros. No te precipites.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo">GEMINIS</p><p class="prediccion">Una conversacion pendiente traera la claridad que tanto necesitabas hoy.</p>',unsafe_allow_html=True)

# Bloque 2
st.markdown('<p class="signo">CANCER</p><p class="prediccion">Escucha tu intuicion en el hogar. Un cambio necesario se aproxima con exito.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo">LEO</p><p class="prediccion">Tu magnetismo esta en el punto mas alto. Es el momento de brillar y proponer.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo">VIRGO</p><p class="prediccion">Ordena tus prioridades. El universo te pide enfoque para recibir abundancia.</p>',unsafe_allow_html=True)

# Bloque 3
st.markdown('<p class="signo">LIBRA</p><p class="prediccion">El equilibrio llega a tus relaciones. Una propuesta inesperada te alegrara.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo">ESCORPIO</p><p class="prediccion">Transformacion profunda. Deja ir lo viejo para que lo nuevo pueda entrar.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo">SAGITARIO</p><p class="prediccion">Nuevos horizontes se abren. Tu optimismo atraera socios muy interesantes.</p>',unsafe_allow_html=True)

# Bloque 4
st.markdown('<p class="signo">CAPRICORNIO</p><p class="prediccion">Tu esfuerzo constante da frutos. Una recompensa economica esta muy cerca.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo">ACUARIO</p><p class="prediccion">Innovacion y libertad. No tengas miedo de ser diferente en tus negocios.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo">PISCIS</p><p class="prediccion">Conecta con tus sueños. El mundo espiritual tiene un mensaje para ti hoy.</p>',unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#444;font-size:0.6rem;'>© OPHAY BOUTIQUE BARCELONA</p>",unsafe_allow_html=True)
