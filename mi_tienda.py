import streamlit as st

# 1. CONFIGURACION
st.set_page_config(page_title="OPHAY", layout="wide")

# 2. CAJA FUERTE DE ESTILOS
STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@100;400;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.sig{color:#d4af37;font-family:'Cinzel';font-weight:700;margin-top:20px;font-size:1.1rem;text-align:center;}
.txt{color:#ccc;font-family:'Montserrat';font-size:0.75rem;text-align:center;font-weight:400;line-height:1.5;margin-bottom:25px;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:2px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:10px;font-weight:900;text-decoration:none;font-size:0.75rem;margin-top:10px;}
.box{border:1px double #d4af37;padding:25px;margin-top:20px;text-align:center;background:#050505;min-height:250px;}
</style>
"""
st.markdown(STYLE, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="font-size:0.7rem;">PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

c1, c2, c3 = st.columns(3)
with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}Cita" class="btn">RESERVAR</a>', unsafe_allow_html=True)
with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}Mazo" class="btn">ADQUIRIR</a>', unsafe_allow_html=True)
with c3:
    st.image(B + "Amatista.png")
    st.markdown('<p class="oro">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}Piedra" class="btn">CONSULTAR</a>', unsafe_allow_html=True)

# 5. HOROSCOPO
st.markdown('<h2 class="oro">HORÓSCOPO</h2>', unsafe_allow_html=True)
Z = [("♈ ARIES","Fuego vital."),("♌ LEO","Brillo solar."),("♐ SAGITARIO","Fortuna."),
     ("♉ TAURO","Exito real."),("♍ VIRGO","Orden total."),("♑ CAPRICORNIO","Disciplina."),
     ("♊ GÉMINIS","Palabra viva."),("♎ LIBRA","Equilibrio."),("♒ ACUARIO","Vision."),
     ("♋ CÁNCER","Paz lunar."),("♏ ESCORPIO","Magnetismo."),("♓ PISCIS","Conexion.")]

cols = st.columns(4)
for i, (n, t) in enumerate(Z):
    with cols[i % 4]:
        st.markdown(f'<p class="sig">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="txt">{t}</p>', unsafe_allow_html=True)

# 6. RITUALES (CONSTRUCCIÓN SEGURA POR FRAGMENTOS)
st.markdown('<h2 class="oro">BIENESTAR</h2>', unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)

# Ritual 1
with r1:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="oro">🌿 LAUREL</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Quema laurel seco para purificar.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Ritual 2
with r2:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="oro">🧂 SAL</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Vaso al hielo durante 9 dias.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Ritual 3
with r3:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="oro">✨ CANELA</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Sopla canela en su umbral.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#444;'>© OPHAY BCN</p>", unsafe_allow_html=True)
