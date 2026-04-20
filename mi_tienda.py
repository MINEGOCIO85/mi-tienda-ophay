import streamlit as st

# 1. Configuración básica
st.set_page_config(page_title="Ophay Tarot", layout="centered")

# 2. Título principal
st.markdown("<h1 style='text-align: center; color: #C5A059;'>🌙 OPHAY TAROT</h1>", unsafe_allow_html=True)
st.write("---")

# 3. Producto 1
col1, col2 = st.columns(2)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2b/Tarot_de_Marseille_conv_1760_-_0_Le_Mat.jpg")
with col2:
    st.subheader("Lectura del Destino")
    st.write("Consulta mística profunda.")
    st.write("**Precio: 25€**")
    st.link_button("Reservar", "https://wa.me/34600000000")

st.write("---")

# 4. Producto 2
col3, col4 = st.columns(2)
with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/db/Tarot_reverso.jpg")
with col4:
    st.subheader("Mazo de Tarot")
    st.write("Edición de lujo.")
    st.write("**Precio: 45€**")
    st.link_button("Comprar", "https://wa.me/34600000000")
