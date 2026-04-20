import streamlit as st

# 1. Configuración de Base
st.set_page_config(page_title="OPHAY | Boutique", layout="wide")

# 2. Estilo CSS "Boutique de Lujo"
st.markdown("""
    <style>
    /* Fondo Gris Carbón (más elegante que el negro puro) */
    .main { 
        background-color: #121212; 
        color: #FFFFFF; 
    }
    [data-testid="stAppViewContainer"] { background-color: #121212; }
    
    /* Logo Ophay */
    .logo-text {
        font-family: 'serif';
        text-align: center;
        font-size: 4rem;
        letter-spacing: 15px;
        background: linear-gradient(145deg, #fdfcfb, #d4af37, #aa8a2e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin: 0;
    }

    /* Tarjetas de Producto */
    .card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        transition: 0.3s;
    }
    .card:hover {
        border-color: #d4af37;
        background: rgba(212, 175, 55, 0.05);
    }

    /* Títulos y Precios */
    .item-title { color: #d4af37; font-size: 1.4rem; margin-top: 15px; font-family: 'serif'; }
    .item-price { color: #FFFFFF; font-size: 1.2rem; margin-bottom: 20px; font-weight: 200; }

    /* Pestañas del Horóscopo */
    .stTabs [data-baseweb="tab"] { color: #888 !important; font-size: 1.1rem; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; border-bottom-color: #d4af37 !important; }
    
    /* Imágenes */
    [data-testid="stImage"] img { border-radius: 10px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabecera
st.markdown('<h1 class="logo-text">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#d4af37; letter-spacing:5px; font-size:0.8rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 4. Variables de imágenes
user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# 5. Sección Tienda
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", use_container_width=True)
    st.markdown('<div class="item-title">ORÁCULO</div><div class="item-price">25€</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398", width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", use_container_width=True)
    st.markdown('<div class="item-title">RIDER LUXE</div><div class="item-price">45€</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398", width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", use_container_width=True)
    st.markdown('<div class="item-title">AMATISTA</div><div class="item-price">15€</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", "https://wa.me/34684668398", width="stretch")
    st.markdown('</div>', unsafe_allow_html=True)

# 6. Sección Horóscopo
st.markdown("<br><br><h2 style='text-align:center; color:#d4af37; font-family:serif;'>✨ HORÓSCOPO SEMANAL ✨</h2>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t1:
    st.markdown("### Aries, Leo, Sagitario\nLa Luna en trígono con Marte te da la fuerza que necesitabas. Es semana de **acción directa**. No pidas permiso, pide perdón después.")
with t2:
    st.markdown("### Tauro, Virgo, Capricornio\nMomento de cosechar. Un esfuerzo de hace meses da frutos económicos esta semana. **Mantén el orden** en tu mesa y en tu mente.")
with t3:
    st.markdown("### Géminis, Libra, Acuario\nLa comunicación fluye. Recibirás una noticia por WhatsApp que cambiará tus planes del fin de semana. **Escucha más de lo que hablas**.")
with t4:
    st.markdown("### Cáncer, Escorpio, Piscis\nTu intuición está disparada. Si sientes que algo no encaja, retírate. Usa tu **Amatista** para filtrar las energías negativas de los demás.")

st.markdown("<br><p style='text-align:center; color:#444; font-size:0.7rem; letter-spacing:5px;'>© MMXXVI OPHAY COLLECTION</p>", unsafe_allow_html=True)
