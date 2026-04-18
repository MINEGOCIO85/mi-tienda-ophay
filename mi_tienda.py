import streamlit as st
import pandas as pd

# 1. Configuración de la web
st.set_page_config(page_title="Ophay Import Pro", layout="wide")

# 2. Tu lista de productos real (Puedes cambiar los nombres y precios aquí)
data = {
    'Producto': ['Smartwatch Ultra', 'Proyector 4K', 'Dron Explorer', 'Auriculares Gamer'],
    'Categoria': ['Electrónica', 'Hogar', 'Hobbies', 'Electrónica'],
    'Costo_Ophay': [20.00, 80.00, 120.00, 15.00],
    'Precio_Venta': [45.00, 150.00, 250.00, 35.00],
    'Imagen': [
        'https://images.unsplash.com/photo-1544117518-2b47c874382d?w=300',
        'https://images.unsplash.com/photo-1535016120720-40c646bebbbb?w=300',
        'https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?w=300',
        'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=300'
    ]
}
df = pd.DataFrame(data)
df['Beneficio'] = df['Precio_Venta'] - df['Costo_Ophay']

# 3. Diseño de la página
st.title("📦 Mi Catálogo de Importación Ophay")
st.sidebar.header("Filtros de Venta")
cat_seleccionada = st.sidebar.multiselect("Categoría", df['Categoria'].unique(), default=df['Categoria'].unique())

# Mostrar productos
cols = st.columns(2)
for index, row in df[df['Categoria'].isin(cat_seleccionada)].iterrows():
    with cols[index % 2]:
        st.image(row['Imagen'])
        st.header(f"{row['Producto']}")
        st.write(f"Precio: **{row['Precio_Venta']}€** | Beneficio: **{row['Beneficio']}€**")
        
        # Botón de WhatsApp (Pon tu número donde están los ceros)
        link_ws = f"https://wa.me/34600000000?text=Hola, quiero el {row['Producto']}"
        st.markdown(f'[💬 Pedir por WhatsApp]({link_ws})')