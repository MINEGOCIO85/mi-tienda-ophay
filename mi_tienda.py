import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury", page_icon="✨")

# 2. ESTILO DORADO DE LUJO
st.markdown("""
    <style>
    /* Fondo Negro Profundo */
    .stApp {
        background-color: #000000;
    }
    
    /* Título con efecto Dorado */
    h1 {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        font-size: 50px !important;
    }

    /* Subtítulos de productos en Dorado suave */
    h3 {
        color: #D4AF37 !important; /* Oro Clásico */
        font-family: 'Playfair Display', serif;
    }
    
    /* Textos en blanco hueso para elegancia */
    p, span, label {
        color: #E5E5E5 !important;
    }
    
    /* Líneas divisorias doradas */
    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0,0,0,0), #D4AF37, rgba(0,0,0,0));
    }

    /* Botón VIP Dorado */
    div.stButton > button {
        background: linear-gradient(to bottom, #D4AF37 0%, #B38728 100%);
        color: black !important;
        border-radius: 5px;
        border: 1px solid #FCF6BA;
        padding: 12px;
        font-weight: bold;
        font-size: 16px;
        transition: 0.4s;
    }
    
    div.stButton > button:hover {
        background: #FCF6BA;
        transform: scale(1.02);
        color: black !important;
    }

    /* Bordes de las imágenes en dorado */
    img {
        border: 2px solid #D4AF37;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ OPHAY LUXURY ✨")
st.write("---")

# PRODUCTO 1: DRON
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400")
with col2:
    st.subheader("🛸 Dron Explorer - 250€")
    st.link_button("🔱 PEDIR EXCLUSIVIDAD", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 2: SMARTWATCH
col3, col4 = st.columns([1, 2])
with col3:
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400")
with col4:
    st.subheader("⌚ Smartwatch Ultra - 45€")
    st.link_button("🔱 PEDIR EXCLUSIVIDAD", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 3: PROYECTOR
col5, col6 = st.columns([1, 2])
with col5:
    st.image("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400")
with col6:
    st.subheader("📽️ Proyector 4K - 150€")
    st.link_button("🔱 PEDIR EXCLUSIVIDAD", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 4: AURICULARES
col7, col8 = st.columns([1, 2])
with col7:
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400")
with col8:
    st.subheader("🎧 Auriculares Gamer - 35€")
    st.link_button("🔱 PEDIR EXCLUSIVIDAD", "https://wa.me/34600000000")

st.write("---")
st.info("💎 Selección exclusiva de productos de alta gama.")
