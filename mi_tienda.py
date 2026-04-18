import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Catálogo Ophay", layout="wide")

# Estilo visual mejorado
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div.stButton > button {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 10px;
        border: none;
        height: 50px;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }
    .producto-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📦 Catálogo Ophay Import")
st.write("Haz clic en el botón verde para pedir por WhatsApp")

# LISTA DE PRODUCTOS (Aquí es donde cambias las fotos)
productos = [
    {
        "nombre": "Smartwatch Ultra", 
        "precio": "45.00€", 
        "img": "https://cdn.pixabay.com/photo/2017/04/24/13/20/smartwatch-2256434_640.jpg"
    },
    {
        "nombre": "Proyector 4K", 
        "precio": "150.00€", 
        "img": "https://cdn.pixabay.com/photo/2016/11/29/09/16/architecture-1868667_640.jpg"
    },
    {
        "nombre": "Dron Explorer", 
        "precio": "250.00€", 
        "img": "https://cdn.pixabay.com/photo/2017/09/07/08/54/drone-2724257_640.jpg"
    },
    {
        "nombre": "Auriculares Gamer", 
        "precio": "35.00€", 
        "img": "https://cdn.pixabay.com/photo/2018/09/17/14/25/headphones-3683983_640.jpg"
    }
]

# Mostrar en cuadrícula
cols = st.columns(2)
for i, p in enumerate(productos):
    with cols[i % 2]:
        st.markdown('<div class="producto-card">', unsafe_allow_html=True)
        st.image(p['img'], use_container_width=True)
        st.subheader(p['nombre'])
        st.write(f"💰 Precio: **{p['precio']}**")
        
        # CAMBIA EL NÚMERO AQUÍ (Pon el tuyo donde están los ceros)
        link_ws = f"https://wa.me/34600000000?text=Hola, estoy interesado en el {p['nombre']}"
        st.link_button("💬 Pedir por WhatsApp", link_ws)
        st.markdown('</div>', unsafe_allow_html=True)
