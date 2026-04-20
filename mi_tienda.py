import streamlit as st

# 1. CONFIG
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CSS FUERZA BRUTA
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@900&display=swap');
.main { background-color: #000; }
[data-testid="stAppViewContainer"] { background-color: #000; }
.oro {
    font-family: 'Cinzel', serif;
    background: linear-gradient(180deg, #bf953f, #fcf6ba, #aa8232);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    font-weight: 900; text-align: center; margin: 0;
}
.plata-f {
    font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 1.7rem;
    background: linear-gradient(to bottom, #fff 0%, #888 45%, #fff 50%, #444 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-transform: uppercase; line-height: 1.2;
}
.card { background: #050505; border: 1px solid #1a1a1a; padding: 20px; border-top: 5px solid #d4af37; text-align: center; }
.btn {
    display: inline-block; background: #d4af37; color: #000 !important;
    padding: 10px 20px; font-weight: 900; text-decoration: none; border-radius: 4px; margin-top: 10px;
}
.h-d { color: #d4af37; font-size: 0.9rem; letter-spacing: 5px; font-weight: 900; margin-top: 20px;}
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:5rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
u = "MINEGOCIO85"
r = "mi-tienda-ophay"
base = "https://raw.githubusercontent.com/" + u + "/" + r + "/main/"
c1, c2, c3 = st.columns(3)

# PRODUCTO 1
with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(base + "primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#fff;font-weight:900;">45 MINUTOS CLARIDAD</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">25€</p>', unsafe_allow_html=True)
    st.markdown('<a href="https://wa.me/34600000000" class="btn">RESERVAR</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# PRODUCTO 2
with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(base + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#fff;font-weight:900;">MAZO PREMIUM ORO</p>', unsafe_allow_html=True)
    st.markdown('<p class="oro" style="font-size:2rem;">45€</p>', unsafe_allow_html=True)
    st.markdown('<a href="https://wa.me/34600000000" class="btn">COMPRAR</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# PRODUCTO 3
with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(base + "Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.5rem;">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown('
