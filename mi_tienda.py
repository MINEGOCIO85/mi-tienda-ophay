import streamlit as st

# 1. SETUP DE PÁGINA
st.set_page_config(page_title="OPHAY | Elite Esoteric", layout="wide")

# 2. CSS DE ALTO CONTRASTE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@300;800&display=swap');

    .main { background-color: #050505; color: #FFFFFF; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    .oro-title {
        font-family: 'Cinzel', serif;
        background: linear-gradient(145deg, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800; text-align: center; letter-spacing: 3px;
    }

    .plata-sub {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(145deg, #888, #fff, #999, #eee, #777);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800; text-transform: uppercase; letter-spacing: 2px;
    }

    .card-dark {
        background: rgba(20, 20, 20, 0.9);
        border: 2px solid #333;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    .day-header {
        color: #d4af37;
        font-family: 'Montserrat', sans-serif;
        font-size: 0.9rem;
        font-weight: 300;
        letter-spacing: 5px;
        border-bottom: 1px solid #222;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGOTIPO OPHAY
st.markdown('<h1 class="oro-title" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; letter-spacing:10px; font-size:0.8rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

# 4. PRODUCTOS
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
col_p1, col_p2, col_p3 = st.columns(3)
with col_p1: st.image(f"{b}/primera%20foto%20isoterica.png", caption="ORÁCULO 25€")
with col_p2: st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png", caption="RIDER LUXE 45€")
with col_p3: st.image(f"{b}/Amatista.png", caption="AMATISTA 15€")

# 5. LECTURAS
# CORRECCIÓN AQUÍ: Usamos comillas simples para las clases CSS
st.markdown("<br><h2 class='oro-title'>✨ EL CAMINO DEL DESTINO ✨</h2>", unsafe_allow_html=True)
tabs = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

def render_signo(signos, camino, lun_mie, fin_sem):
    st.markdown('<div class="card-dark">', unsafe_allow_html=True)
    st.markdown(f'<h2 class="oro-title" style="font-size:1.8rem; text-align:left;">{signos}</h2>', unsafe_allow_html=True)
    st.markdown(f'<h3 class="plata-sub" style="font-size:1rem; margin-bottom:25px;">{camino}</h3>', unsafe_allow_html=True)
    
    st.markdown('<p class="day-header">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:1.2rem; font-weight:700; color:#fff;">{lun_mie}</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="day-header" style="margin-top:20px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:1.2rem; font-weight:700; color:#fff;">{fin_sem}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[0]:
    render_signo("ARIES • LEO • SAGITARIO", "EL CAMINO DE LA ACCIÓN", 
                 "MARTE IMPULSA TU NEGOCIO. CIERRA TRATOS YA.", 
                 "SEÑAL CLAVE EL DOMINGO. ESCUCHA TU INSTINTO.")

with tabs[1]:
    render_signo("TAURO • VIRGO • CAPRICORNIO", "EL CAMINO DE LA COSECHA",
