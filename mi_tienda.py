import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury", page_icon="✨")

# 2. ESTILO: FONDO PLATA + TÍTULO ORO + BOTÓN ULTRA MODERNO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital@1&family=Montserrat:wght@300;600;800&family=Playfair+Display:wght@700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    .title-gold {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        font-size: 55px !important;
        margin-bottom: 5px;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #1e293b !important; 
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 20px !important;
    }
    
    .desc {
        font-family: 'Libre Baskerville', serif !important;
        color: #475569 !important;
        font-size: 15px !important;
        font-style: italic;
        line-height: 1.6;
        margin-bottom: 10px;
    }

    .precio {
        font-family: 'Montserrat', sans-serif !important;
        color: #B38728 !important; 
        font-weight: 800;
        font-size: 24px;
        margin-top: 5px;
    }
    
    /* EL BOTÓN "WAPO" - ESTILO PREMIUM */
    div.stButton > button {
        background: linear-gradient(45deg, #25D366, #075E54, #128C7E) !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 800;
        border-radius: 50px; /* Redondeado moderno */
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
        padding: 15px 30px;
        width: 100%;
        transition: all 0.4s ease;
        box-shadow: 0px 8px 20px rgba(37, 211, 102, 0.4);
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    div.stButton > button:hover {
        background: linear-gradient(45deg, #00AEEF, #0078FF) !important; /* Cambio a Azul MSN */
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0px 12px 25px rgba(0, 174, 239, 0.5);
        border-color: white !important;
    }

    /* Animación sutil de los bloques */
    [data-testid="stHorizontalBlock"] {
        padding: 20px;
        border-radius: 15px;
        transition: background 0.3s ease;
    }

    [data-testid="stHorizontalBlock"]:hover {
        background: rgba(255, 255, 255, 0.4);
    }

    img {
        border-radius: 15px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title-gold">OPHAY SILVER</p>', unsafe_allow_html=True)
st.write("---")

def item(id_prod, img, nombre, precio, texto, link):
    c1, c2 = st.columns([1.2, 2])
    with c1:
        st.image(img)
    with c2:
        st.subheader(f"{id_prod}. {nombre}")
        st.markdown(f'<p class="desc">{texto}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="precio">{precio}€</p>', unsafe_allow_html=True)
        # El letrero renovado
        st.link_button(f"👥 PEDIR POR WHATSAPP ➔", link)
    st.write("---")

# LISTADO DE PRODUCTOS
item("1", "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400", 
     "Dron Explorer", "250", 
     "Domine el horizonte con una perspectiva cinematográfica sin precedentes y estabilidad profesional.", 
     "https://wa.me/34600000000")

item("2", "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", 
     "Smartwatch Ultra", "45", 
     "La perfecta convergencia entre la ingeniería de precisión y el estilo vanguardista para su día a día.", 
     "https://wa.me/34600000000")

item("3", "https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400", 
     "Proyector 4K", "150", 
     "Sumerja sus sentidos en una experiencia visual de gran formato con una pureza de imagen excepcional.", 
     "https://wa.me/34600000000")

item("4", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", 
     "Auriculares Gamer", "35", 
     "Arquitectura sonora diseñada para ofrecer una inmersión absoluta y un confort acústico inigualable.", 
     "https://wa.me/34600000000")

st.markdown("<center>👥 <b style='color:#64748b;'>Estado: Conectado</b> 🟢</center>", unsafe_allow_html=True)
