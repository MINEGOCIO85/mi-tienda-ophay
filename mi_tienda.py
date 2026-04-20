import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="OPHAY | Boutique & Destino", layout="wide")

# 2. ESTILO CSS "LUXURY & MYSTIC"
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
        background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.2);
        padding: 20px; border-radius: 15px; text-align: center; height: 100%;
    }

    .fecha-banner {
        text-align: center; color: #d4af37; font-family: 'serif';
        font-size: 1.1rem; letter-spacing: 3px; border: 1px solid #d4af37;
        padding: 8px 20px; width: fit-content; margin: 20px auto; border-radius: 50px;
    }

    .camino-box {
        background: #111; border-radius: 20px; padding: 25px;
        border-left: 5px solid #d4af37; margin-top: 10px;
    }

    .signo-header { color: #d4af37; font-family: 'serif'; font-size: 1.5rem; margin-bottom: 5px; }
    .meta-camino { color: #aa8a2e; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; }
    .prediction-text { color: #cccccc; font-size: 1rem; line-height: 1.6; margin-top: 10px; }
    
    .stTabs [data-baseweb="tab"] { color: #666 !important; font-weight: bold; font-size: 1.1rem !important; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; border-bottom-color: #d4af37 !important; }
    
    /* Botón personalizado */
    .stButton>button {
        background-color: #d4af37 !important; color: black !important;
        border-radius: 20px !important; font-weight: bold !important; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="logo-text">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#d4af37; letter-spacing:5px; font-size:0.8rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# 4. TIENDA
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png")
    st.markdown('<div style="color:#d4af37; font-weight:bold; margin-top:10px;">ORÁCULO</div><div style="margin-bottom:15px;">25€</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<div style="color:#d4af37; font-weight:bold; margin-top:10px;">RIDER LUXE</div><div style="margin-bottom:15px;">45€</div>', unsafe_allow_html=True)
    st.link_button("ADQUIR
