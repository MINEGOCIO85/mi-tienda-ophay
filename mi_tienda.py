import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay VIP", page_icon="🛍️")

# 2. ESTILO PERSONALIZADO (Color de fondo y fuentes)
st.markdown("""
    <style>
    /* Fondo con degradado profesional */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Títulos en blanco brillante */
    h1 {
        color: #f8fafc !important;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Subtítulos de productos */
    h3 {
        color: #38bdf8 !important; /* Azul cian suave */
    }
    
    /* Color de los textos normales */
    p, span, label {
        color: #cbd5e1 !important;
    }
    
    /* Estilo para las tarjetas de producto (separadores) */
    hr {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0));
    }

    /* Botón de WhatsApp mejorado */
    div.stButton > button {
        background-color: #0284c7;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #0ea5e9;
        border: 1px solid white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 TIENDA OPHAY")
st.write("---")

# PRODUCTO 1: DRON
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400", caption="Dron Explorer")
with col2:
    st.subheader("1. Dron Explorer - 250€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000?text=Hola,quiero+el+Dron")

st.write("---")

# PRODUCTO 2: SMARTWATCH
col3, col4 = st.columns([1, 2])
with col3:
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", caption="Smartwatch Ultra")
with col4:
    st.subheader("2. Smartwatch Ultra - 45€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000?text=Hola,quiero+el+Smartwatch")

st.write("---")

# PRODUCTO 3: PROYECTOR
col5, col6 = st.columns([1, 2])
with col5:
    st.image("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400", caption="Proyector 4K")
with col6:
    st.subheader("3. Proyector 4K - 150€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000?text=Hola,quiero+el+Proyector")

st.write("---")

# PRODUCTO 4: AURICULARES
col7, col8 = st.columns([1, 2])
with col7:
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", caption="Auriculares Gamer")
with col8:
    st.subheader("4. Auriculares Gamer - 35€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000?text=Hola,quiero+los+Auriculares")

st.write("---")
st.info("📦 Envíos rápidos y pago seguro.")
