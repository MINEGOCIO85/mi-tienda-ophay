import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO ORO & NOCHE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300&display=swap');
    
    .stApp { background-color: #0a0a0c; color: #ffffff; }
    
    .gold-text {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif;
        font-weight: 700;
    }

    .header-box {
        text-align: center;
        padding: 40px 0;
        border-bottom: 1px solid rgba(191, 149, 63, 0.3);
        margin-bottom: 40px;
    }
    
    .product-name {
        font-family: 'Cinzel', serif;
        color: #F7E7CE;
        font-size: 24px;
        margin-bottom: 10px;
    }
    
    .price {
        color: #D4AF37;
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 2px;
    }

    /* Botón Estilo Boutique */
    div.stButton > button {
        background-color: transparent !important;
        color: #C5A059 !important;
        border: 1px solid #C5A059 !important;
        border-radius: 0px !important;
        width: 100%;
        padding: 12px;
        transition: 0.4s;
    }
    
    div.stButton > button:hover {
        background-color: #C5A059 !important;
        color: #0a0a0c !important;
    }

    img {
        border-radius: 4px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.8);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<div class="header-box"><p class="gold-text" style="font-size:45px; letter-spacing:10px; margin:0;">OPHAY TAROT</p></div>', unsafe_allow_html=True)

# 4. FUNCIÓN DE PRODUCTO
def item(img_url, nombre, precio, desc):
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(img_url, use_container_width=True)
    with col2:
        st.markdown(f'<p class="product-name">{nombre}</p>', unsafe_allow_html=True)
        st.write(f"<p style='color:#94a3b8; font-style:italic; font-size:14px;'>{desc}</p>", unsafe_allow_html=True)
        st.markdown(f'<p class="price">{precio} €</p>', unsafe_allow_html=True)
        st.link_button(f"SOLICITAR", "https://wa.me/34600000000")
    st.write("<br>", unsafe_allow_html=True)

# 5. LISTADO CON FOTOS REALES (Enlaces ultra-estables)
# Foto 1: Cartas de Tarot reales
item("https://images.pexels.com/photos/7520773/pexels-photo-7520773.jpeg?auto=compress&cs=tinysrgb&w=800", 
     "LECTURA DEL DESTINO", "25", "Sesión privada para desvelar tu camino espiritual.")

# Foto 2: Mazo de cartas místico
item("https://images.pexels.com/photos/7524031/pexels-photo-7524031.jpeg?auto=compress&cs=tinysrgb&w=800", 
     "MAZO RIDER LUXE", "45", "Edición premium con detalles artísticos únicos.")

# Foto 3: Cristales/Amatista real
item("https://images.pexels.com/photos/4057082/pexels-photo-4057082.jpeg?auto=compress&cs=tinysrgb&w=800", 
     "AMATISTA SAGRADA", "15", "Piedra natural para limpieza y transmutación.")

# Foto 4: Vela encendida real
item("https://images.pexels.com/photos/6732997/pexels-photo-6732997.jpeg?auto=compress&cs=tinysrgb&w=800", 
     "VELA DE RITUAL", "12", "Cera orgánica para iluminar tus momentos de paz.")

# PIE DE PÁGINA
st.markdown("<center><p style='color:#5c6b89; font-size:10px; letter-spacing:5px; margin-top:50px;'>OPHAY • 2026</p></center>", unsafe_allow_html=True)
