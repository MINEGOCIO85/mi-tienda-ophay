import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO ORO REAL (Gradientes y Brillos)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300&display=swap');
    
    .stApp { background-color: #0a0a0c; color: #ffffff; }
    
    /* Efecto Oro Metálico */
    .gold-text {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif;
        font-weight: 700;
    }

    .header-box {
        text-align: center;
        padding: 50px 0;
        border-bottom: 1px solid rgba(191, 149, 63, 0.5);
        margin-bottom: 50px;
    }
    
    .gold-title {
        font-size: 55px;
        letter-spacing: 18px;
        margin: 0;
        filter: drop-shadow(0px 2px 2px rgba(0,0,0,0.5));
    }
    
    /* Marco con borde de oro fundido */
    .tarot-frame {
        width: 100%;
        height: 350px;
        border: 2px solid;
        border-image: linear-gradient(to bottom, #BF953F, #FCF6BA, #AA771C) 1;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 80px;
        background: radial-gradient(circle, #1a1a2e 0%, #0a0a0c 100%);
        box-shadow: 0px 0px 20px rgba(191, 149, 63, 0.2);
        margin-bottom: 20px;
    }

    .product-title {
        font-family: 'Cinzel', serif;
        color: #F7E7CE;
        font-size: 26px;
        margin-top: 10px;
    }
    
    .price-tag {
        font-family: 'Inter', sans-serif;
        color: #D4AF37;
        font-size: 22px;
        letter-spacing: 3px;
        font-weight: bold;
    }

    /* Botón Oro de Lujo */
    div.stButton > button {
        background: linear-gradient(135deg, #BF953F 0%, #FCF6BA 50%, #AA771C 100%) !important;
        color: #0a0a0c !important;
        font-family: 'Cinzel', serif !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 0px !important;
        width: 100%;
        padding: 18px;
        transition: 0.5s;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    div.stButton > button:hover {
        box-shadow: 0px 0px 25px rgba(252, 246, 186, 0.5);
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown("""
    <div class="header-box">
        <p class="gold-text gold-title">OPHAY TAROT</p>
        <p style="letter-spacing:8px; color:#94a3b8; font-family:Inter; font-size:12px; margin-top:10px;">
            LECTURAS SAGRADAS & ALQUIMIA
        </p>
    </div>
    """, unsafe_allow_html=True)

# 4. LISTADO DE PRODUCTOS
def draw_product(simbolo, nombre, precio, desc):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f'<div class="tarot-frame">{simbolo}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<p class="product-title">{nombre}</p>', unsafe_allow_html=True)
        st.write(f"<p style='color:#d1d5db; font-style:italic;'>{desc}</p>", unsafe_allow_html=True)
        st.markdown(f'<p class="price-tag">{precio} €</p>', unsafe_allow_html=True)
        st.link_button(f"SOLICITAR {nombre}", "
