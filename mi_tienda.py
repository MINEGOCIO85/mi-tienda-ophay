import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA (Estilo Místico)
st.set_page_config(page_title="Ophay Tarot - Boutique Esotérica", page_icon="🌙", layout="centered")

# 2. SISTEMA DE ESTILO "TAROT MYSTIQUE"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;1,700&family=Inter:wght@300;400&display=swap');

    /* Fondo Azul Noche Profundo */
    .stApp {
        background: radial-gradient(circle, #1a1a2e 0%, #16213e 100%);
        color: #e94560;
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
        margin-bottom: 10px !important;
    }
    
    /* Descripción Esotérica */
    .desc {
        font-family: 'Playfair Display', serif !important;
        color: #d1d5db !important;
        font-size: 15px !important;
        font-style: italic;
        line-height: 1.8;
    }

    /* Precio Dorado */
    .price {
        font-family: 'Inter', sans-serif !important;
        color: #C5A059 !important; 
        font-weight: 600;
        font-size: 22px;
        margin-top: 10px;
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
        padding: 15px;
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
        padding: 50px 0px;
        border-bottom: 1px solid rgba(197, 160, 89, 0.2);
        align-items: center;
    }

    img { 
        transition: all 1s ease; 
        border-radius: 5px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    }
    img:hover { transform: scale(1.05) rotate(1deg); }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="gold-title">OPHAY TAROT</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Lecturas Sagradas & Arte Esotérico</p>', unsafe_allow_html=True)

# 4. FUNCIÓN DE PRODUCTO
def draw_tarot_item(img, nom, precio, txt, link):
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(img, use_container_width=True)
    with col2:
        st.subheader(nom)
        st.markdown(f'<p class="desc">{txt}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="price">{precio} €</p>', unsafe_allow_html=True)
        st.link_button("RESERVAR LECTURA", link)

# 5. LISTADO DE PRODUCTOS MÍSTICOS
draw_tarot_item("https://images.unsplash.com/photo-1572025442646-866d16c84a54?w=700", "LECTURA DEL DESTINO", "25", "Una consulta profunda de 30 minutos para desvelar los misterios de tu camino actual.", "https://wa.me/34600000000")

draw_tarot_item("
