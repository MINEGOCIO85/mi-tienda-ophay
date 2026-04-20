import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO MAESTRO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505; }
.oro { font-family: 'Cinzel'; color: #f1c40f; font-weight: 900; text-align: center; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 1.2rem; font-weight: 700; text-align: center; margin: 10px 0; }
.desc { color: #ffffff; font-family: 'Montserrat'; font-size: 0.85rem; text-align: center; line-height: 1.6; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 8px; }
.sig { color: #f1c40f; font-family: 'Cinzel'; font-weight: 700; text-align: center; margin-top: 15px; }
.plata { color: #bdc3c7; font-family: 'Montserrat'; font-size: 0.75rem; text-align: center; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:8px; font-size:0.7rem;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS (CON PRECIO Y WHATSAPP)
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">60€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Consulta privada de clarividencia. Revelamos los hilos invisibles de su destino con alta precisión mística.</div>', unsafe_allow_html=True)
    st.link_button("💬 RESERVAR POR WHATSAPP", f"{W}Hola, deseo reservar una sesión de Oráculo")

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Edición artesanal con acabados en oro. El mazo definitivo para una conexión superior con el Tarot.</div>', unsafe_allow_html=True)
    st.link_button("💬 COMPRAR POR WHATSAPP", f"{W}Hola, quiero adquirir el mazo Rider Luxe Gold")

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="precio">35€</p>', unsafe_allow_html=True)
    st.markdown('<div class="desc">Geoda sagrada seleccionada por su pureza. Ideal para proteger su santuario y transmutar energías.</div>', unsafe_allow_html=True)
    st.link_button("💬 SOLICITAR POR WHATSAPP", f"{W}Hola, me interesa la pieza de Amatista Sagrada")

# 5. HORÓSCOPO COMPLETO
st.markdown("<br><hr style='border-color:#f1c40f;'><br>", unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2.5rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)

Z = [("♈ ARIES","Fuego vital."),("♌ LEO","Brillo solar."),("♐ SAGITARIO","Fortuna."),
     ("♉ TAURO","Exito real."),("♍ VIRGO","Orden total."),("♑ CAPRICORNIO","Disciplina."),
     ("♊ GÉMINIS","Palabra viva."),("♎ LIBRA","Equilibrio."),("♒ ACUARIO","Vision."),
     ("♋ CÁNCER","Paz lunar."),("♏ ESCORPIO","Magnetismo."),("♓ PISCIS","Conexion.")]

hz = st.columns(4)
for i, (n, t) in enumerate(Z):
    with hz[i % 4]:
        st.markdown(f'<p class="sig">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:white; text-align:center; font-size:0.8rem;">{t}</p>', unsafe_allow_html=True)

# 6. RITUALES (PASO A PASO)
st.markdown("<br><hr style='border-color:#f1c40f;'><br>", unsafe_allow_html=True)
st.markdown('<h2 class="oro" style="font-size:2rem;">BIENESTAR SAGRADO</h2>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)
with r1:
    st.markdown('<p class="oro">🌿 LAUREL</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:white; text-align:center; font-size:0.8rem;">Queme tres hojas de laurel para limpiar su hogar de sombras del pasado.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Paso: Recorra de dentro hacia fuera visualizando luz.</p>', unsafe_allow_html=True)

with r2:
    st.markdown('<p class="oro">🧂 SAL Y HIELO</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:white; text-align:center; font-size:0.8rem;">Neutralice envidias. Use un vaso de cristal con sal marina y su intención.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Paso: Deje 9 días en el congelador y luego deseche.</p>', unsafe_allow_html=True)

with r3:
    st.markdown('<p class="oro">✨ CANELA</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:white; text-align:center; font-size:0.8rem;">Atraiga abundancia. Sople canela en polvo el primer día de cada mes.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">Paso: Desde el umbral sople hacia el interior de su casa.</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#444;'>© MMXXVI OPHAY BOUTIQUE BARCELONA</p>", unsafe_allow_html=True)
