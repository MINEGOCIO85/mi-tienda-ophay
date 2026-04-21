import streamlit as st

st.set_page_config(page_title="OPHAY", layout="wide")

st.markdown("""
<style>
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }
.oro { color: #f1c40f; text-align: center; font-family: serif; }
.btn-verde { background-color: #25D366; color: white !important; text-align: center; padding: 12px; text-decoration: none; display: block; border-radius: 10px; font-weight: bold; margin: 10px 0; }
.wa-btn { position: fixed; bottom: 30px; right: 5%; background-color: #25d366; color: white !important; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 30px; z-index: 999; text-decoration: none !important; border: 2px solid white; }
</style>
<a href="https://wa.me/34684668398" class="wa-btn" target="_blank">🟢</a>
""", unsafe_allow_html=True)

st.markdown('<h1 class="oro">OPHAY BARCELONA</h1>', unsafe_allow_html=True)

B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

col1, col2, col3 = st.columns(3)
with col1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h3 class="oro">ORÁCULO</h3><p style="color:white;text-align:center;">25€</p><a href="'+W+'" class="btn-verde">RESERVAR</a>', unsafe_allow_html=True)
with col2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h3 class="oro">RIDER LUXE</h3><p style="color:white;text-align:center;">45€</p><a href="'+W+'" class="btn-verde">COMPRAR</a>', unsafe_allow_html=True)
with col3:
    st.image(B + "Amatista.png")
    st.markdown('<h3 class="oro">AMATISTA</h3><p style="color:white;text-align:center;">19,95€</p><a href="'+W+'" class="btn-verde">SOLICITAR</a>', unsafe_allow_html=True)

st.markdown('<br><hr><p style="color:gray;text-align:center;font-size:0.8rem;">© 2026 OPHAY BARCELONA</p>', unsafe_allow_html=True)
