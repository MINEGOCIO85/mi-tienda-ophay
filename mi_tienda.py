import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique & Horóscopo", layout="wide")

# ESTILO LUXE CON PROFUNDIDAD (MÁS LUZ Y CONTRASTE)
st.markdown("""
    <style>
    /* Fondo con degradado para que no sea negro total */
    .main { 
        background: radial-gradient(circle, #1a1a1a 0%, #050505 100%); 
        color: #ffffff; 
    }
    [data-testid="stAppViewContainer"] { 
        background: radial-gradient(circle, #1a1a1a 0%, #050505 100%); 
    }
    
    /* Logo con brillo extra */
    .logo-main {
        background: linear-gradient(to bottom, #ffffff 0%, #d4af37 50%, #aa8a2e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        letter-spacing: 12px;
        font-family: 'serif';
        text-align: center;
        font-weight: bold;
        filter: drop-shadow(0px 0px 10px rgba(212, 175, 55, 0.3));
    }

    /* Tarjetas más claras para resaltar */
    .product-card {
        background: rgba(255, 255, 255, 0.05); /* Gris muy suave translúcido */
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 25px;
        text-align: center;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
        transition: 0.4s;
    }
    
    .product-card:hover {
        background: rgba(255, 255, 255, 0.1);
        border-color: #d4af37;
        transform: translateY(-5px);
    }

    /* Títulos y textos con más luz */
    .product-title {
        color: #fcf6ba; /* Oro clarito */
        font-size: 1.2rem;
        letter-spacing: 2px;
        margin-top: 15px;
        font-family: 'serif';
    }

    .stTabs [data-baseweb="tab"] {
        color: #888;
        font-weight: bold;
        font-size: 1rem;
    }
    .stTabs [aria-selected="true"] {
        color: #d4af37 !important;
        border-bottom-color: #d4af37 !important;
    }

    /* Botón vibrante */
    .stButton>button {
        background: #d4af37 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<div style="text-align:center; padding: 40px 0;"><h1 class="logo-main">OPHAY</h1><p style="color:#d4af37; letter-spacing:5px; font-size:0.9rem; font-weight:bold;">ALTA CLARIVIDENCIA • BARCELONA</p></div>', unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# --- TIENDA ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=220)
    st.markdown('<div class="product-title">ORÁCULO</div><div style="color:#fff; font-size:1.3rem; margin-bottom:15px; font-weight:bold;">25 €</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=220)
    st.markdown('<div class="product-title">RIDER LUXE</div><div style="color:#fff; font-size:1.3rem; margin-bottom:15px; font-weight:bold;">45 €</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR MAZO", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", width=220)
    st.markdown('<div class="product-title">AMATISTA</div><div style="color:#fff; font-size:1.3rem; margin-bottom:15px; font-weight:bold;">15 €</div>', unsafe_allow_html=True)
    st.link_button("COMPRAR GEMA", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

# --- HORÓSCOPO ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 style="text-align:center; color:#d4af37; font-family:serif; letter-spacing:4px;">✨ HORÓSCOPO SEMANAL ✨</h2>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with tab1:
    st.info("**Aries, Leo, Sagitario:** La energía de Marte te empuja a tomar decisiones valientes. No esperes a que las cosas pasen, ¡haz que pasen! Tu número es el 7.")
with tab2:
    st.info("**Tauro, Virgo, Capricornio:** Semana de estabilidad financiera. Un proyecto que dabas por perdido revive. Mantén los pies en la tierra pero la mente en tus metas.")
with tab3:
    st.info("**Géminis, Libra, Acuario:** La comunicación es tu fuerte estos días. Recibirás un mensaje importante de alguien que no esperabas. Abre tu mente.")
with tab4:
    st.info("**Cáncer, Escorpio, Piscis:** Tus emociones están a flor de piel. Es un buen momento para una limpieza energética con amatista. Confía en tu instinto.")

st.markdown("<br><br><p style='text-align:center; color:#666; font-size:0.8rem; letter-spacing:3px;'>© MMXXVI OPHAY PRIVATE COLLECTION</p>", unsafe_allow_html=True)
