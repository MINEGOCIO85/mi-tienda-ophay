import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Ophay Luxury Boutique", page_icon="💎", layout="centered")

# 2. SISTEMA DE ESTILO CSS (Verificado y Cerrado)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@200;400;600&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');
    .stApp { background-color: #ffffff; }
    .title-gold {
        font-family: 'Cinzel', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 400;
        font-size: 45px !important;
        letter-spacing: 10px;
        margin-top: 40px;
    }
    .subtitle-luxury {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        text-align: center;
        letter-spacing: 4px;
        font-size: 10px;
        text-transform: uppercase;
        margin-bottom: 50px;
    }
    h3 {
        font-family: 'Inter', sans-serif !important;
        color: #111827 !important; 
        font-weight: 600 !important;
        letter-spacing: 2px;
        font-size: 16px !important;
        text-transform: uppercase;
    }
    .desc {
        font-family: 'Playfair Display', serif !important;
        color: #4b5563 !important;
        font-size: 14px !important;
        font-style: italic;
        line-height: 1.8;
    }
    .precio {
        font-family: 'Inter', sans-serif !important;
        color: #111827 !important; 
        font-weight: 400;
        font-size: 19px;
    }
    div.stButton > button {
        background-color: #ffffff !important;
        color: #111827 !important;
        font-family: 'Inter', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 11px;
        border-radius: 0px !important;
        border: 1px solid #e5e7eb !important;
        padding: 15px;
        width: 100%;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        background-color: #111827 !important;
        color: #ffffff !important;
        letter-spacing: 5px;
    }
    [data-testid="stHorizontalBlock"] {
        padding: 40px 0px;
        border-bottom: 1px solid #f3f4f6;
        align-items: center;
    }
    img { transition: 0.8s; border-radius: 4px; }
    img:hover { transform: scale(1.03); }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="title-gold">OPHAY</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-luxury">Édition Limitée • Silver & Gold</p>', unsafe_allow_html=True)

# 4. FUNCIÓN DE PRODUCTO
def item_lujo(img, nom, precio, txt, link):
    c1, c2 = st.columns([1, 1.2]) 
    with c1:
        st.image(img, use_container_width=True)
    with c2:
        st.subheader(nom)
        st.markdown(f'<p class="desc">{txt}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="precio">{precio} €</p>', unsafe
