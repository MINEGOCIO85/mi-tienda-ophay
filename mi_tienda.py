import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. VARIABLES DE TEXTO (PARA EVITAR CORTES EN LÍNEA 69)
DESC_ORACULO = "Sesión privada de 45 minutos. Inmersión profunda, claridad y guía espiritual."
DESC_TAROT = "Mazo premium con bordes de oro. La herramienta para el buscador experto."
DESC_AMATISTA = "Geoda seleccionada a mano. Transmuta y protege tu aura de vibraciones densas."

# 3. CSS NIVEL DIOS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400;900&display=swap');
.main { background-color: #050505; }
[data-testid="stAppViewContainer"] { background-color: #050505; }
.oro-dios {
    font-family: 'Cinzel', serif;
    background: linear-gradient(90deg, #bf953f, #fcf6ba, #aa8232);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    font-weight: 900; text-align: center;
}
.plata-god {
    font-family: 'Montserrat'; font-weight: 900; font-size: 1.1rem;
    background: linear-gradient(145deg, #fff, #888, #fff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-transform: uppercase;
}
.card { background: #000; border: 1px solid #1a1a1a; padding: 20px; border-radius: 15px; border-bottom: 4px solid #d4af37; }
.h-dia { color: #d4af37; font-size: 0.85rem; letter-spacing: 5px; font-weight: 900; }
</style>
""", unsafe_allow_html=True)

# 4. CABECERA
st.markdown('<h1 class="oro-dios" style="font-size:4rem; margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:12px;font-weight:900;font-size:0.8rem;margin-bottom:40px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 5. TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c = st.columns(3)

with c[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro-dios" style="font-size:1.2rem;">ORÁCULO MÍSTICO</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#888;font-size:0.8rem;text-align:center;">{DESC_ORACULO}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:1.5rem;">25€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro-dios" style="font-size:1.2rem;">TAROT RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#888;font-size:0.8rem;text-align:center;">{DESC_TAROT}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:1.5rem;">45€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro-dios" style="font-size:1.2rem;">AMATISTA SAGRADA</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#888;font-size:0.8rem;text-align:center;">{DESC_AMATISTA}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:1.5rem;">15€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 6. DESTINO SEMANAL
st.markdown("<br><h2 class='oro-dios'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown
