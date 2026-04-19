import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury", page_icon="✨")

# 2. ESTILO: FONDO PLATA + TÍTULO ORO + TEXTOS EN ESPAÑOL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,700;1,300&family=Playfair+Display:wght@700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    /* Título ORO de vuelta */
    .title-gold {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        font-size: 55px !important;
        margin-bottom: 0px;
    }

    /* Subtítulo elegante */
    .subtitle-ophay {
        font-family: 'Montserrat', sans-serif;
        color: #64748b;
        text-align: center;
        font-size: 16px;
        margin-top: -10px;
        padding-bottom: 20px;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #0f172a !important; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .desc {
        font-family: 'Montserrat', sans-serif !important;
        color: #475569 !important;
        font-size: 14px !important;
        font-style: italic;
        line-height: 1.5;
    }

    .precio {
        font-family: 'Montserrat', sans-serif !important;
        color: #B38728 !important; /* Precio en Oro */
        font-weight: 700;
        font-size: 22px;
    }
    
    /* Botón verde con los muñequitos 👥 */
    div.stButton > button {
        background: linear-gradient(to right, #25D366, #128C7E) !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
        border-radius: 10px;
        border: none;
        padding: 12px;
        width: 100%;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background: #00AEEF !important; /* Azul MSN al tocarlo */
        transform: scale(1.02);
    }

    /* Animación para que el producto flote al pasar el ratón */
    [data-testid="stHorizontalBlock"]:hover {
        transform: translateY(-5px);
        transition: all 0.3s ease-in-out;
    }

    img {
        border-radius: 10px;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# CABECERA
st.markdown('<p class="title-gold">OPHAY SILVER</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-ophay">Descubre la libertad con nuestra colección exclusiva</p>', unsafe_allow_html=True)
st.write("---")

# Función para los productos
def item(id_prod, img, nombre, precio, texto, link):
    c1, c2 = st.columns([1.2, 2])
    with c1:
        st.image(img)
    with c2:
        st.subheader(f"{id_prod}. {nombre}")
        st.markdown(f'<p class="desc">{texto}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="precio">{precio}€</p>', unsafe_allow_html=True)
        st.link_button(f"👥 PEDIR POR WHATSAPP", link)
    st.write("---")

# LISTA DE PRODUCTOS EN ESPAÑOL
item("1", 
     "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400", 
     "Dron Explorer", 
     "250", 
     "Experimenta la libertad absoluta con este dron cinematográfico, diseñado para capturas aéreas espectaculares.", 
     "https://wa.me/34600000000?text=Hola,quiero+el+Dron")

item("2", 
     "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", 
     "Smartwatch Ultra", 
     "45", 
     "Mantente conectado y controla tu actividad física con elegancia y resistencia en tu muñeca.", 
     "https://wa.me/34600000000?text=Hola,quiero+el+Smartwatch")

item("3", 
     "https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400", 
     "Proyector 4K", 
     "150", 
     "Transforma tu hogar en una sala de cine premium con la mejor resolución y nitidez del mercado.", 
     "https://wa.me/34600000000?text=Hola,quiero+el+Proyector")

item("4", 
     "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", 
     "Auriculares Gamer", 
     "35", 
     "Calidad acústica pura y confort profesional diseñados para las sesiones de juego más exigentes.", 
     "https://wa.me/34600000000?text=Hola,quiero+los+Auriculares")

st.markdown("<center>👥 <b style='color:#64748b;'>Estado: Conectado</b> 🟢</center>", unsafe_allow_html=True)
