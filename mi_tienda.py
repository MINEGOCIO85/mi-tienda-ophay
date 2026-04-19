import streamlit as st

# 1. Configuración
st.set_page_config(page_title="Ophay Silver Edition", page_icon="🥈")

# 2. ESTILO: FONDO PLATA + ANIMACIONES + BOTÓN VERDE
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f5;
    }
    
    .title-ophay {
        font-family: 'Helvetica Neue', sans-serif;
        color: #000000;
        text-align: center;
        font-weight: 200;
        font-size: 45px !important;
        letter-spacing: 2px;
    }

    /* ANIMACIÓN DE LOS PRODUCTOS (Efecto MSN) */
    [data-testid="stVerticalBlock"] > div:hover {
        transform: translateY(-5px);
        transition: all 0.3s ease-in-out;
    }

    h3 {
        font-family: 'Helvetica Neue', sans-serif !important;
        color: #000000 !important;
        font-weight: 700 !important;
    }
    
    /* BOTÓN VERDE WHATSAPP ESTILO MSN */
    div.stButton > button {
        background: linear-gradient(to right, #25D366, #128C7E) !important;
        color: white !important;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        width: 100%;
        height: 45px;
    }
    
    div.stButton > button:hover {
        background: #00AEEF !important; /* Azul MSN al tocarlo */
        transform: scale(1.02);
    }

    img {
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# CABECERA
st.markdown('<p class="title-ophay">OPHAY SILVER</p>', unsafe_allow_html=True)
st.write("---")

# Función para no repetir código
def producto(id, img, nombre, precio, desc, link):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(img)
    with col2:
        st.subheader(f"{id}. {nombre} - {precio}€")
        st.write(desc)
        st.link_button(f"👥 PEDIR POR WHATSAPP", link)
    st.write("---")

# --- LISTA DE LOS 4 PRODUCTOS ---

producto(
    "1", 
    "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400",
    "Dron Explorer", 
    "250", 
    "Experience freedom with this cinematic drone, perfect for aerial shots.", 
    "https://wa.me/34600000000?text=Quiero+el+Dron"
)

producto(
    "2", 
    "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
    "Smartwatch Ultra", 
    "45", 
    "Stay connected and track your fitness with elegance.", 
    "https://wa.me/34600000000?text=Quiero+el+Smartwatch"
)

producto(
    "3", 
    "https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400",
    "Proyector 4K", 
    "150", 
    "Transform your home into a premium cinema experience.", 
    "https://wa.me/34600000000?text=Quiero+el+Proyector"
)

producto(
    "4", 
    "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
    "Auriculares Gamer", 
    "35", 
    "Pure acoustic quality designed for the most demanding sessions.", 
    "https://wa.me/34600000000?text=Quiero+los+Auriculares"
)

st.markdown("<center>👥 <b>Estado: Conectado</b></center>", unsafe_allow_html=True)
