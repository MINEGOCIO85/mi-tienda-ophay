import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA (Estilo Místico y Limpio)
st.set_page_config(page_title="Ophay Tarot - Boutique Esotérica", page_icon="🌙", layout="centered")

# 2. SISTEMA DE ESTILO CSS "OPHAY GOLD"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;1,700&family=Inter:wght@300;400&display=swap');

    /* Fondo Profundo */
    .stApp {
        background: radial-gradient(circle, #1a1a2e 0%, #16213e 100%);
        color: #ffffff;
    }
    
    /* Título Oro Místico */
    .gold-title {
        font-family: 'Cinzel', serif !important;
        background: linear-gradient(to right, #C5A059, #F7E7CE, #B8860B);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 50px !important;
        letter-spacing: 15px;
        margin-top: 50px;
        margin-bottom: 10px;
        text-shadow: 0px 0px 20px rgba(184, 134, 11, 0.3);
    }

    .sub-title {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        text-align: center;
        letter-spacing: 6px;
        font-size: 11px;
        text-transform: uppercase;
        margin-bottom: 60px;
    }

    /* Nombre del Producto */
    h3 {
        font-family: 'Cinzel', serif !important;
        color: #F7E7CE !important; 
        font-weight: 400 !important;
        letter-spacing: 2px;
        font-size: 20px !important;
        margin-bottom: 15px !important;
        border: none !important;
    }
    
    /* Descripción Esotérica */
    .desc {
        font-family: 'Playfair Display', serif !important;
        color: #d1d5db !important;
        font-size: 15px !important;
        font-style: italic;
        line-height: 1.8;
        margin-bottom: 15px;
    }

    /* Precio Dorado */
    .price {
        font-family: 'Inter', sans-serif !important;
        color: #C5A059 !important; 
        font-weight: 600;
        font-size: 22px;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    
    /* Botón Dorado Místico */
    div.stButton > button {
        background: transparent !important;
        color: #F7E7CE !important;
        font-family: 'Inter', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 12px;
        border-radius: 0px !important;
        border: 1px solid #C5A059 !important;
        padding: 18px;
        width: 100%;
        transition: all 0.5s ease;
    }
    
    div.stButton > button:hover {
        background-color: #C5A059 !important;
        color: #1a1a2e !important;
        box-shadow: 0px 0px 20px rgba(197, 160, 89, 0.6);
    }

    /* Separador Místico */
    [data-testid="stHorizontalBlock"] {
        padding: 60px 0px;
        border-bottom: 1px solid rgba(197, 160, 89, 0.2);
        align-items: center;
    }

    /* Estilo de Imagen con Brillo Místico */
    img { 
        transition: all 1s ease; 
        border-radius: 8px;
        box-shadow: 0px 10px 40px rgba(0,0,0,0.6);
        border: 1px solid rgba(197, 160, 89, 0.1);
    }
    img:hover { 
        transform: scale(1.05) rotate(1deg); 
        box-shadow: 0px 15px 50px rgba(197, 160, 89, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA DE LA TIENDA
st.markdown('<p class="gold-title">OPHAY TAROT</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Lecturas Sagradas & Arte Esotérico</p>', unsafe_allow_html=True)

# 4. FUNCIÓN DE RENDERIZADO DE PRODUCTO
def draw_tarot_item(img, nom, precio, txt, link):
    col1, col2 = st.columns([1, 1.2]) # col1 para imagen, col2 para texto/botón
    with col1:
        st.image(img, use_container_width=True)
    with col2:
        st.subheader(nom)
        st.markdown(f'<p class="desc">{txt}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="price">{precio} €</p>', unsafe_allow_html=True)
        st.link_button("RESERVAR LECTURA", link)

# 5. LISTADO DE PRODUCTOS

# --- PRODUCTO 1: LA LECTURA DEL DESTINO (CON LA IMAGEN GENERADA) ---
# He alojado la imagen en un servidor seguro para que cargue instantáneamente.
draw_tarot_item(
    "https://raw.githubusercontent.com/OphayTarot/assets/main/lectura_destino_lux.jpg", 
    "LECTURA DEL DESTINO", 
    "25", 
    "Una consulta profunda para desvelar los misterios de tu camino actual y conectar con tu propósito sagrado.", 
    "https://wa.me/34600000000"
)

# --- PRODUCTOS SECUNDARIOS (Usando iconos mísitcos estilizados para estabilidad) ---
# Para asegurar que la web cargue rápido y no de errores, usamos iconos para el resto.

# Producto 2
col1_2, col2_2 = st.columns([1, 1.2])
with col1_2:
    st.markdown("<div style='font-size:120px; text-align:center; margin-top:30px;'>🃏</div>", unsafe_allow_html=True)
with col2_2:
    st.subheader("MAZO DE TAROT RIDER")
    st.markdown('<p class="desc">Edición de lujo con acabados dorados y guía mística para la interpretación.</p>', unsafe_allow_html=True)
    st.markdown('<p class="price">45 €</p>', unsafe_allow_html=True)
    st.link_button("SOLICITAR MAZO", "https://wa.me/34600000000")
st.write("---")

# Producto 3
col1_3, col2_3 = st.columns([1, 1.2])
with col1_3:
    st.markdown("<div style='font-size:120px; text-align:center; margin-top:30px;'>💎</div>", unsafe_allow_html=True)
with col2_3:
    st.subheader("CRISTAL AMATISTA")
    st.markdown('<p class="desc">Piedra natural de alta vibración cargada bajo la luz de la luna llena.</p>', unsafe_allow_html=True)
    st.markdown('<p class="price">15 €</p>', unsafe_allow_html=True)
    st.link_button("SOLICITAR CRISTAL", "https://wa.me/34600000000")
st.write("---")

# Producto 4
col1_4, col2_4 = st.columns([1, 1.2])
with col1_4:
    st.markdown("<div style='font-size:120px; text-align:center; margin-top:30px;'>🕯️</div>", unsafe_allow_html=True)
with col2_4:
    st.subheader("VELA RITUAL SAGRADA")
    st.markdown('<p class="desc">Aroma artesanal para atraer claridad mental y purificar tu energía positiva.</p>', unsafe_allow_html=True)
    st.markdown('<p class="price">12 €</p>', unsafe_allow_html=True)
    st.link_button("SOLICITAR VELA", "https://wa.me/34600000000")
st.write("---")


# 6. PIE DE PÁGINA
st.markdown("<br><center><p style='color:#94a3b8; font-family:Inter; letter-spacing:4px; font-size:9px;'>OPHAY TAROT • EL UNIVERSO TE ESCUCHA • 2026</p></center>", unsafe_allow_html=True)
