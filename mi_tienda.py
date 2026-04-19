import streamlit as st

# 1. Configuración de datos de productos
# Asegúrate de que las URLs de las imágenes sean enlaces directos (que terminen en .jpg, .png, etc.)
productos = [
    {
        "nombre": "Producto 1",
        "precio": 25.99,
        "imagen": "https://via.placeholder.com/300", # Sustituir por URL real
        "descripcion": "Descripción breve del producto 1."
    },
    {
        "nombre": "Producto 2",
        "precio": 40.00,
        "imagen": "https://via.placeholder.com/300",
        "descripcion": "Descripción breve del producto 2."
    },
    {
        "nombre": "Producto 3",
        "precio": 15.50,
        "imagen": "https://via.placeholder.com/300",
        "descripcion": "Descripción breve del producto 3."
    },
    {
        "nombre": "Producto 4",
        "precio": 60.00,
        "imagen": "https://via.placeholder.com/300",
        "descripcion": "Descripción breve del producto 4."
    }
]

st.title("🛍️ Mi Tienda Ophay")
st.markdown("---")

# 2. Creación de la cuadrícula (2 columnas por fila para que se vea bien en móvil y PC)
cols = st.columns(2)

for i, producto in enumerate(productos):
    # Usamos el operador módulo % para alternar entre la columna 0 y 1
    col = cols[i % 2]
    
    with col:
        st.subheader(producto["nombre"])
        
        # Intentamos cargar la imagen, si falla ponemos un texto
        try:
            st.image(producto["imagen"], use_container_width=True)
        except:
            st.error("No se pudo cargar la imagen")
            
        st.write(f"**Precio:** {producto['precio']}€")
        st.caption(producto["descripcion"])
        
        if st.button(f"Añadir al carrito", key=f"btn_{i}"):
            st.success(f"¡{producto['nombre']} añadido!")
        
        st.markdown("---")
