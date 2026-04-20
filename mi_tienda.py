import streamlit as st

# 1. SETUP PROFESIONAL
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. CSS NIVEL DIOS (ORO PURO, PLATA REAL Y ANIMACIÓN)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400;900&display=swap');
.main { background-color: #050505; }
[data-testid="stAppViewContainer"] { background-color: #050505; }

/* ORO LÍQUIDO ANIMADO */
.oro-dios {
    font-family: 'Cinzel', serif;
    background: linear-gradient(90deg, #bf953f, #fcf6ba, #b38728, #fcf6ba, #aa8232);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900; text-align: center;
    animation: shine 3s linear infinite;
}

@keyframes shine { to { background-position: 200% center; } }

.boutique-god {
    color: #d4af37; font-family: 'Montserrat'; font-weight: 900;
    text-align: center; letter-spacing: 12px; font-size: 0.8rem;
    text-transform: uppercase; margin-bottom: 50px;
    text-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
}

.plata-god {
    font-family: 'Montserrat'; font-weight: 900; font-size: 1.1rem;
    background: linear-gradient(145deg, #ffffff, #888888, #ffffff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-transform: uppercase; line-height: 1.5;
}

.card {
    background: #000; border: 1px solid #1a1a1a; padding: 20px;
    border-radius: 15px; border-bottom: 4px solid #d4af37;
    transition: 0.3s;
}
.card:hover { border-bottom: 4px solid #fff; transform: translateY(-5px); }

.box-destino {
    background: #000; border-left: 8px solid #d4af37;
    padding: 30px; border-radius: 0 20px 20px 0; margin-bottom: 20px;
}
.h-dia { color: #d4af37; font-size: 0.85rem; letter-spacing: 5px; font-weight: 900; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA IMPACTANTE
st.markdown('<h1 class="oro-dios" style="font-size:5rem; margin-bottom:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="boutique-god">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA NIVEL BOUTIQUE
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c = st.columns(3)

with c[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro-dios" style="font-size:1.5rem;">ORÁCULO MÍSTICO</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#eee; font-size:0.85rem; text-align:center; font-weight:bold;">SESIÓN PRIVADA DE 45 MINUTOS</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#888; font-size:0.8rem; text-align:center; font-style:
