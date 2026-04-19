import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Catálogo Ophay", layout="wide")

# Título de la tienda
st.title("📦 Catálogo Ophay Import")
st.write("Bienvenido a nuestra tienda. Elige tu producto y contacta por WhatsApp.")

# Lista de productos (revisada)
productos = [
    {"n": "Smartwatch Ultra", "p": "45€", "img": "https://m.media-amazon.com/images/I/718Vv7H96PL._AC_SL1500_.jpg"},
    {"n": "Proyector 4K", "p": "150€", "img": "https://m.media-amazon.com/images/I/61y49CjPq9L._AC_SL1500_.jpg"},
    {"n": "Dron Explorer", "p": "250€", "img": "https://m.media-amazon.com/images/I/61S-Yf2oFzL._AC_SL1200_.jpg"},
    {"n": "Auriculares Gamer", "p": "35€", "img": "https://m.media-amazon.com/images/I/61CGHv6kmWL._AC_SL1500_.jpg"}
]

# Crear 2 columnas para que se vea ordenado
cols = st.columns(2)

for i, p in enumerate(productos):
    with cols[i % 2]:
        # Mostramos la foto
        st.image(p['img'], caption=p['n'], use_container_width=True)
        # Nombre y precio
        st.subheader(f"{p['n']} - {p['p']}")
        # Botón de WhatsApp
        link = f"https://wa.me/34600000000?text=Hola, quiero el {p['n']}"
        st.link_button(f"💬 Comprar {p['n']}", link)
        st.write("---")
