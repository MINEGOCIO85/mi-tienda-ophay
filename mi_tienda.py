import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "ANTIKILL" (Para que el botón se vea 100% entero)
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

/* BOTÓN FLOTANTE RE-CALIBRADO */
.float-wa {
    position: fixed;
    bottom: 40px; 
    right: 50px; /* Lo alejamos más del borde derecho para que no se corte */
    background-color: #25d366;
    color: white !important;
    border-radius: 50% !important; /* Asegura círculo perfecto */
    width: 60px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.8);
    z-index: 9999999; 
    text-decoration: none !important;
    border: 1px solid rgba(255,255,255,0.2);
}
.float-wa:hover {
    transform: scale(1.1);
    background-color: #128c7e;
}
</style>

<a href="https://wa.me/34684668398" class="float-wa" target="_blank" title="Contactar por WhatsApp">
    🟢
</a>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem; margin-top: -40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:5px; font-size:0.8rem; margin-bottom: 40px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de tarot y clarividencia. Sesión de 30 min.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR SESIÓN", W)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Mazo artesanal de alta gama. Edición Oro.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">19,95€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada de alta pureza. Protección espiritual.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. HORÓSCOPO (LOS 12 SIGNOS COMPLETOS)
st.markdown('<br><hr style="border-color: rgba(241, 196, 15, 0.2);"><br>', unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2.5rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

S = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),
     ("♉ TAURO","Éxito"),("♍ VIRGO","Orden"),("♑ CAPRI","Rigor"),
     ("♊ GÉMINIS","Mente"),("♎ LIBRA","Paz"),("♒ ACUARIO","Visión"),
     ("♋ CÁNCER","Luna"),("♏ ESCORPIO","Poder"),("♓ PISCIS","Unión")]

hz = st.columns(4)
for i, (n, t) in enumerate(S):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin-bottom:0; font-weight:bold; font-size: 1.1rem;">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#888; text-align:center; font-size:0.8rem; margin-top:0;">{t}</p>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center; color:#444; font-size: 0.7rem;'>© MMXXVI OPHAY BARCELONA</p>", unsafe_allow_html=True)
