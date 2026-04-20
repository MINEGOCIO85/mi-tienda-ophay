import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO ORO & NOCHE (CSS MEJORADO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital@1&family=Inter:wght@300&display=swap');
    
    .stApp { background-color: #08080a; color: #e0e0e0; }
    
    .gold-text {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif;
        font-weight: 700;
    }

    .header-box {
        text-align: center;
        padding: 60px 0;
        border-bottom: 1px solid rgba(191, 149, 63, 0.2);
        margin-bottom: 50px;
    }
    
    .product-name {
        font-family: 'Cinzel', serif;
        color: #F7E7CE;
        font-size: 24px;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }
    
    .price {
        color: #C5A059;
        font-size: 22px;
        font-weight: bold;
        letter-spacing: 3px;
        margin-top: 15px;
    }

    div.stButton > button {
        background-color: transparent !important;
        color: #C5A059 !important;
        border: 1px solid #C5A059 !important;
        border-radius: 0px !important;
        width: 100%;
        padding: 15px;
        transition: 0.5s ease;
        font-family: 'Cinzel', serif;
        letter-spacing: 2px;
    }
    
    div.stButton > button:hover {
        background-color: #C5A059 !important;
        color: #08080a !important;
        box-shadow: 0px 0px 20px rgba(197, 160, 89, 0.3);
    }

    img {
        border-radius: 2px;
        filter: sepia(20%) contrast(110%);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.9);
        border: 1px solid rgba(191, 149, 63, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<div class="header-box"><p class="gold-text" style="font-size:50px; letter-spacing:15px; margin:0;">OPHAY TAROT</p><p style="color:#666; letter-spacing:8px; font-size:10px; margin-top:10px;">EL ARTE DE LEER EL ALMA</p></div>', unsafe_allow_html=True)

# 4. FUNCIÓN DE PRODUCTO
def item(img_url, nombre, precio, desc):
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(img_url, use_container_width=True)
    with col2:
        st.markdown(f'<p class="product-name">{nombre}</p>', unsafe_allow_html=True)
        st.markdown(f"<p style='color:#a0a0a0; font-family:\"Playfair Display\", serif; font-style:italic; font-size:15px; line-height:1.6;'>{desc}</p>", unsafe_allow_html=True)
        st.markdown(f'<p class="price">{precio} €</p>', unsafe_allow_html=True)
        st.link_button(f"CONSULTAR", "https://wa.me/34600000000")
    st.write("<div style='margin-bottom:60px'></div>", unsafe_allow_html=True)

# 5. LISTADO CON FOTOS ESOTÉRICAS REALES
# Foto 1: Lectura mística con velas y sombras
item("https://images.unsplash.com/photo-1572025442646-866d16c84a54?auto=format&fit=crop&q=80&w=800", 
     "LECTURA DEL DESTINO", "25", "Una inmersión profunda en las energías que guían tu presente y futuro.")

# Foto 2: Mazo de cartas con detalles dorados
item("https://images.unsplash.com/photo-1612178991541-b48cc8e92a4d?auto=format&fit=crop&q=80&w=800", 
     "MAZO RIDER LUXE", "45", "78 arcanos en impresión de alta calidad con cantos metalizados.")

# Foto 3: Amatista de gran tamaño sobre altar
item("https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?auto=format&fit=crop&q=80&w=800", 
     "AMATISTA SAGRADA", "15", "Cristal de transmutación cargado ritualmente para protección.")

# Foto 4: Vela negra de ritual en la oscuridad
item("https://images.unsplash.com/photo-1601314167099-232775b3d6fd?auto=format&fit=crop&q=80&w=800", 
     "VELA DE RITUAL", "12", "Alquimia de aceites y cera para purificar y atraer claridad.")

# PIE DE PÁGINA
st.markdown("<center><p style='color:#444; font-size:9px; letter-spacing:6px; margin-top:40px;'>OPHAY • PARIS • MMXXVI</p></center>", unsafe_allow_html=True)
