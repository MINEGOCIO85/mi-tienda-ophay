import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Ophay Tarot | Boutique", page_icon="🌙", layout="centered")

# 2. ESTILO "OPHAY NOIR & GOLD"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;1,700&display=swap');
    
    .stApp { background-color: #0f1116; color: #e5e7eb; }
    
    .main-title {
        font-family: 'Cinzel', serif;
        color: #C5A059;
        text-align: center;
        font-size: 55px;
        letter-spacing: 15px;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .gold-line {
        height: 2px;
        background: linear-gradient(to right, transparent, #C5A059, transparent);
        margin: 20px 0 40px 0;
    }

    .product-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 2px;
        border: 1px solid rgba(197, 160, 89, 0.2);
        margin-bottom: 30px;
        transition: 0.3s;
    }
    
    .product-card:hover { border-color: #C5A059; box-shadow: 0 0 15px rgba(197, 160, 89, 0.1); }

    h3 { font-family: 'Cinzel', serif !important; color: #F7E7CE !important; font-size: 24px !important; }
    
    .price-tag { font-family: 'Playfair Display', serif; color: #C5A059; font-size: 22px; font-weight: bold; }
    
    div.stButton > button {
        background-color: transparent !important;
        color: #C5A059 !important;
        border: 1px solid #C5A059 !important;
        border-radius: 0px !important;
        width: 100%;
        letter-spacing: 2px;
        font-family: 'Cinzel', serif;
    }
    
    div.stButton > button:hover { background-color: #C5A059 !important; color: #0f1116 !important; }
    
    img { border-radius: 2px; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="main-title">OPHAY TAROT</h1>', unsafe_allow_html=True)
st.markdown('<div class="gold-line"></div>', unsafe_allow_html=True)

# 4. LISTADO DE PRODUCTOS
def product(img, name, price, desc):
    with st.container():
        col1, col2 = st.columns([1, 1.2])
        with col1:
            st.image(img, use_container_width=True)
        with col2:
            st.subheader(name)
            st.write(f"*{desc}*")
            st.markdown(f'<p class="price-tag">{price}€</p>', unsafe_allow_html=True)
            st.link_button(f"RESERVAR {name}", "https://wa.me/34600000000")
        st.markdown('<div style="margin-bottom: 50px;"></div>', unsafe_allow_html=True)

# PRODUCTOS CON IMÁGENES SELECCIONADAS POR ESTÉTICA Y ESTABILIDAD
product("https://www.worldhistory.org/img/r/p/1000x1200/16601.jpg", 
        "LECTURA SAGRADA", "25", "Una inmersión profunda en tu destino a través de los arcanos mayores.")

product("https://upload.wikimedia.org/wikipedia/commons/3/33/RWS_Tarot_06_Lovers.jpg", 
        "MAZO RIDER LUXE", "45", "Edición artesanal con grabados en pan de oro y estuche de seda.")

product("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Amethyste_2.jpg/800px-Amethyste_2.jpg", 
        "CRISTAL DE PODER", "15", "Amatista de Uruguay cargada bajo el influjo de la luna llena.")

product("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Candle_in_the_dark.jpg/800px-Candle_in_the_dark.jpg", 
        "VELA RITUALIZADA", "12", "Alquimia de aceites esenciales para la purificación del hogar.")

# PIE DE PÁGINA
st.markdown("<br><br><center><p style='color:#5c6b89; font-size:10px; letter-spacing:5px;'>OPHAY • PARIS • 2026</p></center>", unsafe_allow_html=True)
