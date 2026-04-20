import streamlit as st

# 1. Configuración de Base
st.set_page_config(page_title="OPHAY | Boutique & Horóscopo", layout="wide")

# 2. Estilo CSS "Luxury & Mystic"
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #FFFFFF; }
    [data-testid="stAppViewContainer"] { background-color: #0d0d0d; }
    
    .logo-text {
        font-family: 'serif'; text-align: center; font-size: 3.5rem; letter-spacing: 15px;
        background: linear-gradient(145deg, #fdfcfb, #d4af37, #aa8a2e);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; margin: 0;
    }

    /* Tarjetas de Producto */
    .card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 20px; border-radius: 15px; text-align: center;
    }
    .item-title { color: #d4af37; font-size: 1.1rem; margin-top: 10px; font-family: 'serif'; }

    /* --- SECCIÓN HORÓSCOPO (EL CAMBIO TOP) --- */
    .horoscopo-container {
        background: linear-gradient(180deg, #0d0d0d 0%, #1a150e 50%, #0d0d0d 100%);
        padding: 60px 20px; border-radius: 30px; border: 1px dashed rgba(212, 175, 55, 0.2);
        margin-top: 50px;
    }
    
    .horoscopo-header {
        font-family: 'serif'; text-align: center; color: #d4af37;
        font-size: 2.5rem; letter-spacing: 8px; font-weight: bold;
        text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.5);
        margin-bottom: 40px;
    }

    .signo-box {
        background: rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(212, 175, 55, 0.1);
        padding: 25px; border-radius: 20px;
        box-shadow: inset 0px 0px 20px rgba(212, 175, 55, 0.05);
        border-left: 4px solid #d4af37;
    }
    
    .signo-nombre {
        color: #d4af37; font-size: 1.5rem; font-family: 'serif';
        letter-spacing: 2px; margin-bottom: 10px; display: flex; align-items: center;
    }

    .prediction-text {
        color: #e0e0e0; font-size: 1.1rem; line-height: 1.6; font-style: italic;
    }

    /* Tabs Estilo Dorado */
    .stTabs [data-baseweb="tab"] { 
        color: #888 !important; font-size: 1.2rem !important; 
        padding: 10px 30px !important;
    }
    .stTabs [aria-selected="true"] { 
        color: #d4af37 !important; border-bottom: 3px solid #d4af37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabecera Boutique
st.markdown('<h1 class="logo-text">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#d4af37; letter-spacing:5px; font-size:0.8rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# 4. Sección Tienda
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", use_container_width=True)
    st.markdown('<div class="item-title">ORÁCULO</div><div style="margin-bottom:15px;">25€</div>', unsafe_allow_
