import streamlit as st

# 1. CONFIG
st.set_page_config(page_title="OPHAY", layout="wide")

# 2. CSS PROTEGIDO
CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@100;400;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.sig{color:#d4af37;font-family:'Cinzel';font-weight:700;margin-top:20px;font-size:1.1rem;text-align:center;}
.txt{color:#ccc;font-family:'Montserrat';font-size:0.75rem;text-align:center;font-weight:400;line-height:1.5;margin-bottom:25px;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:2px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:8px;font-weight:900;text-decoration:none;font-size:0.7rem;margin-top:10px;}
.box{border:1px double #d4af37;padding:20px;margin-top:20px;text-align:center;background:#050505;min-height:160px;}
</style>"""
st.markdown(CSS, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-size:0.6rem;letter-spacing:5px;">PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}Cita" class="btn">RESERVAR</a></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}Mazo" class="btn">ADQUIRIR</a></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "Amatista.png")
    st.markdown('<p class="oro">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}Piedra" class="btn">CONSULTAR</a></div>', unsafe_allow_html=True)

# 5. ZODIACO
st.markdown("<br><h2 class='oro'>HORÓSCOPO</h2>", unsafe_allow_html=True)
cols = st.columns(4)
# Lista de datos corta
Z = [("♈ ARIES","Fuego vital."),("♉ TAURO","Exito real."),("♊ GÉMINIS","Palabra viva."),("♋ CÁNCER","Paz lunar."),
     ("♌ LEO","Brillo solar."),("♍ VIRGO","Orden total."),("♎ LIBRA","Equilibrio."),("♏ ESCORPIO","Magnetismo."),
     ("♐ SAGITARIO","Fortuna."),("♑ CAPRICORNIO","Disciplina."),("♒ ACUARIO","Vision."),("♓ PISCIS","Conexion.")]

for i, (n, t) in enumerate(Z):
    with cols[i % 4]:
        st.markdown(f'<p class="sig">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="txt">{t}</p>', unsafe_allow_html=True)

# 6. RITUALES
st.markdown("<br><h2 class='oro'>BIENESTAR</h2>", unsafe_allow_html=True)
r1, r2, r3 = st.columns(3)
with r1:
    st.markdown('<div class="box"><p class="oro">🌿 LAUREL</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Quema laurel para limpiar.</p></div>', unsafe_allow_html=True)
with r2:
    st.markdown('<div class="box"><p class="oro">🧂 SAL</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Vaso al hielo 9 dias.</p></div>', unsafe_allow_html=True)
with r3:
    st.markdown('<div class="box"><p class="oro
