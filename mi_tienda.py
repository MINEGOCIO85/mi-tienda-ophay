import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO CSS "OPHAY LUXURY"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;1,700&family=Inter:wght@300;400&display=swap');
    .stApp { background: radial-gradient(circle, #1a1a2e 0%, #16213e 100%); color: #ffffff; }
    .gold-title {
        font-family: 'Cinzel', serif !important;
        background: linear-gradient(to right, #C5A059, #F7E7CE, #B8860B);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center; font-size: 45px !important; letter-spacing: 12px; margin-top: 40px;
    }
    .sub-title {
        font-family: 'Inter', sans-serif; color: #94a3b8; text-align: center;
        letter-spacing: 5px; font-size: 10px; text-transform: uppercase; margin-bottom: 50px;
    }
    h3 { font-family: 'Cinzel', serif !important; color: #F7E7CE !important; letter-spacing: 2px; border:none !important; }
    .desc { font-family: 'Playfair Display', serif !important; color: #d1d5db !important; font-size: 14px !important; font-style: italic; line-height: 1.8; }
    .price { font-family: 'Inter', sans-serif !important; color: #C5A059 !important; font-weight: 600; font-size: 20px; }
    div.stButton > button {
        background: transparent !important; color: #F7E7CE !important; border: 1px solid #C5A059 !important;
        text-transform: uppercase; letter-spacing: 3px; font-size: 11px; padding: 15px; width: 100%;
    }
    div.stButton > button:hover { background-color: #C5A059 !important; color: #1a1a2e !important; }
    [data-testid="stHorizontalBlock"] { padding: 40px 0px; border-bottom: 1px solid rgba(197, 160, 89, 0.2); align-items: center; }
    img { border-radius: 8px; box-shadow: 0px 10px 30px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="gold-title">OPHAY TAROT</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Conexión Ancestral • 2026</p>', unsafe_allow_html=True)

# 4. FUNCIÓN
def draw_item(img, nom, precio, txt):
    c1, c2 = st.columns([1, 1.2])
    with c1: st.image(img, use_container_width=True)
    with c2:
        st.subheader(nom)
        st.markdown(f'<p class="desc">{txt}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="price">{precio} €</p>', unsafe_allow_html=True)
        st.link_button("RESERVAR", "https://wa.me/34600000000")

# 5. PRODUCTOS (URLs Ultra-estables)
# 1. LECTURA
draw_item("https://cdn.pixabay.com/photo/2019/11/04/13/28/tarot-4601131_1280.jpg", 
          "LECTURA DEL DESTINO", "25", "Consulta profunda para desvelar los hilos de tu futuro espiritual.")

# 2. MAZO
draw_item("https://cdn.pixabay.com/photo/2020/01/26/19/27/tarot-4795556_1280.jpg", 
          "MAZO TAROT LUXE", "45", "Edición de coleccionista con acabados dorados y diseño místico.")

# 3. CRISTAL
draw_item("https://cdn.pixabay.com/photo/2016/09/23/11/35/amethyst-1689392_1280.jpg", 
          "AMATISTA SAGRADA", "15", "Piedra de alta vibración para limpiar tu aura y tu hogar.")

# 4. VELA
draw_item("https://cdn.pixabay.com/photo/2017/08/17/10/47/candle-2650808_1280.jpg", 
          "VELA DE RITUAL", "12", "Cera natural preparada para atraer claridad y paz interior.")

st.markdown("<br><center><p style='color:#94a3b8; font-family:Inter; letter-spacing:4px; font-size:9px;'>OPHAY TAROT • 2026</p></center>", unsafe_allow_html=True)
