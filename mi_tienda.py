import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO "DARK LUXURY" (Inspirado en boutiques de alta gama)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital@1&display=swap');
    
    .stApp { background-color: #050505; color: #d4d4d4; }
    
    .gold-title {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #cfb53b 0%, #8b7500 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 55px;
        letter-spacing: 12px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .sub-header {
        text-align: center;
        font-family: 'Cinzel', serif;
        color: #555;
        letter-spacing: 5px;
        font-size: 12px;
        margin-bottom: 50px;
    }

    .product-card {
        border-bottom: 1px solid rgba(207, 181, 59, 0.1);
        padding-bottom: 40px;
        margin-bottom: 40px;
    }

    h3 {
        font-family: 'Cinzel', serif !important;
        color: #cfb53b !important;
        letter-spacing: 2px !important;
        font-size: 22px !important;
    }

    .description {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        color: #999;
        line-height: 1.6;
    }

    .price {
        font-family: 'Cinzel', serif;
        color: #cfb53b;
        font-size: 20px;
        margin-top: 15px;
    }

    /* Botón Minimalista de Lujo */
    div.stButton > button {
        background-color: transparent !important;
        color: #cfb53b !important;
        border: 1px solid #cfb53b !important;
        border-radius: 0px !important;
        font-family: 'Cinzel', serif !important;
        letter-spacing: 3px !important;
        padding: 10px 30px !important;
        transition: 0.4s !important;
    }

    div.stButton > button:hover {
        background-color: #cfb53b !important;
        color: #000 !important;
        box-shadow: 0px 0px 15px rgba(207, 181, 59, 0.4);
    }

    img {
        filter: grayscale(30%) contrast(120%) brightness(80%);
        border: 1px solid rgba(207, 181, 59, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="gold-title">OPHAY</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">TAROT & ALQUIMIA</p>', unsafe_allow_html=True)

# 4. FUNCIÓN DE PRODUCTO
def product(img, name, price, desc):
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(img, use_container_width=True)
    with col2:
        st.subheader(name)
        st.markdown(f'<p class="description">{desc}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="price">{price} €</p>', unsafe_allow_html=True)
        st.link_button(f"RESERVAR", "https://wa.me/34600000000")

# 5. PRODUCTOS (Selección de imágenes de alto impacto visual)

# PRODUCTO 1: LECTURA (Mano esotérica y cartas)
product("https://images.unsplash.com/photo-1635352739091-628f80459966?q=80&w=800", 
        "Lectura del Destino", "25", "Una consulta privada para descifrar los mensajes del cosmos y tu linaje espiritual.")

# PRODUCTO 2: MAZO (Terciopelo y oro)
product("https://images.unsplash.com/photo-1606132473187-575796249f3e?q=80&w=800", 
        "Mazo Rider Luxe", "45", "78 cartas con cantos metalizados en oro y acabados de tacto suave para rituales.")

# PRODUCTO 3: AMATISTA (Vibración alta)
product("https://images.unsplash.com/photo-1567883124527-33c1b28d747b?q=80&w=800", 
        "Amatista Sagrada", "15", "Drusa de cristal natural seleccionada por su pureza y capacidad de transmutación energética.")

# PRODUCTO 4: VELA (Ritual oscuro)
product("https://images.unsplash.com/photo-1534073828943-f801091bb18c?q=80&w=800", 
        "Vela de Ritual", "12", "Cera de soja negra ungida con aceites sagrados para la protección y el destierro.")

# 6. FOOTER
st.markdown("<br><br><center><p style='color:#333; font-size:10px; letter-spacing:10px;'>OPHAY • PARIS • MMXXVI</p></center>", unsafe_allow_html=True)
