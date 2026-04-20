import streamlit as st

# 1. AJUSTES DE PÁGINA
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. ESTILO CSS: ORO Y PLATA DE ALTO IMPACTO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400;900&display=swap');
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
        font-weight: 900; font-size: 1.1rem; text-transform: uppercase; line-height: 1.4;
    }
    .desc-lujo { 
        color: #888; font-family: 'Montserrat'; font-size: 0.85rem; 
        text-align: center; font-style: italic; margin-bottom: 10px;
    }
    .box { background: #000; border: 1px solid #222; padding: 20px; border-radius: 20px; border-left: 6px solid #d4af37; }
    .h-dia { color: #d4af37; font-size: 0.8rem; letter-spacing: 4px; font-weight: bold; margin-bottom: 8px; }
    .precio { color: #d4af37; font-weight: bold; font-size: 1.2rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.75rem;margin-bottom:40px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA CON DESCRIPCIONES
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c1, c2, c3 = st.columns(3)

with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">ORÁCULO MÍSTICO</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-lujo">Cartas de edición limitada con acabado seda para revelar el destino.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-lujo">El mazo sagrado con bordes bañados en oro y estuche de terciopelo.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
with c3:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.4rem;">AMATISTA SAGRADA</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-lujo">Piedra natural de alta vibración para transmutar energías negativas.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">15€</p>', unsafe_allow_html=True)

# 5. DESTINO SEMANAL (BÚCLE SEGURO)
st.markdown("<br><h2 class='oro' style='font-size:2.2rem;'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

# --- TIERRA ---
with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;font-size:1.5rem;">TAURO • VIRGO • CAPRICORNIO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown("""<p class="plata-fuerte">LOS FR
