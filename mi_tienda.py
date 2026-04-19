import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury Silver", page_icon="🥈")

# 2. ESTILO MEJORADO (Tipografía y espaciado)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,700;1,300&family=Playfair+Display:wght@700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    h1 {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        font-size: 55px !important;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #0f172a !important; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px !important;
    }
    
    /* Estilo para la descripción elegante */
    .desc {
        font-family: 'Montserrat', sans-serif !important;
        color: #64748b !important;
        font-size: 14px !important;
        font-style: italic;
        margin-bottom: 15px !important;
        line-height: 1.4;
    }

    .precio {
        font-family: 'Montserrat', sans-serif !important;
        color: #1e293b !important;
        font-weight: 700;
        font-size: 18px;
    }
    
    div.stButton > button {
        background: linear-gradient(to bottom, #D4AF37 0%, #B38728 100%);
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700;
        border-radius: 0px;
        border: none;
        padding: 10px;
        transition: 0.4s;
    }
    
    div.stButton > button:hover {
        background: #000000;
        transform: translateY(-2px);
    }

    img {
        border-radius: 2px;
        box-shadow: 10px 10px 30px #cbd5e1;
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
    st.markdown('<p class="desc">Libertad absoluta en el aire con captura de imagen cinematográfica de alta precisión.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">250€</p>', unsafe_allow_html=True)
    st.link_button("🔱 ADQUIRIR", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 2: SMARTWATCH
col3, col4 = st.columns([1, 2])
with col3:
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400")
with col4:
    st.subheader("Smartwatch Ultra")
    st.markdown('<p class="desc">La perfecta armonía entre el diseño vanguardista y el control total de tu bienestar diario.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.link_button("🔱 ADQUIRIR", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 3: PROYECTOR
col5, col6 = st.columns([1, 2])
with col5:
    st.image("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400")
with col6:
    st.subheader("Proyector 4K")
    st.markdown('<p class="desc">Transforma cualquier espacio en una experiencia visual inmersiva con nitidez incomparable.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">150€</p>', unsafe_allow_html=True)
    st.link_button("🔱 ADQUIRIR", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 4: AURICULARES
col7, col8 = st.columns([1, 2])
with col7:
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400")
with col8:
    st.subheader("Auriculares Gamer")
    st.markdown('<p class="desc">Pureza acústica y confort premium diseñados para las sesiones más exigentes.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">35€</p>', unsafe_allow_html=True)
    st.link_button("🔱 ADQUIRIR", "https://wa.me/34600000000")

st.write("---")
st.caption("OPHAY LUXURY © 2026 - EXCLUSIVE SELECTION")
