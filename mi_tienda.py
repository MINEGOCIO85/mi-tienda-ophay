import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS CON ICONO DE WHATSAPP
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505; }
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 15px; min-height: 100px; margin-bottom: 15px; }

/* BOTÓN WHATSAPP CON ICONO */
div[data-testid="stLinkButton"] > a {
    background-color: #25D366 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Montserrat' !important;
    font-weight: 700 !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    text-decoration: none !important;
    padding: 10px !important;
    transition: 0.3s !important;
}
div[data-testid="stLinkButton"] > a:hover {
    background-color: #128C7E !important;
    transform: scale(1.02);
    box-shadow: 0 0 15px rgba(37,211,102,0.4) !important;
}
hr { border-color: rgba(241, 196, 15, 0.2); }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:5px; font-size:0.8rem;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia. Sesión de 30 min.</div>', unsafe_allow_html=True)
    st.link_button("💬 WHATSAPP", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal de alta gama. Edición Oro.</div>', unsafe_allow_html=True)
    st.link_button("💬 COMPRAR", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada de alta pureza. Protección.</div>', unsafe_allow_html=True)
    st.link_button("💬 PEDIR", W)

# 5. HORÓSCOPO
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h2 class="oro">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

S = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),
     ("♉ TAURO","Éxito"),("♍ VIRGO","Orden"),("♑ CAPRI","Rigor"),
     (" Gemini GÉMINIS","Mente"),(" Libra LIBRA","Paz"),(" Aquarius ACUARIO","Visión."),
     (" Cancer CÁNCER","Luna"),(" Scorpio ESCORPIO","Poder"),(" Pisces PISCIS","Unión")]

hz = st.columns(4)
for i, (n, t) in enumerate(S):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin-bottom:0;">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#888; text-align:center; font-size:0.8rem; margin-top:0;">{t}</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#333;'>© MMXXVI OPHAY BCN</p>", unsafe_allow_html=True)
