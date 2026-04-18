import streamlit as st

st.set_page_config(page_title="Catálogo Ophay", layout="wide")

st.markdown("""
    <style>
    .producto-card {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1); margin-bottom: 25px; text-align: center;
    }
    div.stButton > button {
        background-color: #25D366 !important; color: white !important;
        border-radius: 10px; font-weight: bold; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📦 Catálogo Ophay Import")

productos = [
    {"n": "Smartwatch Ultra", "p": "45€", "img": "https://m.media-amazon.com/images/I/718Vv7H96PL._AC_SL1500_.jpg"},
    {"n": "Proyector 4K", "p": "150€", "img": "https://m.media-amazon.com/images/I/61y49CjPq9L._AC_SL1500_.jpg"},
    {"n": "Dron Explorer", "p": "250€", "img": "https://m.media-amazon.com/images/I/61S-Yf2oFzL._AC_SL1200_.jpg"},
    {"n": "Auriculares Gamer", "p": "35€", "img": "https://m.media-amazon.com/images/I/61CGHv6kmWL._AC_SL1500_.jpg"}
]

cols = st.columns(2)
for i, p in enumerate(productos):
    with cols[i % 2]:
        st.markdown('<div class="producto-card">', unsafe_allow_html=True)
        st.image(p['img'], use_container_width=True)
        st.subheader(p['n'])
        st.write(f"### {p['p']}")
        link = f"https://wa.me/34600000000?text=Hola, quiero el {p['n']}"
        st.link_button("💬 Pedir por WhatsApp", link)
        st.markdown('</div>', unsafe_allow_html=True)
