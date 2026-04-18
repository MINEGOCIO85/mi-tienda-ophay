import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Import - Catálogo", page_icon="📦", layout="wide")

# Estilo personalizado
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #25D366; color: white; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #128C7E; color: white; }
    .product-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); border: 1px solid #eee; }
    </style>
    """, unsafe_allow_html=True)

st.title("📦 Catálogo de Importación Ophay")
st.subheader("Calidad premium al mejor precio directo")
st.write("---")

# Lista de productos (Nombre, Precio, Imagen, Descripción)
productos = [
    ["Smartwatch Ultra", "45.0€", "https://images.unsplash.com/photo-1544117518-2b04428e34e9?w=500", "Pantalla HD, llamadas y salud."],
    ["Dron Explorer", "250.0€", "https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?w=500", "Cámara 4K y vuelo estable."],
    ["Proyector 4K", "150.0€", "https://images.unsplash.com/photo-1535016120720-40c646bebbbb?w=500", "Cine en casa de gran formato."],
    ["Auriculares Gamer", "35.0€", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", "Sonido envolvente y micro."]
]

# Crear filas y columnas
cols = st.columns(2)

for i, prod in enumerate(productos):
    with cols[i % 2]:
        st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
        st.image(prod[2], use_container_width=True)
        st.subheader(prod[0])
        st.write(f"**Precio:** {prod[1]}")
        st.caption(prod[3])
        
        # Botón de WhatsApp (Cambia el número cuando quieras)
        link_wa = f"https://wa.me/34600000000?text=Hola! Me interesa el {prod[0]}"
        st.link_button(f"💬 Pedir por WhatsApp", link_wa)
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("") 

st.sidebar.title("Contacto")
st.sidebar.write("📍 Importaciones directas")
st.sidebar.write("🚀 Envíos rápidos")
st.sidebar.info("Selecciona tus productos y contacta conmigo por WhatsApp.")
