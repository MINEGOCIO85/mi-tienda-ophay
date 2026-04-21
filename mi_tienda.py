import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO CSS "INMUNE"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');

/* Fondo General */
.main,[data-testid="stAppViewContainer"]{ background-color: #050505 !important; }

/* Botón de Pago Personalizado (HTML) */
.btn-pago {
    background-color: #25D366 !important;
    color: white !important;
    text-align: center;
    padding: 12px 20px;
    text-decoration: none;
    display: block;
    border-radius: 10px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    margin-top: 10px;
    border: 1px solid #ffffff33;
    transition: 0.3s;
}
.btn-pago:hover {
    background-color: #128C7E !important;
    box-shadow: 0px 0px 15px #f1c40f66;
    transform: translateY(-2px);
}

/* WhatsApp Flotante (Redonda completa) */
.wa-wrap { position: fixed; bottom: 30px; right: 10%; z-index: 999999; display: flex; align-items: center; gap: 10px; }
.wa-box { background: white; color: black; padding: 8px 15px; border-radius: 20px 20px 0 20px; font-weight: 700; font-family: 'Montserrat'; font-size: 0.8rem; border: 1px solid #f1c40f; }
.wa-btn { background-color: #25d366; color: white !important; border-radius: 50% !important; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 30px; text-decoration: none !important; border: 2px solid white; box-shadow: 0 4px 15px #000; }

/* Textos */
.oro { font-family: 'Cinzel'; color: #f1c40f; text-align: center; font-weight: 900; }
.precio { font-family: 'Montserrat'; color: #f1c40f; font-size: 2rem; font-weight: 700; text-align: center; margin:0; }
.desc { color: #fff; font-family: 'Montserrat'; font-size: 0.85rem; text-align: center; background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; min-height: 60px; }
</style>

<div class="wa-wrap">
    <div class="wa-box">Asesoramiento Boutique ✨</div>
    <a href="https://wa.me/34684668398" class="wa-btn" target="_blank">🟢</a>
</div>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem; margin-top:-40px;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro" style="letter-spacing:6px; font-size:0.7rem; margin-bottom:30px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS CON BOTONES HTML
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398"
c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="oro">ORÁCULO</h2><p class="precio">25€</p><div class="desc">Consulta privada de tarot y clarividencia.</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}" class="btn-pago" target="_blank">RESERVAR CITA</a>', unsafe_allow_html=True)

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="oro">RIDER LUXE</h2><p class="precio">45€</p><div class="desc">Mazo artesanal de alta gama. Edición Oro.</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}" class="btn-pago" target="_blank">ADQUIRIR</a>', unsafe_allow_html=True)

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="oro">AMATISTA</h2><p class="precio">19,95€</p><div class="desc">Geoda sagrada de alta pureza. Protección.</div>', unsafe_allow_html=True)
    st.markdown(f'<a href="{W}" class="btn-pago" target="_blank">SOLICITAR</a>', unsafe_allow_html=True)

# 5. HORÓSCOPO
st.markdown('<br><h2 class="oro" style="font-size:2rem; margin-top:20px;">HORÓSCOPO ELITE</h2>', unsafe_allow_html=True)
sig = [("♈ ARIES","Fuego"),("♌ LEO","Sol"),("♐ SAGITARIO","Suerte"),("♉ TAURO","Éxito"),("♍ VIRGO","Orden"),("♑ CAPRICORNIO","Rigor"),("♊ GÉMINIS","Mente"),("♎ LIBRA","Paz"),("♒ ACUARIO","Visión"),("♋ CÁNCER","Luna"),("♏ ESCORPIO","Poder"),("♓ PISCIS","Unión")]
hz = st.columns(4)
for i, (n, t) in enumerate(sig):
    with hz[i % 4]:
        st.markdown(f'<p style="color:#f1c40f; text-align:center; font-family:Cinzel; margin:0; font-weight:bold; font-size:1rem;">{n}</p><p style="color:#888; text-align:center; font-size:0.75rem; margin-bottom:15px;">{t}</p>', unsafe_allow_html=True)

# 6. PIE
st.markdown('<br><hr style="border-color:#f1c40f22;">', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; font-size:0.7rem;'>© 2026 OPHAY
