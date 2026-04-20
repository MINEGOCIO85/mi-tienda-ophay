import streamlit as st

# 1. SETUP & CSS COMPACTO
st.set_page_config(page_title="OPHAY ELITE", layout="wide")
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@400;900&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.plata{font-family:'Montserrat';font-weight:900;font-size:1.3rem;background:linear-gradient(to bottom,#fff,#888,#fff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-transform:uppercase;text-align:center;}
.card{background:#050505;border:1px solid #111;padding:20px;border-top:3px solid #d4af37;text-align:center;min-height:450px;}
.desc{color:#777;font-family:'Montserrat';font-size:0.8rem;margin:10px 0;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:10px;font-weight:900;text-decoration:none;font-size:0.7rem;letter-spacing:2px;}
</style>""", unsafe_allow_html=True)

# 2. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.6rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 3. RUTAS
B="https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W="https://wa.me/34684668398?text="
c1,c2,c3=st.columns(3)

# 4. PRODUCTOS
with c1:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">✨ ORÁCULO</p>',unsafe_allow_html=True)
    st.markdown('<p class="desc">Sesión privada 45 min. Guía absoluta.</p>',unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:1.8rem;">25€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Deseo%20cita%20Oraculo" class="btn">RESERVAR</a></div>',unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">📜 RIDER LUXE</p>',unsafe_allow_html=True)
    st.markdown('<p class="desc">Edición oro. Arte sacro premium.</p>',unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:1.8rem;">45€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Deseo%20Rider%20Luxe" class="btn">ADQUIRIR</a></div>',unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">',unsafe_allow_html=True)
    st.image(B+"Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">💎 AMATISTA</p>',unsafe_allow_html=True)
    st.markdown('<p class="desc">Protección y transmutación energética.</p>',unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:1.8rem;">15€</p>',unsafe_allow_html=True)
    st.markdown('<a href="'+W+'Deseo%20Amatista" class="btn">CONSULTAR</a></div>',unsafe_allow_html=True)

# 5. DESTINO
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>✨ DESTINO ✨</h2>",unsafe_allow_html=True)
st.markdown('<p class="plata">🌱 TIERRA: ÉXITO.<br>🔥 FUEGO: ACC
