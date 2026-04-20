import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO LUJO OSCURO
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
        margin-bottom: 0px;
    }

    .sub-header {
        text-align: center;
        font-family: 'Cinzel', serif;
        color: #555;
        letter-spacing: 5px;
        font-size: 10px;
        margin-bottom: 50px;
    }

    h3 { font-family: 'Cinzel', serif !important; color: #cfb53b !important; font-size: 22px !important; }
    
    .price { font-family: 'Cinzel', serif; color: #cfb53b; font-size: 20px; }

    div.stButton > button {
        background-color: transparent !important;
        color: #cfb53b !important;
        border: 1px solid #cfb53b !important;
        border-radius: 0px !important;
        width: 100%;
        padding: 10px !important;
    }

    div.stButton > button:hover {
        background-color: #cfb53b !important;
        color: #000 !important;
    }

    img {
        border-radius: 2px;
        border: 1px solid rgba(207, 181, 59, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="gold-title">OPHAY</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">TAROT & ALQUIMIA</p>', unsafe_allow_html=True)

# 4. FUNCIÓN
def item(img, name, price, desc):
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.image(img, use_container_width=True)
    with c2:
        st.subheader(name)
        st.markdown(f'<p style="font-style:italic; color:#888;">{desc}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="price">{price} €</p>', unsafe_allow_html=True)
        st.link_button(f"SOLICITAR", "https://wa.me/34600000000")
    st.markdown("<hr style='border:0.5px solid rgba(207,181,59,0.1)'>", unsafe_allow_html=True)

# 5. PRODUCTOS (FOTOS ESOTÉRICAS REALES COMPROBADAS)

# 1. Lectura de Tarot (Mano con cartas)
item("https://images.pexels.com/photos/7520773/pexels-photo-7520773.jpeg?auto=compress&w=800", 
     "Lectura del Destino", "25", "Consulta profunda con los arcanos para guiar tu camino.")

# 2. Mazo de Cartas (Estética mística)
item("https://images.pexels.com/photos/7524031/pexels-photo-7524031.jpeg?auto=compress&w=800", 
     "Mazo Rider Luxe", "45", "78 cartas premium con acabados artesanales.")

# 3. Amatista (Cristal real)
item("https://images.pexels.com/photos/4057082/pexels-photo-4057082.jpeg?auto=compress&w=800", 
     "Amatista Sagrada", "15", "Piedra natural de alta vibración energética.")

# 4. Vela Ritual (Fuego y oscuridad)
item("https://images.pexels.com/photos/6732997/pexels-photo-6732997.jpeg?auto=compress&w=800", 
     "Vela de Ritual", "12", "Cera ungida para rituales de claridad y protección.")

# 6. FOOTER
st.markdown("<center><p style='color:#333; font-size:9px; letter-spacing:10px;'>OPHAY • PARIS</p></center>", unsafe_allow_html=True)
