import streamlit as st

# Configuración básica
st.set_page_config(page_title="Mi Tienda Ophay", layout="wide")

# ESTILO VISUAL (El maquillaje)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button {
        width: 100%;
        background-color: #25D366;
        color: white;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
    }
    .producto-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛍️ Catálogo Exclusivo Ophay")
st.write("---")

# Lista de productos (Nombre, Precio, Foto)
productos = [
    {"nombre": "Smartwatch Ultra", "precio": "45€", "img": "https://images.unsplash.com/photo-1544117518-2b47c874382d?w=400"},
    {"nombre": "Proyector 4K", "precio": "150€", "img": "https://images.unsplash.com/photo-1535016120720-40c646bebbbb?w=400"},
    {"nombre": "Dron Explorer", "precio": "250€", "img": "https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?w=400"},
    {"nombre": "Auriculares Gamer", "precio": "35€", "img": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=400"}
]

# Crear la cuadrícula (2 columnas)
cols = st.columns(2)

for i, p in enumerate(productos):
    with cols[i % 2]:
        # Contenedor del producto
        st.markdown(f'<div class="producto-card">', unsafe_allow_html=True)
        st.image(p['img'], use_container_width=True)
        st.subheader(p['nombre'])
        st.write(f"### {p['precio']}")
        
        # Botón de WhatsApp
        link = f"https://wa.me/34600000000?text=Hola, quiero el {p['nombre']}"
        st.link_button("💬 Pedir por WhatsApp", link)
        st.markdown('</div>', unsafe_allow_html=True)
