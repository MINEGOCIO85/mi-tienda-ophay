import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO CSS (Diseño místico sin fallos)
st.markdown("""
    <style>
    .stApp { background-color: #1a1a2e; color: #ffffff; }
    .gold-title {
        color: #C5A059;
        text-align: center;
        font-size: 45px;
        font-family: 'Serif';
        letter-spacing: 8px;
        margin-top: 30px;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid rgba(197, 160, 89, 0.3);
        margin-bottom: 25px;
        text-align: center;
    }
    .emoji-icon { font-size: 60px; margin-bottom: 15px; }
    .price-tag { color: #C5A059; font-size: 24px; font-weight: bold; }
    div.stButton > button {
        background-color: #C5A059;
        color: #1a1a2e;
        font-weight: bold;
        border-radius: 5px;
        border: none;
        width: 100%;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="gold-title">OPHAY TAROT</p>', unsafe_allow_html=True)
st.markdown("<center><p style='color:#94a3b8; letter-spacing:3px;'>EL DESTINO EN TUS MANOS</p></center>", unsafe_allow_html=True)
st.write("---")

# 4. FUNCIÓN DE PRODUCTO (USANDO ICONOS)
def draw_card(emoji, nom, precio, txt):
    with st.container():
        st.markdown(f"""
        <div class="card">
            <div class="emoji-icon">{emoji}</div>
            <h2 style="color:#F7E7CE;">{nom}</h2>
            <p style="font-style: italic; color:#d1d5db;">{txt}</p>
            <p class="price-tag">{precio} €</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(f"SOLICITAR {nom}", "https://wa.me/34600000000")
        st.write("<br>", unsafe_allow_html=True)

# 5. LISTADO DE PRODUCTOS
draw_card("🔮", "LECTURA DEL DESTINO", "25", "Consulta profunda para desvelar tu camino sagrado y conectar con tu propósito.")

draw_card("🃏", "MAZO DE TAROT RIDER", "45", "Edición de lujo con acabados dorados y guía mística para la interpretación.")

draw_card("💎", "CRISTAL AMATISTA", "15", "Piedra natural de alta vibración cargada bajo la luz de la luna llena.")

draw_card("🕯️", "VELA RITUAL SAGRADA", "12", "Aroma artesanal para atraer claridad mental y purificar tu energía.")

# PIE DE PÁGINA
st.write("---")
st.markdown("<center><small style='color:#5c6b89;'>OPHAY TAROT • 2026</small></center>", unsafe_allow_html=True)
