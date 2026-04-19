import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Nostalgia", page_icon="⚡")

# 2. ESTILO: FONDO PLATA + BOTÓN AZUL MESSENGER
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,700;1,300&family=Playfair+Display:wght@700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
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
        color: #0f172a !important; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .desc {
        font-family: 'Montserrat', sans-serif !important;
        color: #64748b !important;
        font-size: 14px !important;
        font-style: italic;
    }

    .precio {
        font-family: 'Montserrat', sans-serif !important;
        color: #1e293b !important;
        font-weight: 700;
        font-size: 20px;
    }
    
    /* BOTÓN AZUL MESSENGER CLÁSICO */
    div.stButton > button {
        background: linear-gradient(135deg, #0084FF 0%, #0078FF 100%) !important; /* El azul de Messenger */
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        width: 100%;
        transition: 0.3s;
        box-shadow: 0px 4px 15px rgba(0, 132, 255, 0.3);
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #00C6FF 0%, #0072FF 100%) !important; /* Brillo al pasar el ratón */
        transform: translateY(-2px);
        box-shadow: 0px 6px 20px rgba(0, 132, 255, 0.5);
    }

    img {
        border-radius: 10px;
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
        # El rayo de Messenger ⚡
        st.link_button(f"⚡ ADQUIRIR POR MESSENGER", link)
    st.write("---")

# LISTA DE PRODUCTOS (He puesto el link a WhatsApp pero con el estilo visual de Messenger)
item("https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400", 
     "Dron Explorer", "Libertad absoluta en el aire con captura cinematográfica.", "250", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", 
     "Smartwatch Ultra", "Diseño vanguardista y control total de tu bienestar.", "45", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400", 
     "Proyector 4K", "Transforma tu hogar en una experiencia visual inmersiva.", "150", "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", 
     "Auriculares Gamer", "Pureza acústica y confort premium profesional.", "35", "https://wa.me/34600000000")

st.caption("OPHAY LUXURY © 2026")
