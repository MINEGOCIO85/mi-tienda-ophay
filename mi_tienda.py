import streamlit as st

# Configuración de página
st.set_page_config(page_title="Ophay Tarot", layout="centered")

# Título Principal
st.title("🌙 OPHAY TAROT")
st.write("---")

# Función simple de producto
def tarot_item(nombre, precio, descripcion, imagen_url):
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.image(imagen_url, use_container_width=True)
    with col2:
        st.subheader(nombre)
        st.write(descripcion)
        st.write(f"**Precio: {precio} €**")
        st.link_button("RESERVAR LECTURA", "https://wa.me/34600000000")
    st.write("---")

# Lista de Productos con enlaces directos verificados
tarot_item(
    "LECTURA DEL DESTINO", 
    "25", 
    "Consulta profunda para desvelar tu camino sagrado.",
    "https://images.unsplash.com/photo-1590424744257-fdb03ed7880d?w=500"
)

tarot_item(
    "MAZO DE TAROT RIDER", 
    "45", 
    "Edición de lujo con acabados dorados.",
    "https://images.unsplash.com/photo-1612178991541-b48cc8e92a4d?w=500"
)

tarot_item(
    "CRISTAL AMATISTA", 
    "15", 
    "Piedra natural cargada bajo la luna llena.",
    "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=500"
)

st.caption("OPHAY TAROT • 2026")
