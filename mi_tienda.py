import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS CON PRIORIDAD MÁXIMA (FORCE GREEN)
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

/* EL BOTÓN VERDE "INCORROMPIBLE" */
div.stButton > button {
    background-color: transparent !important;
    color: #25D366 !important;
    border: 2px solid #25D366 !important;
    border-radius: 10px !important;
    width: 100% !important;
    height: 50px !important;
    font-family: 'Cinzel' !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
}

div.stButton > button:hover {
    background-color: #25D366 !important;
    color: #000000 !important;
    box-shadow: 0 0 20px rgba(37, 211, 102, 0.6) !important;
    border: 2px solid #25D366 !important;
}

/* HORÓSCOPO */
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
    st.markdown('<h2 class="oro-header">CLARIVIDENCIA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<p class="tiempo">Consulta privada de 30 min</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Lectura profunda de Tarot y Clarividencia. Un espacio sagrado para hallar respuestas.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro-header">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<p class="tiempo">Edición Oro Limitada</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal de alta gama diseñado para canalizar energías superiores.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR MAZO", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro-header">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<p class="tiempo">Gema de Protección</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda de amatista pura. Ideal para transmutar la energía del hogar.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR PIEZA", W)

# 5. HORÓSCOPO
st.markdown("<br><br><hr><br>", unsafe_allow_html=True)
st.markdown('<h2 class="oro-header" style="font-size:2.5rem;">HORÓSCOPO SEMANAL</h2>', unsafe_allow_html=True)

signos = [
    ("♈ ARIES","Fuego."),("♌ LEO","Brillo."),("♐ SAGITARIO","Fortuna."),
    (" Taurus TAURO","Éxito."),(" Virgo VIRGO","Orden."),(" Capricorn CAPRICORNIO","Rigor."),
    (" Gemini GÉMINIS","Palabra."),(" Libra LIBRA","Paz."),(" Aquarius ACUARIO","Visión."),
    (" Cancer CÁNCER","Lunar."),(" Scorpio ESCORPIO","Poder."),(" Pisces PISCIS","Unión.")
]

hz = st.columns(4)
for i, (nombre, clima) in enumerate(signos):
    with hz[i % 4]:
        st.markdown(f'<p class="sig">{nombre}</p>', unsafe_allow_html=True)

st.markdown("<br><br><br><p style='text-align:center;color:#444;font-size:0.7rem;'>© MMXXVI OPHAY BARCELONA</p>", unsafe_allow_html=True)
