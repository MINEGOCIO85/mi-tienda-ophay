import streamlit as st
import pandas as pd

# 1. Configuración de la web (Título en la pestaña del navegador)
st.set_page_config(page_title="Ophay Import Pro", layout="wide")

# Estilo para que los botones de WhatsApp sean verdes, grandes y bonitos
st.markdown("""
    <style>
    .stMarkdown a {
        background-color: #25D366;
        color: white !important;
        padding: 12px 24px;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
        display: inline-block;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .stMarkdown a:hover {
        background-color: #128C7E;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Tu inventario (Aquí es donde cambiarás nombres, precios y fotos después)
data = {
    'Producto': ['Smartwatch Ultra', 'Proyector 4K', 'Dron Explorer', 'Auriculares Gamer'],
    'Categoria': ['Electrónica', 'Hogar', 'Hobbies', 'Electrónica'],
    'Costo_Ophay': [20.00, 80.00, 120.00, 15.00],
    'Precio_Venta': [45.00, 150.00, 250.00, 35.00],
    'Imagen': [
        'https://images.unsplash.com/photo-1544117518-2b47c874382d?w=500',
        'https://images.unsplash.com/photo-1535016120720-40c646bebbbb?w=500',
        'https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?w=500',
        'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500'
    ]
}

# Creamos la tabla de datos
df = pd.DataFrame(data)
df['Beneficio'] = df['Precio_Venta'] - df['Costo_Ophay']

# 3. Diseño de la página principal
st.title("📦 Mi Catálogo de Importación Ophay")
st.write("Selecciona lo que más te guste y contacta conmigo directamente.")

# Menú lateral para filtrar por categoría
st.sidebar.header("Menú de Navegación")
cat_seleccionada = st.sidebar.multiselect(
    "Filtrar por tipo de producto:", 
    df['Categoria'].unique(), 
    default=df['Categoria'].unique()
)

# Mostramos los productos en 2 columnas (ideal para móvil)
cols = st.columns(2)
productos_finales = df[df['Categoria'].isin(cat_seleccionada)].reset_index()

for index, row in productos_finales.iterrows():
    with cols[index % 2]:
        # Ponemos la foto
        st.image(row['Imagen'], use_container_width=True)
        # Nombre y precio
        st.subheader(row['Producto'])
        st.write(f"💰 Precio final: **{row['Precio_Venta']}€**")
        
        # Esto solo lo ves tú: tu ganancia
        st.info(f"Tu beneficio en esta venta: {row['Beneficio']}€")
        
        # El botón mágico de WhatsApp (RECUERDA PONER TU NÚMERO ABAJO)
        # Cambia el 34600000000 por tu número real
        numero_tel = "34600000000" 
        link_ws = f"https://wa.me/{numero_tel}?text=Hola! Estoy interesado en el {row['Producto']} por {row['Precio_Venta']}€"
        
        st.markdown(f'[💬 Pedir por WhatsApp]({link_ws})')
        st.write("---") # Una raya para separar productos

# Mensaje al final del menú lateral
st.sidebar.write("---")
st.sidebar.success("✅ Stock disponible para envío inmediato")
