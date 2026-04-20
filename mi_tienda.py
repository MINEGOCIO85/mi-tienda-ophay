import streamlit as st
import urllib.parse

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")
TF = "34600000000" # <--- TU NÚMERO AQUÍ

# 2. CSS PLATA CROMADO Y ORO MACIZO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@900&display=swap');
.main { background-color: #000; }
[data-testid="stAppViewContainer"] { background-color: #000; }
.oro {
    font-family: 'Cinzel', serif;
    background: linear-gradient(180deg, #bf953f, #fcf6ba, #aa8232);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    font-weight: 900; text-align: center;
}
.plata-f {
    font-family: 'Montserrat'; font-weight: 900; font-size: 1.7rem;
    background: linear-gradient(to bottom, #fff 0%, #888 45%, #fff 50%, #666 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-transform: uppercase; line-height: 1.1;
}
.btn {
    display: block; background: linear-gradient(#bf953f, #aa8232);
    color: #000 !important; text-align: center; padding: 12px;
    font-family: 'Montserrat'; font-weight: 900; text-decoration: none;
    border-radius: 4px; margin-top: 10px; font-size: 0.8rem;
}
.card { background: #050505; border: 1px solid #1a1a1a; padding: 20px; border-top: 5px solid #d4af37; }
.h-d { color: #d4af37; font-size: 0.9rem; letter-spacing: 5px; font-weight: 900; margin-top: 20px;}
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:12px;font-weight:900;font-size:0.8rem;margin-bottom:40px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
u, r = "MINEGOCIO85", "mi-tienda-ophay"
img_b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c1, c2, c3 = st.columns(3)

def render_item(col, tit, desc, precio, img_url):
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(f"{img_b}/{img_url}")
        st.markdown(f'<p class="oro" style="font-size:1.5rem;">{tit}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#fff;font-size:0.8rem;text-align:center;font-weight:900;">{desc}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="
