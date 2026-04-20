import streamlit as st

# 1. CONFIGURACION
st.set_page_config(page_title="OPHAY", layout="wide")

# 2. ESTILO CSS MINIMALISTA (SOLO PARA TITULOS)
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:5px;">PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS (COLUMNAS SIMPLES)
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

c1, c2, c3 = st.columns(3)
with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO</p>', unsafe_allow_html=True)
    st.link_button("RESERVAR", f"{W}Cita")
with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE</p>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", f"{W}Mazo")
with c3:
    st.image(B + "Amatista.png")
    st.markdown('<p class="oro">AMATISTA</p>', unsafe_allow_html=True)
    st.link_button("CONSULTAR", f"{W}Piedra")

# 5. HOROSCOPO
st.divider()
st.markdown('<h2 class="oro">HORÓSCOPO</h2>', unsafe_allow_html=True)
Z = [("♈ ARIES","Fuego vital."),("♌ LEO","Brillo solar."),("♐ SAGITARIO","Fortuna."),
     ("♉ TAURO","Exito real."),("♍ VIRGO","Orden total."),("♑ CAPRICORNIO","Disciplina."),
     ("♊ GÉMINIS","Palabra viva."),("♎ LIBRA","Equilibrio."),("♒ ACUARIO","Vision."),
     ("♋ CÁNCER","Paz lunar."),("♏ ESCORPIO","Magnetismo."),("♓ PISCIS","Conexion.")]

cols = st.columns(4)
for i, (n, t) in enumerate(Z):
    with cols[i % 4]:
        st.subheader(n)
        st.write(t)

# 6. RITUALES (USANDO BLOQUES NATIVOS QUE NO FALLAN)
st.divider()
st.markdown('<h2 class="oro">BIENESTAR SAGRADO</h2>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)

with r1:
    st.warning("🌿 EL LAUREL (PURIFICACIÓN)")
    st.write("Prenda tres hojas secas y recorra su casa de dentro hacia fuera visualizando luz dorada.")
    st.caption("Color Sugerido: Plata")

with r2:
    st.info("🧂 SAL Y HIELO (NEUTRALIZAR)")
    st.write("Escriba el problema en papel, pongalo en un vaso con sal marina y deje al congelador 9 dias.")
    st.caption("Color Sugerido: Plata")

with r3:
    st.success("✨ LA CANELA (ABUNDANCIA)")
    st.write("Sople canela en polvo desde la puerta hacia el interior de su hogar para llamar al exito.")
    st.caption("Color Sugerido: Plata")

st.markdown("<p style='text-align:center;color:#444;margin-top:50px;'>© OPHAY BCN</p>", unsafe_allow_html=True)
