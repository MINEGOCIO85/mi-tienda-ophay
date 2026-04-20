import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO BOUTIQUE DE LUJO (CSS PURO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300&display=swap');
    
    .stApp { background-color: #0a0a0c; color: #ffffff; }
    
    .header-box {
        text-align: center;
        padding: 50px 0;
        border-bottom: 1px solid #C5A059;
        margin-bottom: 50px;
    }
    
    .gold-title {
        font-family: 'Cinzel', serif;
        color: #C5A059;
        font-size: 50px;
        letter-spacing: 15px;
        margin: 0;
    }
    
    /* Marco místico que sustituye a la foto rota */
    .tarot-frame {
        width: 100%;
        height: 350px;
        border: 2px solid #C5A059;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Cinzel', serif;
        font-size: 80px;
        color: rgba(197, 160, 89, 0.3);
        background: radial-gradient(circle, #1a1a2e 0%, #0a0a0c 100%);
        box-shadow: inset 0 0 50px rgba(197, 160, 89, 0.2);
        margin-bottom: 20px;
    }

    .product-title {
        font-family: 'Cinzel', serif;
        color: #F7E7CE;
        font-size: 24px;
        margin-top: 10px;
    }
    
    .price-tag {
        font-family: 'Inter', sans-serif;
        color: #C5A059;
        font-size: 20px;
        letter-spacing: 2px;
    }

    div.stButton > button {
        background-color: #C5A059 !important;
        color: #0a0a0c !important;
        font-family: 'Cinzel', serif !important;
        border: none !important;
        border-radius: 0px !important;
        width: 100%;
        padding: 15px;
        transition: 0.4s;
    }
    
    div.stButton > button:hover {
        background-color: #F7E7CE !important;
        transform: translateY(-3px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<div class="header-box"><p class="gold-title">OPHAY TAROT</p><p style="letter-spacing:5px; color:#5c6b89;">LECTURAS SAGRADAS</p></div>', unsafe_allow_html=True)

# 4. LISTADO DE PRODUCTOS (4 PRODUCTOS)
def draw_product(simbolo, nombre, precio, desc):
    col1, col2 = st.columns([1, 1])
    with col1:
        # Aquí creamos un "Arte Místico" con el símbolo en lugar de una foto que se rompa
        st.markdown(f'<div class="tarot-frame">{simbolo}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<p class="product-title">{nombre}</p>', unsafe_allow_html=True)
        st.write(f"_{desc}_")
        st.markdown(f'<p class="price-tag">{precio} €</p>', unsafe_allow_html=True)
        st.link_button(f"RESERVAR {nombre}", "https://wa.me/34600000000")
    st.markdown('<br><br>', unsafe_allow_html=True)

# Los 4 productos con símbolos esotéricos elegantes
draw_product("👁", "LECTURA DEL DESTINO", "25", "Una conexión profunda con tu hilo espiritual y propósito de vida.")
draw_product("⚔️", "MAZO RIDER LUXE", "45", "78 cartas con bordes dorados, estuche de seda y guía mística.")
draw_product("✨", "AMATISTA SAGRADA", "15", "Cristal de alta vibración para la transmutación energética.")
draw_product("🔥", "VELA DE RITUAL", "12", "Cera de soja alquímica para iluminar tus meditaciones.")

# PIE DE PÁGINA
st.markdown("<center><p style='color:#5c6b89; font-size:10px; letter-spacing:8px;'>OPHAY • MMXXVI</p></center>", unsafe_allow_html=True)
