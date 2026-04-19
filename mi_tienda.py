import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury Silver", page_icon="🥈")

# 2. ESTILO PLATA Y DORADO
st.markdown("""
    <style>
    /* Fondo Plata Claro */
    .stApp {
        background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
    }
    
    /* Título con efecto Dorado sobre fondo claro */
    h1 {
        background: linear-gradient(to right, #B38728, #AA771C, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        font-size: 50px !important;
        padding-bottom: 20px;
    }

    /* Subtítulos de productos en Gris Oscuro Elegante */
    h3 {
        color: #1e293b !important; 
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: bold;
    }
    
    /* Textos descriptivos en Gris Carbón */
    p, span, label {
        color: #334155 !important;
    }
    
    /* Líneas divisorias en gris metalizado */
    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0,0,0,0), #94a3b8, rgba(0,0,0,0));
    }

    /* Botón Dorado (resalta mucho sobre el plata) */
    div.stButton > button {
        background: linear-gradient(to bottom, #D4AF37 0%, #B38728 100%);
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 12px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    
    div.stButton > button:hover {
        background: #1e293b; /* Cambia a oscuro al pasar el ratón */
        color: #D4AF37 !important;
        transform: translateY(-2px);
    }

    /* Bordes de las imágenes limpios */
    img {
        border-radius: 15px;
        box-shadow: 0px 10px 15px -3px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🥈 OPHAY SILVER EDITION")
st.write("---")

# PRODUCTO 1: DRON
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400")
with col2:
    st.subheader("🛸 Dron Explorer - 250€")
    st.link_button("🔱 PEDIR POR WHATSAPP", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 2: SMARTWATCH
col3, col4 = st.columns([1, 2])
with col3:
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400")
with col4:
    st.subheader("⌚ Smartwatch Ultra - 45€")
    st.link_button("🔱 PEDIR POR WHATSAPP", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 3: PROYECTOR
col5, col6 = st.columns([1, 2])
with col5:
    st.image("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400")
with col6:
    st.subheader("📽️ Proyector 4K - 150€")
    st.link_button("🔱 PEDIR POR WHATSAPP", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 4: AURICULARES
col7, col8 = st.columns([1, 2])
with col7:
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400")
with col8:
    st.subheader("🎧 Auriculares Gamer - 35€")
    st.link_button("🔱 PEDIR POR WHATSAPP", "https://wa.me/34600000000")

st.write("---")
st.info("📦 Calidad garantizada en cada pedido.")
