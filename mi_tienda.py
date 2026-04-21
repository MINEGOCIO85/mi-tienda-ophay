import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS INMUNE
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }

/* BOTONES VERDES REALES */
.btn-verde {
    background-color: #25D366 !important;
    color: white !important;
    text-align: center;
    padding: 12px;
    text-decoration: none;
    display: block;
    border-radius: 10px;
    font-family: 'Montserrat';
    font-weight: 700;
    margin-top: 10px;
    border: 1px solid #ffffff33;
}

/* WHATSAPP REDONDO */
.wa-wrap { position: fixed; bottom: 30px; right: 10%; z-index: 999; display: flex; align-items: center; gap: 10px; }
.wa-box { background: white; color: black; padding: 8px 15px; border-radius: 20px 20px 0 20px; font-weight: 700; font-size: 0.8rem; border: 1px solid #f1c40f; }
.wa-btn { background-color: #25d366; color: white !important; border-radius: 50% !important; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 30px; text-decoration: none !important; border: 2px solid white; }

.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 1.8rem; font-weight: 700; text-align: center; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.85rem; text-align: center; background: rgba(255,255,255,0.05); padding: 10px; border-radius: 10px; min-height: 50px; }
</style>

<div class="wa-wrap">
    <div class="wa-box">Atención Boutique ✨</div>
    <a href="https://wa.me/34684668398" class="wa-btn" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:5px; font-size:0.7rem;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"
c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro" style="font-size:1.2rem;">ORÁCULO</h2><p class="precio">25€</p><div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}" class="btn-verde">RESERVAR CITA</a>', unsafe_allow_html=True)
with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro" style="font-size:1.2rem;">RIDER LUXE</h2><p class="precio">45€</p><div class="desc">Mazo artesanal de alta gama. Edición Oro.</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}" class="btn-verde">ADQUIRIR</a>', unsafe_allow_html=True)
with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro" style="font-size:1.2rem;">AMATISTA</h2><p class="precio">19,95€</p><div class="desc">Geoda sagrada de alta pureza. Protección.</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}" class="btn-verde">SOLICITAR</a>', unsafe_allow_html=True)

# 5. HORÓSCOPO
st.markdown('<br><h2 class="oro" style="font-size:1.5rem;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)
sig = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),("♉ TAURO","Éxito"),("♍ VIRGO","Orden"),("♑ CAPRICORNIO","Rigor"),(" Gemini GÉMINIS","Mente"),(" Libra LIBRA","Paz"),(" Aquarius ACUARIO","Visión"),(" Cancer CÁNCER","Luna"),(" Scorpio ESCORPIO","Poder"),(" Pisces PISCIS","Unión")]
hz = st.columns(4)
for i, (n, t) in enumerate(sig):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; margin:0; font-weight:bold; font-size:0.9rem;">{n}</p><p style="color:#888; text-align:center; font-size:0.7rem; margin-bottom:10px;">{t}</p>', unsafe_allow_html=True)

# 6. PIE LEGAL (Línea protegida contra cortes)
st.markdown('<hr style="border-color:#222;">', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#555; font-size:0.6rem;">© 2026 OPHAY BARCELONA • MAYORES 18 AÑOS</p>', unsafe_allow_html=True)
