import streamlit as st

# 1. CONFIGURACION
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS
CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@100;400;700&display=swap');
.main,[data-testid="stAppViewContainer"]{background-color:#000;}
.oro{font-family:'Cinzel';background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;text-align:center;}
.sig{color:#d4af37;font-family:'Cinzel';font-weight:700;margin-top:20px;font-size:1.1rem;text-align:center;}
.txt{color:#ccc;font-family:'Montserrat';font-size:0.75rem;text-align:center;font-weight:400;line-height:1.5;margin-bottom:25px;}
.card{background:#050505;border:1px solid #111;padding:15px;border-top:2px solid #d4af37;text-align:center;}
.btn{display:block;border:1px solid #bf953f;color:#bf953f!important;padding:8px;font-weight:900;text-decoration:none;font-size:0.7rem;margin-top:10px;}
.box{border:1px double #d4af37;padding:20px;margin-top:20px;text-align:center;background:#050505;}
</style>"""
st.markdown(CSS, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;font-size:0.6rem;letter-spacing:8px;">PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO</p><a href="'+W+'Cita" class="btn">RESERVAR</a></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE</p><a href="'+W+'Mazo" class="btn">ADQUIRIR</a></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(B + "Amatista.png")
    st.markdown('<p class="oro">AMATISTA</p><a href="'+W+'Piedra" class="btn">CONSULTAR</a></div>', unsafe_allow_html=True)

# 5. HOROSCOPO
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>HORÓSCOPO</h2>", unsafe_allow_html=True)

T1, T2, T3, T4 = "Fuego vital. Audacia hoy.", "Exito y enfoque real.", "Palabra con poder.", "Intuicion lunar hoy."
T5, T6, T7, T8 = "Brillo solar puro.", "Maestria y orden.", "Equilibrio y paz.", "Poder magnetico."
T9, T10, T11, T12 = "Fortuna visionaria.", "Disciplina y exito.", "Vision de futuro.", "Conexion espiritual."

cols = st.columns(4)
cols[0].markdown(f'<p class="sig">♈ ARIES</p><p class="txt">{T1}</p>', unsafe_allow_html=True)
cols[1].markdown(f'<p class="sig">♉ TAURO</p><p class="txt">{T2}</p>', unsafe_allow_html=True)
cols[2].markdown(f'<p class="sig">♊ GÉMINIS</p><p class="txt">{T3}</p>', unsafe_allow_html=True)
cols[3].markdown(f'<p class="sig">♋ CÁNCER</p><p class="txt">{T4}</p>', unsafe_allow_html=True)

cols2 = st.columns(4)
cols2[0].markdown(f'<p class="sig">♌ LEO</p><p class="txt">{T5}</p>', unsafe_allow_html=True)
cols2[1].markdown(f'<p class="sig">♍ VIRGO</p><p class="txt">{T6}</p>', unsafe_allow_html=True)
cols2[2].markdown(f'<p class="sig">♎ LIBRA</p><p class="txt">{T7}</p>', unsafe_allow_html=True)
cols2[3].markdown(f'<p class="sig">♏ ESCORPIO</p><p class="txt">{T8}</p>', unsafe_allow_html=True)

cols3 = st.columns(4)
cols3[0].markdown(f'<p class="sig">♐ SAGITARIO</p><p class="txt">{T9}</p>', unsafe_allow_html=True)
cols3[1].markdown(f'<p class="sig">♑ CAPRICORNIO</p><p class="txt">{T10}</p>', unsafe_allow_html=True)
cols3[2].markdown(f'<p class="sig">♒ ACUARIO</p><p class="txt">{T11}</p>', unsafe_allow_html=True)
cols3[3].markdown(f'<p class="sig">♓ PISCIS</p><p class="txt">{T12}</p>', unsafe_allow_html=True)

# 6. RITUALES
st.markdown("<br><h2 class='oro' style='font-size:2rem;'>RITUALES OPHAY</h2>", unsafe_allow_html=True)

r1, r2 = st.columns(2)
with r1:
    st.markdown('<div class="box"><p class="oro">🌿 LAUREL</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Quema laurel y visualiza luz dorada para renovar tu hogar.</p></div>', unsafe_allow_html=True)
with r2:
    st.markdown('<div class="box"><p class="oro">🧂 SAL Y HIELO</p>', unsafe_allow_html=True)
    st.markdown('<p class="txt">Pon sal gruesa en un vaso, escribe lo negativo en papel y al congelador 9 dias.</p></div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#333;font-size:0.5rem;'>© OPHAY BCN</p>", unsafe_allow_html=True)
