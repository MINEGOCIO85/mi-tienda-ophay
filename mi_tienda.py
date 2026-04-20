import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="OPHAY | Boutique & Horóscopo", layout="wide")

# 2. ESTILO CSS "GOLDEN MYSTIC" (RESISTENTE A ERRORES)
st.markdown("""
    <style>
    .main { background-color: #0a0a0a; color: #FFFFFF; }
    [data-testid="stAppViewContainer"] { background-color: #0a0a0a; }
    
    .logo-text {
        font-family: 'serif'; text-align: center; font-size: 3.5rem; letter-spacing: 12px;
        background: linear-gradient(145deg, #fdfcfb, #d4af37, #aa8a2e);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; margin: 0;
    }

    .card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(212, 175, 55, 0.2);
        padding: 20px; border-radius: 15px; text-align: center;
    }

    /* SECCIÓN HORÓSCOPO REDISEÑADA */
    .horoscopo-header {
        font-family: 'serif'; text-align: center; color: #d4af37;
        font-size: 2.2rem; letter-spacing: 6px; font-weight: bold;
        text-shadow: 0px 0px 10px rgba(212, 175, 55, 0.4);
        margin: 40px 0;
    }

    .signo-box {
        background: linear-gradient(145deg, #111, #1a1a1a);
        border: 1px solid rgba(212, 175, 55, 0.15);
        padding: 30px; border-radius: 20px;
        border-top: 3px solid #d4af37;
        margin-top: 10px;
    }
    
    .signo-nombre {
        color: #d4af37; font-size: 1.4rem; font-family: 'serif';
        letter-spacing: 2px; margin-bottom: 15px;
    }

    .prediction-text {
        color: #cccccc; font-size: 1.1rem; line-height: 1.7;
    }

    .stTabs [data-baseweb="tab"] { color: #777 !important; font-size: 1.1rem !important; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; border-bottom: 2px solid #d4af37 !important; }
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
    st.image(f"{base_url}/primera%20foto%20isoterica.png", use_container_width=True)
    st.markdown('<div style="color:#d4af37; font-size:1.2rem; margin-top:10px;">ORÁCULO</div><div style="font-size:1.1rem; margin-bottom:15px;">25€</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", use_container_width=True)
    st.markdown('<div style="color:#d4af37; font-size:1.2rem; margin-top:10px;">RIDER LUXE</div><div style="font-size:1.1rem; margin-bottom:15px;">45€</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", use_container_width=True)
    st.markdown('<div style="color:#d4af37; font-size:1.2rem; margin-top:10px;">AMATISTA</div><div style="font-size:1.1rem; margin-bottom:15px;">15€</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. HORÓSCOPO SEMANAL (ZONA DESTACADA)
st.markdown('<h2 class="horoscopo-header">✨ HORÓSCOPO SEMANAL ✨</h2>', unsafe_allow_html=True)

t1, t2, t3, t4 = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t1:
    st.markdown('<div class="signo-box"><div class="signo-nombre">♈ ARIES • ♌ LEO • ♐ SAGITARIO</div><p class="prediction-text">La energía de Marte te impulsa. Es semana de acción y resultados. No dudes de tu instinto, el fuego te guía hacia una oportunidad única el miércoles.</p></div>', unsafe_allow_html=True)

with t2:
    st.markdown('<div class="signo-box"><div class="signo-nombre">♉ TAURO • ♍ VIRGO • ♑ CAPRICORNIO</div><p class="prediction-text"><b>Momento de cosechar.</b> Un esfuerzo de hace meses da frutos económicos esta semana. Mantén el orden en tu mesa y en tu mente; el universo premia tu disciplina.</p></div>', unsafe_allow_html=True)

with t3:
    st.markdown('<div class="signo-box"><div class="signo-nombre">♊ GÉMINIS • ♎ LIBRA • ♒ ACUARIO</div><p class="prediction-text">Mercurio aclara tus ideas. Una conversación pendiente se resuelve a tu favor. El aire limpia tus dudas y te trae una propuesta creativa muy interesante.</p></div>', unsafe_allow_html=True)

with t4:
    st.markdown('<div class="signo-box"><div class="signo-nombre">♋ CÁNCER • ♏ ESCORPIO • ♓ PISCIS</div><p class="prediction-text">Tu intuición está en su punto máximo. Escucha tus sueños, traen mensajes clave. Es un buen momento para meditar con tu amatista y proteger tu paz interior.</p></div>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center; color:#333; font-size:0.8rem; letter-spacing:4px;'>© MMXXVI OPHAY COLLECTION • BARCELONA</p>", unsafe_allow_html=True)
