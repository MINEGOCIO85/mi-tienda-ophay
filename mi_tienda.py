import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY | Boutique & Destino", layout="wide")

# 2. ESTILO CSS "DIARIO MÍSTICO"
st.markdown("""
    <style>
    .main { background-color: #080808; color: #FFFFFF; }
    [data-testid="stAppViewContainer"] { background-color: #080808; }
    
    .logo-text {
        font-family: 'serif'; text-align: center; font-size: 3.5rem; letter-spacing: 15px;
        background: linear-gradient(145deg, #ffffff, #d4af37, #aa8a2e);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; margin: 0;
    }

    .card {
        background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 20px; border-radius: 15px; text-align: center;
    }

    /* SECCIÓN HORÓSCOPO POR FECHAS */
    .fecha-banner {
        text-align: center; color: #d4af37; font-family: 'serif';
        font-size: 1.2rem; letter-spacing: 4px; border: 1px solid #d4af37;
        padding: 10px; width: fit-content; margin: 20px auto; border-radius: 50px;
    }

    .camino-box {
        background: #111;
        border-radius: 20px; padding: 25px;
        border: 1px solid #222;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .camino-box:hover { border-color: #d4af37; background: #161616; }

    .signo-header {
        color: #d4af37; font-family: 'serif'; font-size: 1.6rem;
        border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 15px;
    }

    .meta-camino {
        background: rgba(212, 175, 55, 0.1); color: #d4af37;
        padding: 5px 15px; border-radius: 5px; font-size: 0.8rem;
        font-weight: bold; text-transform: uppercase;
    }

    .prediction-text { color: #bbbbbb; font-size: 1rem; line-height: 1.6; margin-top: 15px; }

    .stTabs [data-baseweb="tab"] { color: #666 !important; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; border-bottom-color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="logo-text">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#d4af37; letter-spacing:5px; font-size:0.7rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# 4. TIENDA (CORTA Y LIMPIA)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=180)
    st.markdown('<div style="color:#d4af37; margin-top:10px;">ORÁCULO</div><div>25€</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=180)
    st.markdown('<div style="color:#d4af37; margin-top:10px;">RIDER LUXE</div><div>45€</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", width=180)
    st.markdown('<div style="color:#d4af37; margin-top:10px;">AMATISTA</div><div>15€</div>', unsafe_allow_html=True)
    st.link_button("COMPRAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. SECCIÓN HORÓSCOPO DETALLADO
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center; color:#d4af37; font-family:serif; letter-spacing:4px;">✨ EL CAMINO DE LA SEMANA ✨</h2>', unsafe_allow_html=True)
st.markdown('<div class="fecha-banner">📅 20 DE ABRIL AL 26 DE ABRIL, 2026</div>', unsafe_allow_html=True)

tabs = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with tabs[0]:
    st.markdown('<div class="camino-box"><div class="signo-header">Aries, Leo, Sagitario</div><span class="meta-camino">El Camino de la Acción</span><p class="prediction-text"><b>Lunes-Miércoles:</b> Energía alta. Es el momento de iniciar trámites o conversaciones difíciles.<br><b>Jueves-Domingo:</b> C
