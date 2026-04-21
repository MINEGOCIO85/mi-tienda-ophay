import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "FULL VIEW"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');

/* Fondo General */
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }

/* Tipografías */
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 15px; min-height: 100px; margin-bottom: 15px; }

/* BOTONES DE PRODUCTO */
div[data-testid="stLinkButton"] > a {
    background-color: #25D366 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Montserrat' !important;
    font-weight: 700 !important;
    display: flex !important;
    justify-content: center !important;
    text-decoration: none !important;
}

/* BOTÓN FLOTANTE CON MARGEN DE SEGURIDAD */
.float-wa {
    position: fixed;
    bottom: 40px; 
    right: 80px; /* Aumentado de 50 a 80 para evitar el corte */
    background-color: #25d366;
    color: white !important;
    border-radius: 50% !important;
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.9);
    z-index: 9999999; 
    text-decoration: none !important;
}
.float-wa:hover {
    transform: scale(1.1);
    background-color: #128c7e;
}
</style>

<a href="https://wa.me/34684668398" class="float-wa" target="_blank">
    🟢
</a>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem; margin-top: -40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:5px; font-size:0.8rem; margin-bottom: 40px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2,
