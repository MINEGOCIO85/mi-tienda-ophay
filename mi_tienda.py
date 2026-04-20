import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS (ESTILO FRAGMENTADO PARA EVITAR CORTES)
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@400;900&display=swap');
.main {background-color:#000;}
[data-testid="stAppViewContainer"] {background-color:#000;}
.oro {
    font-family:'Cinzel'; 
    background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232); 
    -webkit-background-clip:text; 
    -webkit-text-fill-color:transparent; 
    font-weight:900; text-align:center;
}
.plata {
    font-family:'Montserrat'; font-weight:900; font-size:1.4rem; 
    background:linear-gradient(to bottom,#fff,#888,#fff); 
    -webkit-background-clip:text; 
    -webkit-text-fill-color:transparent; 
    text-transform:uppercase; text-align:center;
}
.card {
    background:#050505; border:1px solid #1a1a1a; padding:20px; 
    border-top:3px solid #d4af37; text-align:center; min-height:500px;
}
.desc {color:#999; font-family:'Montserrat'; font-size:0.8rem; margin:15px 0;}
.btn {
    display:block; border:1px solid #bf953f; color:#bf953f!important; 
    padding:10px; font-weight:900; text-decoration:none; 
    font-size:0.7rem; letter-spacing:2px;
}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.7rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. RUTAS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

# 5. PRODUCTOS (ESTRUCTURA VERTICAL ANTI-CORTE)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">✨ ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">Sesión privada de 45 minutos. Claridad y guía espiritual absoluta.</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">25€</p>', unsafe_allow_html=True)
    m1 = "Saludos%20OPHAY.%20Deseo%20solicitar%20cita%20para%20Oraculo."
    st.markdown('<a href="' + W + m1 + '" class="btn">SOLICITAR CITA</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">📜 RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">Mazo de coleccionista con bord
