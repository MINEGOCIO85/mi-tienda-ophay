import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO CSS (Compacto y seguro)
st.markdown("""
    <style>
    .stApp { background-color: #1a1a2e; color: #ffffff; }
    .gold-title {
        color: #C5A059;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        letter-spacing: 5px;
        margin-bottom: 0px;
    }
    .price { color: #C5A059; font-weight: bold; font-size: 20px; }
    div.stButton > button {
        background-color: transparent;
        color: #C5A059;
        border: 1px solid #C5A059;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #C5A059;
        color: #1a1a2e;
    }
    hr { border-color: rgba(197, 160, 89, 0.3); }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="gold-title">OPHAY TAROT</p>', unsafe_allow_html=True)
st.center = st.markdown("<center><small>LECTURAS Y ARTE ESOTÉRICO</small></center>", unsafe_allow_html=True)
st.write("---")

# 3. FUNCIÓN DE PRODUCTO
def draw_item(img, nom, precio, txt):
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.image(img, use_container_width=True)
    with c2:
        st.subheader(nom)
        st.write(txt)
        st.markdown(f'<p class="price">{precio} €</p>', unsafe_allow_html=True)
        st.link_button("RESERVAR LECTURA", "https://wa.me/34600000000")
    st.write("---")

# 4. PRODUCTOS (Con enlaces de Wikipedia/Wikimedia - Ultra estables)

# Foto 1: Lectura (Representada por una carta clásica)
draw_item("https://upload.wikimedia.org/wikipedia/commons/3/3a/RWS_Tarot_00_Fool.jpg", 
          "LECTURA DEL DESTINO", "25", "Consulta profunda para desvelar tu camino sagrado.")

# Foto 2: Mazo
draw_item("https://upload.wikimedia.org/wikipedia/commons/d/db/Tarot_reverso.jpg", 
          "MAZO DE TAROT", "45", "Edición clásica con acabados premium.")

# Foto 3: Cristal
draw_item("https://upload.wikimedia.org/wikipedia/commons/a/af/Amethyst_Crystal.jpg", 
          "CRISTAL AMATISTA", "15", "Piedra natural cargada bajo la luna llena.")

# Foto 4: Vela
draw_item("https://upload.wikimedia.org/wikipedia/commons/f/f2/Candle_burning.jpg", 
          "VELA RITUAL", "12", "Luz y aroma para purificar tu energía.")

st.markdown("<center><small>OPHAY TAROT • 2026</small></center>", unsafe_allow_html=True)
