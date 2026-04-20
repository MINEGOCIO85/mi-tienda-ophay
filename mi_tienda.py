import streamlit as st

# 1. CONFIGURACIÓN DE ALTA GAMA
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. INYECCIÓN DE ESTILO (PROTEGIDO EN BLOQUE)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color: #0a0a0a;}
.oro {
    font-family: 'Cinzel';
    background: linear-gradient(180deg, #d4af37, #fcf6ba, #aa8232);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
    text-align: center;
}
.txt-blanco {color: #ffffff; font-family: 'Montserrat'; text-align: center; font-size: 0.85rem; line-height: 1.6;}
.txt-plata {color: #C0C0C0; font-family: 'Montserrat'; text-align: center; font-size: 0.75rem; font-style: italic;}
.card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:10px;">PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS (ESTRUCTURA BLINDADA)
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">CONEXIÓN ANCESTRAL</h2>', unsafe_allow_html=True)
    st.write("Acceda a la sabiduría del destino a través de nuestro Oráculo privado.")
    st.link_button("RESERVAR CITA", f"{W}Oraculo")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE GOLD</h2>', unsafe_allow_html=True)
    st.write("Edición limitada con acabados artesanales para maestros.")
    st.link_button("ADQUIRIR", f"{W}Rider")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA SAGRADA</h2>', unsafe_allow_html=True)
    st.write("Pieza única de transmutación energética seleccionada.")
    st.link_button("CONSULTAR", f"{W}Amatista")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. HORÓSCOPO (ORGANIZADO)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2.5rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

Z = [("♈ ARIES","Fuego vital."),("♌ LEO","Brillo solar."),("♐ SAGITARIO","Fortuna."),
     ("♉ TAURO","Exito real."),("♍ VIRGO","Orden total."),("♑ CAPRICORNIO","Disciplina."),
     ("♊ GÉMINIS","Palabra viva."),("♎ LIBRA","Equilibrio."),("♒ ACUARIO","Vision."),
     ("♋ CÁNCER","Paz lunar."),("♏ ESCORPIO","Magnetismo."),("♓ PISCIS","Conexion.")]

hz = st.columns(4)
for i, (signo, desc) in enumerate(Z):
    with hz[i % 4]:
        st.markdown(f'<p class="oro" style="font-size:1.2rem;">{signo}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="txt-blanco">{desc}</p>', unsafe_allow_html=True)

# 6. BIENESTAR (LÍNEAS CORTAS ANTICORTE)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2.5rem;">BIENESTAR SAGRADO</h2>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)
with r1:
    st.markdown('<p class="oro">🌿 LAUREL</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt-blanco">Purificación total del hogar.</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt-plata">Queme tres hojas de dentro hacia fuera.</p>', unsafe_allow_html=True)
with r2:
    st.markdown('<p class="oro">🧂 SAL Y HIELO</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt-blanco">Neutralización de energías densas.</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt-plata">Nueve días en frío con su intención.</p>', unsafe_allow_html=True)
with r3:
    st.markdown('<p class="oro">✨ CANELA</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt-blanco">Apertura de caminos y abundancia.</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt-plata">Sople hacia dentro el primer día del mes.</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#444;'>© OPHAY BOUTIQUE BARCELONA</p>", unsafe_allow_html=True)
