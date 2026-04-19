import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Luxury", page_icon="💎", layout="centered")

# 2. ESTILO CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@200;400;600&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');
    .stApp { background-color: #ffffff; }
    .gold-title {
        font-family: 'Cinzel', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-align: center; font-size: 45px !important; letter-spacing: 10px; margin-top: 40px;
    }
    .sub-title {
        font-family: 'Inter', sans-serif; color: #94a3b8; text-align: center;
        letter-spacing: 4px; font-size: 10px; text-transform: uppercase; margin-bottom: 50px;
    }
    h3 { font-family: 'Inter', sans-serif !important; color: #111827 !important; letter-spacing: 2px; text-transform: uppercase; }
    .desc { font-family: 'Playfair Display', serif !important; color: #4b5563 !important; font-size: 14px !important; font-style: italic; line-height: 1.8; }
    .price { font-family: 'Inter', sans-serif !important; color: #111827 !important; font-size: 19px; }
    div.stButton > button {
        background-color: #ffffff !important; color: #111827 !important; font-family: 'Inter', sans-serif !important;
        text-transform: uppercase; letter-spacing: 3px; font-size: 11px; border-radius: 0px !important;
        border: 1px solid #e5e7eb !important; padding: 15px; width: 100%; transition: 0.4s;
    }
    div.stButton > button:hover { background-color: #111827 !important; color: #ffffff !important; letter-spacing: 5px; }
    [data-testid="stHorizontalBlock"] { padding: 40px 0px; border-bottom: 1px solid #f3f4f6; align-items: center; }
    img { transition: 0.8s; border-radius: 4px; }
    img:hover { transform: scale(1.03); }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="gold-title">OPHAY</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Édition Limitée • Silver & Gold</p>', unsafe_allow_html=True)

# 4. FUNCIÓN DE PRODUCTO (Simplificada para evitar errores)
def draw_item(img, nom, precio, txt, link):
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(img, use_container_width=True)
    with col2:
        st.subheader(nom)
        st.markdown(f'<p class="desc">{txt}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="price">{precio} €</p>', unsafe_allow_html=True)
        st.link_button("SOLICITAR INFORMACIÓN", link)

# 5. PRODUCTOS
draw_item("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700", "AURICULARES NOIRE PRESTIGE", "35", "Pureza acústica excepcional y confort premium.", "https://wa.me/34600000000")
draw_item("https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?w=700", "DRON EXPLORER HORIZON", "250", "Perspectiva privilegiada y aerodinámica de vanguardia.", "https://wa.me/34600000000")
draw_item("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=700", "SMARTWATCH PLATINUM CORE", "45", "La fusión definitiva entre tecnología y alta relojería.", "https://wa.me/34600000000")
draw_item("https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=700", "PROYECTOR LUMIÈRE 4K", "150", "Nitidez cinematográfica en un diseño minimalista.", "https://wa.me/34600000000")

st.markdown("<br><center><p style='color:#94a3b8; font-family:Inter; letter-spacing:4px; font-size:9px;'>OPHAY LUXURY RETAIL • 2026</p></center>", unsafe_allow_html=True)
