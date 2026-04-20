import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", layout="wide")

# ESTILO MEJORADO: BOTONES DE LUJO CON ICONO
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    
    /* Títulos y Precios */
    h1, h3, .precio-oro { 
        color: #d4af37 !important; 
        text-align: center; 
        font-family: 'serif'; 
    }
    
    .descripcion-texto {
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 20px;
        min-height: 50px;
    }

    /* BOTÓN PERSONALIZADO */
    .stButton>button {
        background: linear-gradient(145deg, #d4af37, #b8962e) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 30px !important; /* Más redondeado, más elegante */
        border: 1px solid #aa8a24 !important;
        width: 100%;
        height: 55px;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3); /* Sombra dorada */
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px); /* El botón sube un poco al tocarlo */
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
        background: #ffffff !important;
    }

    p { text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("# 🌙 OPHAY TAROT")
st.markdown("<p style='color: #d4af37;'>Clarividencia & Boutique Esotérica</p>", unsafe_allow_html=True)
st.markdown("---")

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

col1, col2, col3 = st.columns(3)

# PRODUCTO 1
with col1:
    st.image(f"{base_url}/primera%20foto%20isoterica.png")
    st.markdown("### ORÁCULO DEL DESTINO")
    st.markdown("<h2 class='precio-oro'>25 €</h2>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>Lectura profunda para despejar dudas.</div>", unsafe_allow_html=True)
    # Añadimos un emoji de mensaje para que se vea más como contacto
    st.link_button("💬 CONTACTAR", "https://wa.me/34684668398")

# PRODUCTO 2
with col2:
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown("### MAZO RIDER LUXE")
    st.markdown("<h2 class='precio-oro'>45 €</h2>", unsafe_allow_html=True)
    st.markdown("<div class='descripcion-texto'>Mazo premium con acabados de arte.</div>", unsafe_allow_html=True)
    st.link_button("🛍️ COMPRAR AHORA", "https://wa.me/34684668398")

# PRODUCTO 3
with
