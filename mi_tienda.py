import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Ophay Import Pro", layout="wide")

# Estilo para que se vea PROFESIONAL
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .product-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .stMarkdown a {
        background-color: #25D366;
        color: white !important;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📦 Catálogo Ophay Import")
st.write("Bienvenido a tu tienda profesional.")

# Tus productos
data = {
    'Producto': ['Smartwatch Ultra', 'Proyector 4K', 'Dron Explorer', 'Auriculares Gamer'],
    'Precio': ['45.00€', '150.00€', '250.00€', '35.00€'],
    'Imagen': [
        'https://images.unsplash.com/photo-1544117518-2b47c874382d?w=400',
        'https://images.unsplash.com/photo-1535016120720-40c646bebbbb?w=400',
        'https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?w=400',
        'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=400'
    ]
}
df = pd.DataFrame(data)

# Mostrar en 2 columnas
cols = st.columns(2)
for i, row in df.iterrows():
    with cols[i % 2]:
        st.markdown('<div class="product-box">', unsafe_allow_html=True)
        st.image(row['Imagen'], use_container_width=True)
        st.subheader(row['Producto'])
        st.write(f"Precio: **{row['Precio']}**")
        
        # EL BOTÓN DE WHATSAPP
        link_ws = f"https://wa.me/34600000000?text=Hola, quiero el {row['Producto']}"
        st.markdown(f'[💬 Pedir por WhatsApp]({link_ws})')
        st.markdown('</div>', unsafe_allow_html=True)
