import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury Silver", page_icon="🥈")

# 2. ESTILO: FONDO PLATA + BOTÓN DORADO + TIPOGRAFÍA PREMIUM
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    /* Fondo Plata Metalizado */
    .stApp {
        background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
    }
    
    /* Título: Fuente 'Playfair Display' (Estilo Revista de Lujo) */
    h1 {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        font-size: 55px !important;
        letter-spacing: -1px;
    }

    /* Nombres de productos: 'Montserrat' (Moderna y Limpia) */
    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #0f172a !important; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 20px !important;
    }
    
    /* Textos y precios */
    p, span, label {
        font-family: 'Montserrat', sans-serif !important;
        color: #475569 !important;
        font-weight: 400;
    }
    
    /* Botón Dorado con letra refinada */
    div.stButton > button {
        background: linear-gradient(to bottom, #D4AF37 0%, #B38728 100%);
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700;
        border-radius: 0px; /* Botones cuadrados son más 'fashion' */
        border: none;
        padding: 15px;
        transition: all 0.5s;
    }
    
    div.stButton > button:hover {
        background: #000000;
        color: #D4AF37 !important;
    }

    /* Imágenes con sombra suave */
    img {
        border-radius: 4px;
        box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("OPHAY SILVER")
st.write("---")

# PRODUCTO 1: DRON
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400")
with col2:
    st.subheader("Dron Explorer")
    st.write("Tecnología de vuelo avanzada. **250€**")
    st.link_button("🔱 ADQUIRIR", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 2: SMARTWATCH
col3, col4 = st.columns([1, 2])
with col3:
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400")
with col4:
    st.subheader("Smartwatch Ultra")
    st.write("Elegancia y salud en tu muñeca. **45€**")
    st.link_button("🔱 ADQUIRIR", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 3: PROYECTOR
col5, col6 = st.columns([1, 2])
with col5:
    st.image("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400")
with col6:
    st.subheader("Proyector 4K")
    st.write("Cine en casa con la mejor resolución. **150€**")
    st.link_button("🔱 ADQUIRIR", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 4: AURICULARES
col7, col8 = st.columns([1, 2])
with col7:
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400")
with col8:
    st.subheader("Auriculares Gamer")
    st.write("Sonido inmersivo profesional. **35€**")
    st.link_button("🔱 ADQUIRIR", "https://wa.me/34600000000")

st.write("---")
st.caption("OPHAY LUXURY © 2026 - PRODUCTOS EXCLUSIVOS")
