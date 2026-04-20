import streamlit as st

# 1. CONFIGURACIÓN (Debe ser lo primero siempre)
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505; }
.oro { font-family: 'Cinzel'; color: #f1c40f; font-weight: 900; text-align: center; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 1.8rem; font-weight: 700; text-align: center; margin-bottom: 0px; }
.tiempo { font-family: 'Montserrat'; color: #bdc3c7; font-size: 0.8rem; text-align: center; margin-top: 0px; margin-bottom: 10px; font-style: italic; }
.desc { color: #ffffff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; line-height: 1.6; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; min-height: 110px; margin-bottom: 15px; }
.sig { color: #f1c40f; font-family: 'Cinzel'; font-weight: 700; text-align: center; font-size: 1.1rem; }
hr { border-color: rgba(241, 196, 15, 0.3) !important; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. DEFINICIÓN DE COLUMNAS (Esto evita el NameError)
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<p class="tiempo">Sesión de 30 minutos</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia. Un espacio exclusivo para descifrar su destino.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<p class="tiempo">Edición Oro</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo de Tarot artesanal con acabados de lujo para una conexión superior.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<p class="tiempo">Piedra Sagrada</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda de alta pureza seleccionada para la protección de su santuario personal.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. SECCIONES FINALES
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2.5rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

# Lista de signos
Z = [("♈ ARIES","Fuego."),("♌ LEO","Brillo."),("♐ SAGITARIO","Fortuna."),
     ("♉ TAURO","Exito."),("♍ VIRGO","Orden."),("♑ CAPRICORNIO","Rigor."),
     ("♊ GÉMINIS","Palabra."),("♎ LIBRA","Paz."),("♒ ACUARIO","Visión."),
     ("♋ CÁNCER","Lunar."),("♏ ESCORPIO","Poder."),("♓ PISCIS","Unión.")]

hz = st.columns(4)
for i, (n, t) in enumerate(Z):
    with hz[i % 4]:
        st.markdown(f'<p class="sig">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:white;text-align:center;">{t}</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#444;'>© MMXXVI OPHAY BCN</p>", unsafe_allow_html=True)
