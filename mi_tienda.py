import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO MAESTRO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505; }
.oro { font-family: 'Cinzel'; color: #f1c40f; font-weight: 900; text-align: center; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 1.6rem; font-weight: 700; text-align: center; margin: 10px 0; border: 1px solid #f1c40f; padding: 5px; border-radius: 5px; }
.desc { color: #ffffff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; line-height: 1.6; background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; min-height: 120px; display: flex; align-items: center; justify-content: center; }
.sig { color: #f1c40f; font-family: 'Cinzel'; font-weight: 700; text-align: center; margin-top: 20px; font-size: 1.1rem; }
.plata { color: #bdc3c7; font-family: 'Montserrat'; font-size: 0.8rem; text-align: center; font-style: italic; margin-top: 10px; }
hr { border-color: rgba(241, 196, 15, 0.3) !important; }
/* Botón Estilo WhatsApp */
.stButton>button { border: 1px solid #f1c40f !important; color: #f1c40f !important; background: transparent !important; width: 100%; }
.stButton>button:hover { background: #f1c40f !important; color: #000 !important; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:10px; font-size:0.8rem; opacity:0.8;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. PRECIOS (CAMBIA LOS NÚMEROS AQUÍ ABAJO)
precio_oraculo = "100€" 
precio_rider = "80€"
precio_amatista = "150€"
# ---------------------------------------------------------

B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown(f'<p class="precio">{precio_oraculo}</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de clarividencia. Revelamos los hilos invisibles de su destino con alta precisión mística.</div>', unsafe_allow_html=True)
    st.link_button("CONSULTAR DISPONIBILIDAD", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown(f'<p class="precio">{precio_rider}</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Edición artesanal con acabados en oro. El mazo definitivo para una conexión superior con el Tarot.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR PIEZA", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown(f'<p class="precio">{precio_amatista}</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada seleccionada por su pureza. Ideal para proteger su santuario y transmutar energías.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR INFORMACIÓN", W)

# 5. HORÓSCOPO
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2.5rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

Z = [("♈ ARIES","Fuego vital."),("♌ LEO","Brillo solar."),("♐ SAGITARIO","Fortuna."),
     ("♉ TAURO","Exito real."),("♍ VIRGO","Orden total."),("♑ CAPRICORNIO","Disciplina."),
     ("♊ GÉMINIS","Palabra viva."),("♎ LIBRA","Equilibrio."),("♒ ACUARIO","Vision."),
     ("♋ CÁNCER","Paz lunar."),("♏ ESCORPIO","Magnetismo."),("♓ PISCIS","Conexion.")]

hz = st.columns(4)
for i, (n, t) in enumerate(Z):
    with hz[i % 4]:
        st.markdown(f'<p class="sig">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:white; text-align:center; font-size:0.9rem;">{t}</p>', unsafe_allow_html=True)

# 6. RITUALES
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2.5rem;">BIENESTAR SAGRADO</h2>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)
with r1:
    st.markdown('<p class="oro" style="font-size:1.5rem;">🌿 LAUREL</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:white; text-align:center;">Purificación energética profunda.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Queme tres hojas secas y recorra su hogar de dentro hacia fuera visualizando luz.</p>', unsafe_allow_html=True)

with r2:
    st.markdown('<p class="oro" style="font-size:1.5rem;">🧂 SAL Y HIELO</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:white; text-align:center;">Neutralización de envidias.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Escriba su intención, póngala en sal marina y deje 9 días en el congelador.</p>', unsafe_allow_html=True)

with r3:
    st.markdown('<p class="oro" style="font-size:1.5rem;">✨ CANELA</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:white; text-align:center;">Apertura de abundancia.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">El primer día del mes, sople canela en polvo desde el umbral hacia el interior.</p>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center; color:#555; font-size:0.7rem;'>© MMXXVI OPHAY BOUTIQUE BARCELONA</p>", unsafe_allow_html=True)
