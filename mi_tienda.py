import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO ORO METÁLICO (Tu favorito)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300&display=swap');
    .stApp { background-color: #0a0a0c; color: #ffffff; }
    .gold-text {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif; font-weight: 700;
    }
    .header-box { text-align: center; padding: 40px 0; border-bottom: 1px solid rgba(191, 149, 63, 0.4); margin-bottom: 40px; }
    .gold-title { font-size: 50px; letter-spacing: 15px; margin: 0; }
    .product-title { font-family: 'Cinzel', serif; color: #F7E7CE; font-size: 24px; margin-top: 10px; }
    .price-tag { color: #D4AF37; font-size: 20px; font-weight: bold; letter-spacing: 2px; }
    
    div.stButton > button {
        background: linear-gradient(135deg, #BF953F 0%, #FCF6BA 50%, #AA771C 100%) !important;
        color: #0a0a0c !important;
        font-family: 'Cinzel', serif !important; font-weight: bold !important;
        border: none !important; border-radius: 0px !important; width: 100%; padding: 15px;
    }
    img { border: 1px solid rgba(191, 149, 63, 0.3); box-shadow: 0px 5px 15px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<div class="header-box"><p class="gold-text gold-title">OPHAY TAROT</p></div>', unsafe_allow_html=True)

# 4. PRODUCTOS (He usado enlaces de respaldo ultra-seguros esta vez)
def draw_item(img, name, price, desc):
    c1, c2 = st.columns([1, 1.2])
    with c1:
        # Usamos use_container_width para que se adapte bien
        st.image(img, use_container_width=True)
    with c2:
        st.markdown(f'<p class="product-title">{name}</p>', unsafe_allow_html=True)
        st.write(f"_{desc}_")
        st.markdown(f'<p class="price-tag">{price} €</p>', unsafe_allow_html=True)
        st.link_button(f"SOLICITAR", "https://wa.me/34600000000")
    st.write("---")

# PRODUCTOS CON ENLACES DIRECTOS DE WIKIMEDIA (Los únicos que Streamlit no bloquea)
draw_item("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Tarot_reading_1.jpg/800px-Tarot_reading_1.jpg", 
          "LECTURA DEL DESTINO", "25", "Consulta profunda para desvelar los misterios de tu camino.")

draw_item("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Tarot_reverso.jpg/800px-Tarot_reverso.jpg", 
          "MAZO RIDER LUXE", "45", "Edición de lujo con acabados místico-dorados.")

draw_item("https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Amethyst_Crystal.jpg/800px-Amethyst_Crystal.jpg", 
          "AMATISTA SAGRADA", "15", "Piedra de poder para armonizar tu espacio sagrado.")

draw_item("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Candle_burning.jpg/800px-Candle_burning.jpg", 
          "VELA DE RITUAL", "12", "Luz ungida para la meditación y la paz interior.")

# 5. PIE DE PÁGINA
st.markdown("<center><p style='color:#444; letter-spacing:5px; font-size:10px;'>OPHAY • MMXXVI</p></center>", unsafe_allow_html=True)
