import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Catálogo Ophay", layout="wide")

# ESTILO PARA PONERLA GUAPA
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div.stButton > button {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 20px;
        border: none;
        height: 45px;
        width: 100%;
        font-weight: bold;
    }
    .img-container {
        border-radius: 15px;
        overflow: hidden;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📦 Mi Catálogo Ophay")
st.write("Selecciona un producto para hacer tu pedido por WhatsApp.")

# Tus productos
productos = [
    {"nombre": "Smartwatch Ultra", "precio": "45.00€", "img": "https://images.unsplash.com/photo-1544117518-2b47c874382d?w=400"},
    {"nombre": "Proyector 4K", "precio": "150.00€", "img": "https://images.unsplash.com/photo-1535016120720-40c646bebbbb?w=400"},
    {"nombre": "Dron Explorer", "precio": "250.00€", "img": "https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?w=400"},
    {"nombre": "Auriculares Gamer", "precio": "35.00€", "img": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=400"}
]

# Mostrar en cuadrícula
cols = st.columns(2)
for i, p in enumerate(productos):
    with cols[i % 2]:
        st.image(p['img'], use_container_width=True)
        st.subheader(p['nombre'])
        st.write(f"💰 Precio: **{p['precio']}**")
        
        # EL BOTÓN DE WHATSAPP (Acuérdate de cambiar el número luego)
        link_ws = f"https://wa.me/34600000000?text=Hola, quiero el {p['nombre']}"
        st.link_button("💬 Pedir por WhatsApp", link_ws)
        st.write("---")
