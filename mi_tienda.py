import streamlit as st

# 1. AJUSTES DE PÁGINA
st.set_page_config(page_title="OPHAY | Elite", layout="wide")

# 2. CSS: FONDO TEXTURIZADO Y RELIEVES METÁLICOS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@800&display=swap');
    
    .main { 
        background-color: #0a0a0a; 
        background-image: radial-gradient(#1a1a1a 1px, transparent 1px);
        background-size: 30px 30px;
        color: #FFFFFF; 
    }
    [data-testid="stAppViewContainer"] { background-color: #0a0a0a; }
    
    .oro {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #cfb53b 0%, #fcf6ba 30%, #d4af37 50%, #aa8232 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; text-align: center;
    }

    .plata {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(to bottom, #e2e2e2 0%, #ffffff 40%, #999999 60%, #666666 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800; text-transform: uppercase;
    }

    .box-zodiaco {
        background-color: #000000; 
        border: 1px solid #222;
        padding: 30px; 
        border-radius: 20px; 
        margin-top: 10px;
        box-shadow: 0px 10px 40px rgba(0,0,0,0.9);
        border-left: 4px solid #d4af37;
    }

    .header-dia { 
        color: #d4af37; font-size: 0.8rem; letter-spacing: 5px; 
        border-bottom: 1px solid #1a1a1a; padding-bottom: 5px; margin: 20px 0 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem; margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; letter-spacing:8px; font-size:0.7rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

# 4. PRODUCTOS
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c1, c2, c3 = st.columns(3)
with c1: st.image(f"{b}/primera%20foto%20isoterica.png", caption="ORÁCULO 25€")
with c2: st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png", caption="RIDER LUXE
