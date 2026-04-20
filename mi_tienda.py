import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", layout="wide")

# ESTILO DE LUJO REFINADO
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    .stButton>button {
        background-color: #d4af37;
        color: #000000;
        font-weight: bold;
        border-radius: 5px;
        border: 1px solid #d4af37;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #ffffff; border: 1px solid #ffffff; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'serif'; text-align: center; }
    p { text-align: center; font-size: 1.1rem; }
    .footer { text-align: center; color: #555555; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# Título con clase
st.markdown("# 🌙 OPHAY TAROT")
st.markdown("### *Alta Clarividencia & Boutique Esotérica*")
st.markdown("---")

# Función para los productos
def item(img_url, nombre, precio, descripcion, boton_texto, telefono):
    st.image(img_url, width=300)
    st.markdown(f"### {nombre}")
    st.markdown(f"**Inversión: {precio} €**")
    st.write(descripcion)
    url_wa = f"https://wa.me/{telefono}"
    st.link_button(boton_texto, url_wa)

# Organización en columnas
col1, col2, col3 = st.columns(3)

# USAREMOS TUS FOTOS (Asegúrate de que los nombres coincidan con los que subiste a GitHub)
url_fotos = "https://raw.githubusercontent.com/tu_usuario/tu_repo/main" # Esto se ajustará solo si las fotos están en la misma carpeta

with col1:
    item("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/primera%20foto%20isoterica.png", 
         "ORÁCULO DEL DESTINO", "25", "Lectura profunda de clarividencia evolutiva.", "RESERVAR SESIÓN", "34684668398")

with col2:
    item("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/FOTOMAZO.png", 
         "MAZO RIDER LUXE", "45", "Edición premium con detalles artísticos en oro.", "LO QUIERO", "34684668398")

with col3:
    item("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/fotoamatista.png", 
         "AMATISTA SAGRADA", "15", "Cristal purificado para transmutación energética.", "COMPRAR", "34684668398")

st.markdown("---")
st.markdown("<p class='footer'>OPHAY • MMXXVI | El destino no se espera, se construye.</p>", unsafe_allow_html=True)
