import streamlit as st

# 1. AJUSTES
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. CSS: ORO Y PLATA DE ALTO IMPACTO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@900&display=swap');
    .main { background-color: #050505; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    .oro {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #cfb53b, #fcf6ba, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; text-align: center;
    }
    .plata-fuerte {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(145deg, #fff 0%, #aaa 50%, #eee 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; font-size: 1.5rem; text-transform: uppercase;
    }
    .desc-lujo { color: #888; font-family: 'Montserrat'; font-size: 0.8rem; text-align: center; font-style: italic; }
    .box { background: #000; border: 1px solid #222; padding: 20px; border-radius: 15px; border-left: 6px solid #d4af37; }
    .h-dia { color: #d4af37; font-size: 0.9rem; letter-spacing: 4px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.7rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

c1, c2, c3 = st.columns(3)
with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-lujo">Revelaciones ancestrales en edición de seda.</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:bold;">25€</p>', unsafe_allow_html=True)
with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-lujo">Bordes de oro y terciopelo sagrado.</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:bold;">45€</p>', unsafe_allow_html=True)
with c3:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-lujo">Escudo energético de transmutación pura.</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:bold;">15€</p>', unsafe_allow_html=True)

# 5. DESTINO
st.markdown("<br><h2 class='oro'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
