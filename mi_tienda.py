import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Messenger Edition", page_icon="👥")

# 2. ESTILO: FONDO PLATA + BOTÓN RETRO MSN MESSENGER
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,700;1,300&family=Playfair+Display:wght@700&display=swap');

    /* Fondo Plata Brillante estilo interfaz clásica */
    .stApp {
        background: linear-gradient(135deg, #eef2f7 0%, #d1d9e6 100%);
    }
    
    h1 {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        font-size: 55px !important;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #2c3e50 !important; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .desc {
        font-family: 'Montserrat', sans-serif !important;
        color: #5d6d7e !important;
        font-size: 14px !important;
        font-style: italic;
    }

    .precio {
        font-family: 'Montserrat', sans-serif !important;
        color: #2c3e50 !important;
        font-weight: 700;
        font-size: 20px;
    }
    
    /* BOTÓN RETRO MSN (Azul y Verde) */
    div.stButton > button {
        background: white !important;
        color: #2c3e50 !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
        border-radius: 50px; /* Muy redondeado como las burbujas de antes */
        border: 2px solid #3498db !important; /* Borde azul Messenger */
        padding: 10px 20px;
        width: 100%;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background: #3498db !important; /* Se vuelve azul al pasar */
        color: white !important;
        border-color: #2ecc71 !important; /* Y el borde verde */
        transform: scale(1.03);
    }

    img {
        border-radius: 15px;
        border: 3px solid white;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
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
        # El icono de los muñequitos 👥
        st.link_button(f"👥 ADQUIRIR (ABRIR CHAT)", link)
    st.write("---")

# LISTA DE PRODUCTOS
item("https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400", 
     "Dron Explorer", "Tecnología de vanguardia para capturas aéreas.", "250", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", 
     "Smartwatch Ultra", "Control y elegancia en tu muñeca.", "45", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400", 
     "Proyector 4K", "Cine premium en la comodidad de tu hogar.", "150", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", 
     "Auriculares Gamer", "Inmersión total y sonido de alta fidelidad.", "35", "https://wa.me/34600000000")

st.caption("OPHAY LUXURY • ESTADO: DISPONIBLE 🟢")
