import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Catálogo Ophay", layout="centered")

# 2. Título principal
st.title("🚀 MI NUEVA TIENDA OPHAY")
st.write("Haz clic en el botón de cada producto para pedirlo por WhatsApp.")
st.write("---")

# PRODUCTO 1
st.subheader("1. Smartwatch Ultra - 45€")
st.image("https://images.unsplash.com/photo-1544117518-2b476eb99404?w=500", width=300)
st.link_button("💬 PEDIR SMARTWATCH", "https://wa.me/34600000000?text=Hola,quiero+el+Smartwatch")
st.write("---")

# PRODUCTO 2
st.subheader("2. Proyector 4K - 150€")
st.image("https://images.unsplash.com/photo-1535016120720-40c646bebbfc?w=500", width=300)
st.link_button("💬 PEDIR PROYECTOR", "https://wa.me/34600000000?text=Hola,quiero+el+Proyector")
st.write("---")

# PRODUCTO 3
st.subheader("3. Dron Explorer - 250€")
st.image("https://images.unsplash.com/photo-1473960104312-d2e11b5362f1?w=500", width=300)
st.link_button("💬 PEDIR DRON", "https://wa.me/34600000000?text=Hola,quiero+el+Dron")
st.write("---")

# PRODUCTO 4
st.subheader("4. Auriculares Gamer - 35€")
st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", width=300)
st.link_button("💬 PEDIR AURICULARES", "https://wa.me/34600000000?text=Hola,quiero+los+Auriculares")
