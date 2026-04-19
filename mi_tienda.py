import streamlit as st
st.set_page_config(page_title="Catalogo Ophay", layout="centered")

# AQUÍ CAMBIAS EL TÍTULO
st.title("🚀 MI NUEVA TIENDA OPHAY")

productos = [
    {"n": "Smartwatch Ultra", "p": "45€", "img": "https://m.media-amazon.com/images/I/718Vv7H96PL._AC_SL1500_.jpg"},
    {"n": "Proyector 4K", "p": "150€", "img": "https://m.media-amazon.com/images/I/61y49CjPq9L._AC_SL1500_.jpg"},
    {"n": "Dron Explorer", "p": "250€", "img": "https://m.media-amazon.com/images/I/61S-Yf2oFzL._AC_SL1200_.jpg"},
    {"n": "Auriculares Gamer", "p": "35€", "img": "https://m.media-amazon.com/images/I/61CGHv6kmWL._AC_SL1500_.jpg"}
]

for p in productos:
    st.markdown("---")
    st.image(p['img'], width=400)
    st.subheader(f"{p['n']} - {p['p']}")
    st.link_button(f"💬 Pedir {p['n']}", "https://wa.me/34600000000")
