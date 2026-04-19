import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay MSN Edition", page_icon="👥")

# 2. ESTILO: FONDO PLATA + BOTÓN DUO-COLOR (AZUL Y VERDE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Playfair+Display:wght@700&display=swap');

    /* Fondo Plata suave */
    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%);
    }
    
    h1 {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        font-size: 50px !important;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #243b53 !important; 
        font-weight: 700;
        text-transform: uppercase;
        font-size: 18px !important;
    }
    
    .desc {
        font-family: 'Montserrat', sans-serif !important;
        color: #486581 !important;
        font-size: 14px !important;
        font-style: italic;
    }

    .precio {
        font-family: 'Montserrat', sans-serif !important;
        color: #102a43 !important;
        font-weight: 700;
        font-size: 20px;
    }
    
    /* EL BOTÓN DE LOS MUÑEQUITOS (VERDE Y AZUL) */
    div.stButton > button {
        background: linear-gradient(to right, #00AEEF 0%, #8CC63F 100%) !important; /* Azul y Verde MSN */
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
        border-radius: 25px;
        border: 2px solid white !important;
        padding: 10px 20px;
        width: 100%;
        transition: 0.4s;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 20px #00AEEF, 0px 0px 20px #8CC63F; /* Brillo doble */
        letter-spacing: 2px;
    }

    img {
        border-radius: 12px;
        border: 2px solid #bcccdc;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("OPHAY SILVER")
st.write("---")

# Función para los productos
def item(img, name, text, price, link):
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(img)
    with c2:
        st.subheader(name)
        st.markdown(f'<p class="desc">{text}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="precio">{price}€</p>', unsafe_allow_html=True)
        # Los muñequitos azul y verde en emoji 👥
        st.link_button(f"👥 INICIAR CHAT MSN", link)
    st.write("---")

# LISTA DE PRODUCTOS
item("https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400", 
     "Dron Explorer", "Tecnología de vuelo avanzada para capturas épicas.", "250", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", 
     "Smartwatch Ultra", "Estilo y salud conectados en tu muñeca.", "45", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400", 
     "Proyector 4K", "Tu cine personal con la máxima resolución.", "150", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", 
     "Auriculares Gamer", "Sonido envolvente para una victoria total.", "35", "https://wa.me/34600000000")

st.markdown("<center><p style='color:#486581;'><b>Estado: Conectado</b> 🟢</p></center>", unsafe_allow_html=True)
