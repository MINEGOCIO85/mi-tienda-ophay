import streamlit as st
import urllib.parse

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. WHATSAPP (Pon tu número aquí)
TF = "34612345678" 

def link_wa(prod):
    m = urllib.parse.quote(f"Hola OPHAY, quiero info sobre: {prod}")
    return f"https://wa.me/{TF}?text={m}"

# 3. CSS PLATA FUERTE Y ORO
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
.plata-fuerte {
    font-family: 'Montserrat'; font-weight: 900; font-size: 1.7rem;
    background: linear-gradient(to bottom, #fff 0%, #888 45%, #fff 50%, #666 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-transform: uppercase; line-height: 1.1;
    filter: drop-shadow(2px 2px 2px #000);
}
.btn {
    display: block; background: linear-gradient(#bf953f, #aa8232);
    color: #000 !important; text-align: center; padding: 10px;
    font-family: 'Montserrat'; font-weight: 900; text-decoration: none;
    border-radius: 4px; margin-top: 10px; font-size: 0.8rem;
}
.card { background: #050505; border: 1px solid #1a1a1a; padding: 20px; border-top: 5px solid #d4af37; }
.h-dia { color: #d4af37; font-size: 0.9rem; letter-spacing: 5px; font-weight: 900; margin-top: 15px;}
</style>
""", unsafe_allow_html=True)

# 4. CABECERA
st.markdown('<h1 class="oro" style="font-size:6rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:15px;font-weight:900;font-size:0.8rem;margin-bottom:50px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 5. TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
col = st.columns(3)

items = [
    ("ORÁCULO", "SESIÓN 45 MIN. CLARIDAD Y GUÍA.", "25€", "primera%20foto%20isoterica.png"),
    ("RIDER LUXE", "MAZO PREMIUM BORDES ORO.", "45€", "SEGUNDA%20FOTO%20ESOTERICA.png"),
    ("AMATISTA", "GEODA NATURAL. PROTECCIÓN.", "15€", "Amatista.png")
]

for i, (n, d, p, img) in enumerate(items):
    with col[i]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(f"{b}/{img}")
        st.markdown(f'<p class="oro" style="font-size:1.5rem;">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#fff;font-size:0.8rem;text-align:center;font-weight:900;">{d}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#d4af37;text-align:center;font-weight:900;font-size:1.8rem;">{p}</p>', unsafe_allow_html=True)
        st.markdown(f'<a href="{link_wa(n)}" class="btn">RESERVAR AHORA</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# 6. DESTINO ELEMENTOS
st.markdown("<br><br><h2 class='oro' style='font-size:4rem;'>✨ DESTINO ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

def box
