import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY", layout="wide")

# 2. ESTILO LUMINOSO Y EXCLUSIVO
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@400;700&display=swap');

/* Fondo gris noche para que no canse la vista */
.main,[data-testid="stAppViewContainer"]{
    background-color: #111111;
}

/* Oro vibrante y nítido */
.oro{
    font-family: 'Cinzel';
    color: #f1c40f;
    font-weight: 900;
    text-align: center;
    text-transform: uppercase;
}

/* Texto blanco puro para lectura fácil */
.texto-blanco{
    color: #ffffff;
    font-family: 'Montserrat';
    font-size: 0.9rem;
    text-align: center;
    line-height: 1.6;
}

/* Plata brillante */
.plata{
    color: #e5e7e9;
    font-family: 'Montserrat';
    font-size: 0.85rem;
    text-align: center;
    font-style: italic;
}

/* Tarjetas con borde definido */
.card{
    background-color: #1a1a1a;
    border: 2px solid #f1c40f;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

/* Divisores dorados */
hr {
    border: 0;
    height: 1px;
    background: #f1c40f;
    margin: 40px 0;
}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#f1c40f; text-align:center; letter-spacing:8px; font-weight:700;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
st.markdown("<br>", unsafe_allow_html=True)
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO</p>', unsafe_allow_html=True)
    st.link_button("RESERVAR CITA", f"{W}Cita")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE</p>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", f"{W}Mazo")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "Amatista.png")
    st.markdown('<p class="oro">AMATISTA</p>', unsafe_allow_html=True)
    st.link_button("CONSULTAR", f"{W}Piedra")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. HORÓSCOPO (LIMPIO Y CLARO)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<h2 class="oro">HORÓSCOPO</h2>', unsafe_allow_html=True)

Z = [("♈ ARIES","Fuego vital."),("♌ LEO","Brillo solar."),("♐ SAGITARIO","Fortuna."),
     ("♉ TAURO","Exito real."),("♍ VIRGO","Orden total."),("♑ CAPRICORNIO","Disciplina."),
     ("♊ GÉMINIS","Palabra viva."),("♎ LIBRA","Equilibrio."),("♒ ACUARIO","Vision."),
     ("♋ CÁNCER","Paz lunar."),("♏ ESCORPIO","Magnetismo."),("♓ PISCIS","Conexion.")]

cols = st.columns(4)
for i, (n, t) in enumerate(Z):
    with cols[i % 4]:
        st.markdown(f'<h3 style="color:#f1c40f; text-align:center;">{n}</h3>', unsafe_allow_html=True)
        st.markdown(f'<p class="texto-blanco">{t}</p>', unsafe_allow_html=True)

# 6. BIENESTAR (RITUALES EN PLATA Y ORO)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<h2 class="oro">BIENESTAR SAGRADO</h2>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)

with r1:
    st.markdown('<p class="oro" style="font-size:1.5rem;">🌿 LAUREL</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto-blanco"><b>Purificación:</b> Prenda tres hojas secas y recorra su hogar de dentro hacia fuera.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Visualice luz dorada sellando sus paredes.</p>', unsafe_allow_html=True)

with r2:
    st.markdown('<p class="oro" style="font-size:1.5rem;">🧂 SAL Y HIELO</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto-blanco"><b>Protección:</b> Escriba su problema en papel y póngalo en un vaso con sal marina.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Deje en el congelador 9 días para neutralizar.</p>', unsafe_allow_html=True)

with r3:
    st.markdown('<p class="oro" style="font-size:1.5rem;">✨ CANELA</p>', unsafe_allow_html=True)
    st.markdown('<p class="texto-blanco"><b>Abundancia:</b> Sople canela en polvo desde la puerta hacia el interior.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Llame al éxito y la fortuna el primer día del mes.</p>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center; color:#777;'>© OPHAY BOUTIQUE BARCELONA</p>", unsafe_allow_html=True)
