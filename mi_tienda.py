import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "TOTAL RETAIL LUXURY"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }

/* Tipografías */
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2.2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 15px; min-height: 80px; }

/* EFECTO GLOW EN FOTOS (PUNTO 1) */
[data-testid="stImage"] img {
    border: 1px solid #333;
    transition: 0.5s ease;
    border-radius: 10px;
}
[data-testid="stImage"] img:hover {
    border: 1px solid #f1c40f;
    transform: scale(1.03);
    box-shadow: 0px 0px 20px rgba(241, 196, 15, 0.3);
}

/* WHATSAPP FLOTANTE */
.wa-wrap { position: fixed; bottom: 40px; right: 18%; z-index: 999999; display: flex; align-items: center; gap: 15px; }
.wa-bubble { background: #fff; color: #000; padding: 10px 20px; border-radius: 30px 30px 5px 30px; font-weight: 600; font-family: 'Montserrat'; font-size: 0.85rem; border: 1px solid #f1c40f; }
.wa-btn { background-color: #25d366; color: white !important; border-radius: 50% !important; width: 65px; height: 65px; display: flex; align-items: center; justify-content: center; font-size: 35px; text-decoration: none !important; }

/* TESTIMONIOS (PUNTO 3) */
.testimonio { font-style: italic; color: #ddd; text-align: center; font-family: 'Montserrat'; padding: 20px; border-left: 2px solid #f1c40f; margin: 10px; background: #111; border-radius: 0 15px 15px 0; }

/* REDES SOCIALES (PUNTO 4) */
.social-link { color: #f1c40f !important; text-decoration: none; font-family: 'Montserrat'; font-weight: 600; margin: 0 15px; font-size: 0.9rem; }
</style>

<div class="wa-wrap">
    <div class="wa-bubble">Asesoramiento Private Boutique ✨</div>
    <a href="https://wa.me/34684668398" class="wa-btn" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem; margin-top:-40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:8px; font-size:0.8rem; margin-bottom:40px;">BARCELONA • PRIVATE BOUTIQUE</p>',
