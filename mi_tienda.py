import streamlit as st

st.set_page_config(page_title="Catálogo Ophay", layout="centered")

st.title("🚀 MI NUEVA TIENDA OPHAY")
st.write("Haz clic en el botón de cada producto para pedirlo por WhatsApp.")

# PRODUCTO 1
st.header("1. Smartwatch Ultra - 45€")
st.image("https://m.media-amazon.com/images/I/718Vv7H96PL._AC_SL1500_.jpg", width=300)
st.link_button("💬 Pedir Smartwatch", "https://wa.me/34600000000")
st.write("---")

# PRODUCTO 2
st.header("2. Proyector 4K - 150€")
st.image("https://m.media-amazon.com/images/I/61y49CjPq9L._AC_SL1500_.jpg", width=300)
st.link_button("💬 Pedir Proyector", "https://wa.me/34600000000")
st.write("---")

# PRODUCTO 3
st.header("3. Dron Explorer - 250€")
st.image("https://m.media-amazon.com/images/I/61S-Yf2oFzL._AC_SL1200_.jpg", width=300)
st.link_button("💬 Pedir Dron", "https://wa.me/34600000000")
st.write("---")

# PRODUCTO 4
st.header("4. Auriculares Gamer - 35€")
st.image("https://m.media-amazon.com/images/I/61CGHv6kmWL._AC_SL1500_.jpg", width=300)
st.link_button("💬 Pedir Auriculares", "https://wa.me/34600000000")
