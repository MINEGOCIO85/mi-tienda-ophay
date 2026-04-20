import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO MÍSTICO (Inspirado en Tarotoo)
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
    h3 { font-family: 'Cinzel', serif !important; color: #F7E7CE !important; letter-spacing: 2px; }
    .desc { font-family: 'Playfair Display', serif !important; color: #d1d5db !important; font-size: 14px !important; font-style: italic; line-height: 1.8; }
    .price { font-family: 'Inter', sans-serif !important; color: #C5A059 !important; font-weight: 600; font-size: 20px; }
    div.stButton > button {
        background: transparent !important; color: #F7E7CE !important; font-family: 'Inter', sans-serif !important;
        text-transform: uppercase; letter-spacing: 3px; font-size: 11px; border-radius: 0px !important;
        border: 1px solid #C5A059 !important; padding: 15px; width: 100%; transition: 0.4s;
    }
    div.stButton > button:hover { background-color: #C5A059 !important; color: #1a1a2e !important; box-shadow: 0px 0px 15px #C5A059; }
    [data-testid="stHorizontalBlock"] { padding: 40px 0px; border-bottom: 1px solid rgba(197, 160, 89, 0.2); align-items: center; }
    img { transition: 0.8s; border-radius: 5px; box-shadow: 0px 5px 15px rgba(0,0,0,0.5); }
    img:hover { transform: scale(1.03) rotate(1deg); }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="gold-title">OPHAY TAROT</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Lecturas Sagradas & Arte Esotérico</p>', unsafe_allow_html=True)

# 4. FUNCIÓN (Compacta)
def draw_item(img, nom, precio, txt, link):
    c1, c2 = st.columns([1, 1.2])
    with c1: st.image(img, use_container_width=True)
    with c2:
        st.subheader(nom)
        st.markdown(f'<p class="desc">{txt}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="price">{precio} €</p>', unsafe_allow_html=True)
        st.link_button("RESERVAR LECTURA", link)

# 5. PRODUCTOS (En una sola línea para evitar cortes)

# --- PRODUCTO 1: INTEGRACIÓN DE LA IMGEN GENERADA ---
draw_item("image_0.png", "LECTURA DEL DESTINO", "25", "Consulta profunda para desvelar tu camino sagrado.", "https://wa.me/34600000000")

# --- PRODUCTOS RESTANTES ---
draw_item("https://images.unsplash.com/photo-1612178991541-b48cc8e92a4d?w=700", "MAZO DE TAROT RIDER", "45", "Edición de lujo con acabados dorados y guía mística.", "https://wa.me/34600000000")
draw_item("https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=700", "CRISTAL AMATISTA", "15", "Piedra natural cargada bajo la luz de la luna llena.", "https://wa.me/34600000000")
draw_item("https://images.unsplash.com/photo-1601314167099-232775b3d6fd?w=700", "VELA RITUAL SAGRADA", "12", "Aroma para atraer claridad mental y energía positiva.", "https://wa.me/34600000000")

st.markdown("<br><center><p style='color:#94a3b8; font-family:Inter; letter-spacing:4px; font-size:9px;'>OPHAY TAROT • 2026</p></center>", unsafe_allow_html=True)
