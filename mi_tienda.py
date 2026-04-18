import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Catálogo Ophay", layout="wide")

# Estilo visual pro
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div.stButton > button {
        background-color: #25D366 !important;
        color: white !important;
        border-radius: 12px;
        border: none;
        height: 50px;
        width: 100%;
        font-weight: bold;
    }
    .producto-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📦 Catálogo Ophay Import")
st.write("Selecciona lo que te guste y dale al botón de WhatsApp")

# PRODUCTOS CON FOTOS ESTABLES
productos = [
    {"n": "Smartwatch Ultra", "p": "45€", "img": "https://images.unsplash.com/photo-1544117518-2b47c874382d?w=500"},
    {"n": "Proyector 4K", "p": "150€", "img": "https://images.unsplash.com/photo-1535016120720-40c646bebbbb?w=500"},
    {"n": "Dron Explorer", "p": "250€", "img": "https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?w=500"},
    {"n": "Auriculares Gamer", "p": "35€", "img": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500"}
]

cols = st.columns(2)
for i, p in enumerate(productos):
    with cols[i % 2]:
        st.markdown('<div class="producto-card">', unsafe_allow_html=True)
        st.image(p['img'], use_container_width=True)
        st.subheader(p['n'])
        st.write(f"### {p['p']}")
        # CAMBIA EL 34600000000 POR TU MÓVIL CUANDO QUIERAS
        link = f"https://wa.me/34600000000?text=Hola, quiero el {p['n']}"
        st.link_button("💬 Pedir por WhatsApp", link)
        st.markdown('</div>', unsafe_allow_html=True)
