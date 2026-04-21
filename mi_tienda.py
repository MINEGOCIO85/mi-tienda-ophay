import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "FUERZA BRUTA" PARA VERDE WHATSAPP
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');

.main,[data-testid="stAppViewContainer"]{ background-color: #050505; }

/* TÍTULOS */
.oro-header { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.sub-header { font-family: 'Montserrat'; color: #bdc3c7; text-align: center; font-size: 0.8rem; letter-spacing: 8px; text-transform: uppercase; margin-bottom: 50px; }

/* PRODUCTOS */
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2.2rem; font-weight: 700; text-align: center; margin: 0; }
.tiempo { font-family: 'Montserrat'; color: #888; font-size: 0.75rem; text-align: center; margin-bottom: 15px; }
.desc { color: #ffffff; font-family: 'Montserrat'; font-size: 0.95rem; text-align: center; line-height: 1.7; background: rgba(255,255,255,0.03); padding: 25px; border-radius: 15px; border: 1px solid rgba(241,196,15,0.1); min-height: 140px; margin-bottom: 20px; }

/* ESTE ES EL SELECTOR ESPECÍFICO PARA LINK_BUTTON */
a[data-testid="stLinkButton"] {
    border: 2px solid #25D366 !important;
    color: #25D366 !important;
    background-color: transparent !important;
    text-decoration: none !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    height: 50px !important;
    border-radius: 10px !important;
    font-family: 'Cinzel' !important;
    font-weight: 700 !important;
    transition: all 0.3s ease !important;
}

a[data-testid="stLinkButton"]:hover {
    background-color: #25D366 !important;
    color: #000000 !important;
    box-shadow: 0 0 20px rgba(37, 211, 102, 0.6) !important;
}

.sig { font-family: 'Cinzel'; color: #f1c40f; font-weight: 700; text-align: center; font-size: 1.2rem; margin-top: 20px; }
hr { border-color: rgba(241, 196, 15, 0.2) !important; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro-header" style="font-size:4.5rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Barcelona • Private Boutique</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro-header">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<p class="tiempo">Sesión de 30 minutos</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro-header">RIDER LUXE</h2>', unsafe_allow_html=True
