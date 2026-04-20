import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY", layout="wide")

# 2. CSS COMPACTO
st.markdown("""
<style>
.main { background-color: #050505; }
[data-testid="stAppViewContainer"] { background-color: #050505; }
.oro {
    font-family: serif;
    background: linear-gradient(#cfb53b, #aa8232);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold; text-align: center;
}
.plata {
    font-family: sans-serif;
    color: #eee; font-weight: 900; 
    font-size: 1.1rem; text-transform: uppercase;
}
.desc { color: #888; font-size: 0.8rem; text-align: center; }
.box { border-left: 5px solid #d4af37; padding: 15px; background: #000; }
.h { color: #d4af37; font-size: 0.8rem; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:8px;font-size:0.7rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c = st.columns(3)

with c[0]:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO 25€</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">Edición seda y oro.</p>', unsafe_allow_html=True)
with c[1]:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE 45€</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">Terciopelo y bordes oro.</p>', unsafe_allow_html=True)
with c[2]:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro">AMATISTA 15€</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">Energía pura natural.</p>', unsafe_allow_html=True)

# 5. DESTINO
st.markdown("<br><h2 class='oro'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="h">LUNES-MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">FRUTOS DE TU ESFUERZO LLEGAN.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">PAGO CONFIRMADO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">LIMPIA TU HOGAR. ATRAE ABUNDANCIA.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[1]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="h">LUNES-MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">MARTE IMPULSA TU NEGOCIO.</p>',
