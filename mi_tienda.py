import streamlit as st

# 1. SETUP & CSS DE ALTA COSTURA
st.set_page_config(page_title="OPHAY ELITE | BCN", layout="wide")
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@100;700;900&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
/* Estilo Oro para el Signo */
.signo-oro{
    color:#d4af37; font-family:'Cinzel'; font-weight:700; margin-top:30px; 
    font-size:1.3rem; text-align:center; letter-spacing:3px;
    background: linear-gradient(180deg, #bf953f 0%, #fcf6ba 50%, #aa8232 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
/* Estilo Ultra-Ligero para la Predicción */
.prediccion-luxe{
    color:#eee; font-family:'Montserrat'; font-size:0.95rem; text-align:center; 
    margin-bottom:15px; line-height:1.8; font-weight:100; letter-spacing:1px;
}
.card{background:#050505;border:1px solid #111;padding:20px;border-top:3px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:10px;font-weight:900;text-decoration:none;font-size:0.75rem;margin-top:15px;letter-spacing:2px;}
</style>""", unsafe_allow_html=True)

# 2. CABECERA
st.markdown('<h1 class="oro" style="font-size:4.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:0.7rem;letter-spacing:12px;margin-bottom:50px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 3. PRODUCTOS
B="https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W="https://wa.me/34684668398?text="
c1,c2,c3=st.columns(3)

with c1:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.6rem;">ORÁCULO</p><p class="oro" style="font-size:1.8rem;">25€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Cita%20Oraculo" class="btn">RESERVAR SESIÓN</a></div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.6rem;">RIDER LUXE</p><p class="oro" style="font-size:1.8rem;">45€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Mazo%20Rider" class="btn">ADQUIRIR PIEZA</a></div>',unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.6rem;">AMATISTA</p><p class="oro" style="font-size:1.8rem;">15€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Amatista" class="btn">CONSULTAR</a></div>',unsafe_allow_html=True)

# 4. HORÓSCOPO SEMANAL Lujo Top (ESTRUCTURA SEGURA)
st.markdown("<br><br><h2 class='oro' style='font-size:3rem;'>✨ HORÓSCOPO ✨</h2>",unsafe_allow_html=True)
st.markdown("<p style='color:#d4af37;text-align:center;letter-spacing:5px;margin-bottom:30px;'>COMENTARIO SEMANAL</p>",unsafe_allow_html=True)

# Bloque 1
st.markdown('<p class="signo-oro">♈ ARIES</p><p class="prediccion-luxe">El Carnero Sagrado te impulsa a liderar proyectos estancados. La energia de Marte te favorece.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo-oro">♉ TAURO</p><p class="prediccion-luxe">La paciencia del Toro sera tu mejor aliada en temas financieros. No te precipites en tus decisiones.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo-oro">♊ GÉMINIS</p><p class="prediccion-luxe">Los Gemelos Sagrados traen claridad a una conversacion pendiente. Tu palabra tiene poder hoy.</p>',unsafe_allow_html=True)

# Bloque 2
st.markdown('<p class="signo-oro">♋ CÁNCER</p><p class="prediccion-luxe">La Luna te guia en el hogar. Un cambio necesario en tu espacio se aproxima con exito.</p>',unsafe_allow_html=True)
st.markdown('<p class="signo-oro">♌ LEO</
