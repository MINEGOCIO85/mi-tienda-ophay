import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS (AQUÍ ESTÁ TODO EL DISEÑO)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505; }
.oro { font-family: 'Cinzel'; color: #f1c40f; font-weight: 900; text-align: center; }
.titulo-seccion { font-family: 'Cinzel'; color: #f1c40f; font-size: 2.5rem; text-align: center; margin: 30px 0; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 1.8rem; font-weight: 700; text-align: center; }
.desc { color: #ffffff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; line-height: 1.6; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; min-height: 110px; margin-bottom: 15px; }
.sig { color: #f1c40f; font-family: 'Cinzel'; font-weight: 700; text-align: center; font-size: 1.1rem; margin-top:15px; }
.plata { color: #bdc3c7; font-family: 'Montserrat'; font-size: 0.8rem; text-align: center; font-style: italic; }
hr { border-color: rgba(241, 196, 15, 0.3) !important; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS (LÍNEAS LÓGICAS CORTAS)
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de clarividencia ancestral.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal con acabados en oro.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada de alta pureza.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. HORÓSCOPO
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h2 class="titulo-seccion">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

Z = [("♈ ARIES","Fuego."),("♌ LEO","Brillo."),("♐ SAGITARIO","Fortuna."),
     ("♉ TAURO","Exito."),("♍ VIRGO","Orden."),("♑ CAPRICORNIO","Rigor."),
     (" Gemini GÉMINIS","Palabra."),(" Libra LIBRA","Paz."),(" Aquarius ACUARIO","Visión."),
     (" Cancer CÁNCER","Lunar."),(" Scorpio ESCORPIO","Poder."),(" Pisces PISCIS","Unión.")]

hz = st.columns(4)
for i, (n, t) in enumerate(Z):
    with hz[i % 4]:
        st.markdown(f'<p class="sig">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:white;text-align:center;">{t}</p>', unsafe_allow_html=True)

# 6. RITUALES
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h2 class="titulo-seccion">BIENESTAR</h2>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)
with r1:
    st.markdown('<p class="oro">🌿 LAUREL</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Queme 3 hojas secas para limpiar su hogar.</p>', unsafe_allow_html=True)
with r2:
    st.markdown('<p class="oro">🧂 SAL</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Vaso con sal al hielo 9 días para protección.</p>', unsafe_allow_html=True)
with r3:
    st.markdown('<p class="oro">✨ CANELA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Sople hacia adentro el primer día del mes.</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#444;'>© OPHAY BCN</p>", unsafe_allow_html=True)
