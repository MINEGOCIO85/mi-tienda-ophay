import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "BOUTIQUE TOTAL"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.9rem; text-align: center; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 15px; min-height: 70px; }

/* EFECTO FOTOS */
[data-testid="stImage"] img { border-radius: 10px; transition: 0.5s; border: 1px solid #222; }
[data-testid="stImage"] img:hover { transform: scale(1.02); border: 1px solid #f1c40f; box-shadow: 0 0 15px #f1c40f44; }

/* WHATSAPP POSICIÓN SEGURA */
.wa-wrap { position: fixed; bottom: 30px; right: 20%; z-index: 999999; display: flex; align-items: center; gap: 12px; }
.wa-bubble { background: white; color: black; padding: 8px 15px; border-radius: 20px 20px 0 20px; font-weight: 700; font-family: 'Montserrat'; font-size: 0.8rem; border: 1px solid #f1c40f; }
.wa-btn { background-color: #25d366; color: white !important; border-radius: 50% !important; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 30px; text-decoration: none !important; box-shadow: 0 4px 15px #000; }

/* TESTIMONIOS Y SOCIAL */
.testi { font-style: italic; color: #bbb; text-align: center; padding: 15px; border-left: 2px solid #f1c40f; background: #111; border-radius: 0 10px 10px 0; font-size: 0.85rem; }
.social { color: #f1c40f !important; text-decoration: none; font-weight: 600; margin: 0 10px; font-size: 0.8rem; }
</style>
<div class="wa-wrap">
    <div class="wa-bubble">Asesoramiento Private Boutique ✨</div>
    <a href="https://wa.me/34684668398" class="wa-btn" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem; margin-top:-40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:6px; font-size:0.7rem; margin-bottom:30px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"
c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2><p class="precio">25€</p><div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR CITA", W)
with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2><p class="precio">45€</p><div class="desc">Mazo artesanal de alta gama. Edición Oro.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", W)
with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2><p class="precio">19,95€</p><div class="desc">Geoda sagrada de alta pureza. Protección.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR", W)

# 5. TESTIMONIOS Y CONTACTO
st.markdown('<br><br>', unsafe_allow_html=True)
t1, t2 = st.columns(2)
t1.markdown('<div class="testi">"La lectura del oráculo me dio la claridad que necesitaba."<br>— Elena M.</div>', unsafe_allow_html=True)
t2.markdown('<div class="testi">"El mazo Rider Luxe es una obra de arte. Envío perfecto."<br>— Marc R.</div>', unsafe_allow_html=True)

st.markdown('<br><hr style="border-color:#f1c40f22;"><br>', unsafe_allow_html=True)
con1, con2 = st.columns(2)
con1.markdown('<h3 class="oro">UBICACIÓN</h3><p style="text-align:center; color:white; font-size:0.8rem;">📍 Barcelona<br>(Cita previa exclusivamente)</p>', unsafe_allow_html=True)
con2.markdown('<h3 class="oro">HORARIO</h3><p style="text-align:center; color:white; font-size:0.8rem;">L-V: 10:00 - 20:00<br>S: 11:00 - 14:00</p>', unsafe_allow_html=True)

# 6. HORÓSCOPO
st.markdown('<br><h2 class="oro" style="font-size:2rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)
sig = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),("♉ TAURO","Éxito"),("♍ VIRGO","Orden"),("♑ CAPRICORNIO","Rigor"),("♊ GÉMINIS","Mente"),("♎ LIBRA","Paz"),("♒ ACUARIO","Visión"),("♋ CÁNCER","Luna"),("♏ ESCORPIO","Poder"),("♓ PISCIS","Unión")]
hz = st.columns(4)
for i, (n, t) in enumerate(sig):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin:0; font-weight:bold; font-size:0.9rem;">{n}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="color:#888; text-align:center; font-size:0.7rem; margin-bottom:10px;">{t}</p>', unsafe_allow_html=True)

# 7. PIE Y LEGAL
st.markdown('<br>', unsafe_allow_html=True)
with st.expander("⚖️ LEGAL"):
    st.write("Responsable: OPHAY BCN. Mayores de 18 años. Los datos se tratan según RGPD.")

st.markdown("""
<div style="text-align:center; margin-top:20px;">
    <a href="#" class="social">INSTAGRAM</a> | <a href="#" class="social">TIKTOK</a>
</div>
<p style='text-align:center; color:#333; font-size:0.6rem; margin-top:15px;'>© 2026 OPHAY BARCELONA</p>
""", unsafe_allow_
