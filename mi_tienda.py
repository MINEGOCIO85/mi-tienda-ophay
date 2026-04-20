import streamlit as st

# 1. CONFIGURACION
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO LUXURY
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@100;400;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.sig{color:#d4af37;font-family:'Cinzel';font-weight:700;margin-top:20px;font-size:1.1rem;text-align:center;}
.txt{color:#ccc;font-family:'Montserrat';font-size:0.75rem;text-align:center;font-weight:400;line-height:1.5;margin-bottom:25px;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:2px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:8px;font-weight:900;text-decoration:none;font-size:0.7rem;margin-top:10px;}
.box{border:1px double #d4af37;padding:25px;margin-top:40px;text-align:center;background:#050505;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-size:0.6rem;letter-spacing:8px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
B="https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W="https://wa.me/34684668398?text="
c1,c2,c3=st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">ORÁCULO</p><a href="'+W+'Cita" class="btn">RESERVAR</a></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">RIDER LUXE</p><a href="'+W+'Mazo" class="btn">ADQUIRIR</a></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">AMATISTA</p><a href="'+W+'Piedra" class="btn">CONSULTAR</a></div>', unsafe_allow_html=True)

# 5. HOROSCOPO
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>HORÓSCOPO</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<p class="sig">♈ ARIES</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Fuego transformador. Tu audacia abrira puertas hoy.</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<p class="sig">♉ TAURO</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Persistencia dorada. La estabilidad llega con enfoque.</p>', unsafe_allow_html=True)
with col3:
    st.markdown('<p class="sig">♊ GÉMINIS</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Dualidad magica. Tu palabra es el puente al exito.</p>', unsafe
