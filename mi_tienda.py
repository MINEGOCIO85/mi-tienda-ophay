import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", layout="wide")

# Estilo CSS para que se vea lujoso (Dorado y Negro)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        background-color: #d4af37;
        color: black;
        font-weight: bold;
        border-radius: 20px;
        border: none;
        width: 100%;
    }
    .product-card {
        background-color: #1a1c23;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #d4af37;
        text-align: center;
        margin-bottom: 20px;
    }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.title("🌙 OPHAY TAROT")
st.subheader("Alta Clarividencia & Boutique Esotérica")

# Función para crear cada producto
def item(img_url, nombre, precio, descripcion, boton_texto, telefono):
    with st.container():
        st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
        st.image(img_url, use_container_width=True)
        st.markdown(f"<h3>{nombre}</h3>", unsafe_allow_html=True)
        st.markdown(f"**Inversión: {precio} €**")
        st.write(descripcion)
        # El botón de WhatsApp directo con tu número
        url_wa = f"https://wa.me/{telefono}"
        st.link_button(boton_texto, url_wa)
        st.markdown('</div>', unsafe_allow_html=True)

# --- CONTENIDO ---
col1, col2, col3 = st.columns(3)

url_base = "https://raw.githubusercontent.com/tu_usuario/tu_repo/main" # Esto es un ejemplo, usa tus fotos

with col1:
    item("https://img.freepik.com/foto-gratis/cartas-tarot-velas-mesa_23-2149444315.jpg", 
         "ORÁCULO DEL DESTINO", "25", 
         "Sesión de clarividencia profunda para desvelar tu futuro.", 
         "RESERVAR MI SESIÓN", "34684668398")

with col2:
    item("https://img.freepik.com/foto-gratis/mazo-cartas-tarot-mesa_23-2149444320.jpg", 
         "MAZO RIDER LUXE", "45", 
         "Edición premium con detalles dorados para iniciados.", 
         "LO QUIERO", "34684668398")

with col3:
    item("https://img.freepik.com/foto-gratis/primer-plano-piedra-amatista_23-2149252327.jpg", 
         "AMATISTA SAGRADA", "15", 
         "Cristal purificado para protección y transmutación.", 
         "COMPRAR", "34684668398")

st.markdown("---")
st.markdown("<p style='text-align: center;'>OPHAY • MMXXVI | El destino no se espera, se construye.</p>", unsafe_allow_html=True)
