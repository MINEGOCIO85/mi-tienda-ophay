import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "BLINDADO" (TODO EN UNO)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505; }
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 15px; min-height: 100px; margin-bottom: 15px; }

/* BOTÓN VERDE WHATSAPP FORZADO */
a[data-testid="stLinkButton"] {
    border: 2px solid #25D366 !important;
    color: #25D366 !important;
    background-color: transparent !important;
    border-radius: 10px !important;
    font-family: 'Cinzel' !important;
    font-weight: 700 !important;
    display: flex !important;
    justify-content: center !important;
}
a[data-testid="stLinkButton"]:hover {
    background-color: #25D366 !important;
    color: #000 !important;
    box-shadow: 0 0 15px rgba(37,211,102,0.5) !important;
}
hr { border-color: rgba(241, 196, 15, 0.2); }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:8px; font-size:0.8rem;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#888; text-align:center; font-size:0.8rem;">30 MINUTOS</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#888; text-align:center; font-size:0.8rem;">EDICIÓN ORO</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal de alta gama.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#888; text-align:center; font-size:0.8rem;">PURA GEMA</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada de alta pureza.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. HORÓSCOPO
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h2 class="oro">HORÓSCOPO</h2>', unsafe_allow_html=True)

Z = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),("♉ TAURO","Éxito")]
hz = st.columns(4)
for i, (n, t) in enumerate(Z):
    with hz[i]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel;">{n}</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#333;'>© OPHAY BCN</p>", unsafe_allow_html=True)
