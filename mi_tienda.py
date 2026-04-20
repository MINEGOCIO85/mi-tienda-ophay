import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. ESTILO CSS: ORO Y PLATA DE ALTO IMPACTO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@900&display=swap');
    .main { background-color: #050505; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    .oro {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #cfb53b, #fcf6ba, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; text-align: center;
    }
    .plata-fuerte {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(145deg, #fff 0%, #aaa 50%, #eee 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; font-size: 1.4rem; text-transform: uppercase; line-height: 1.3;
    }
    .box { background: #000; border: 1px solid #222; padding: 25px; border-radius: 20px; border-left: 6px solid #d4af37; }
    .h-dia { color: #d4af37; font-size: 0.9rem; letter-spacing: 5px; font-weight: bold; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.7rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c1, c2, c3 = st.columns(3)
with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO 25€</p>', unsafe_allow_html=True)
with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE 45€</p>', unsafe_allow_html=True)
with c3:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro">AMATISTA 15€</p>', unsafe_allow_html=True)

# 5. DESTINO SEMANAL COMPLETO
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;">ARIES LEO SAGI</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p><p class="plata-fuerte">MARTE IMPULSA TU NEGOCIO. MOMENTO DE CERRAR TRATOS Y MOVER TU ECONOMÍA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p><p class="plata-fuerte">UNA SEÑAL CLAVE APARECE EL DOMINGO. ESCUCHA TU INSTINTO ANTES DE ACTUAR.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[1]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;">TAURO VIRGO CAPRI</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p><p class="plata-fuerte">LOS FRUTOS DE TU ESFUERZO LLEGAN AL FIN. UN PAGO ESPERADO SERÁ CONFIRMADO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p><p class="plata-fuerte">LIMPIA TU HOGAR DE ENERGÍAS DENSAS. ES EL MOMENTO DE ATRAER ABUNDANCIA.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[2]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;">GEMINIS LIBRA ACUA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p><p class="plata-fuerte">MERCURIO TE DA LA PALABRA JUSTA. HABLA SIN MIEDO, TUS IDEAS SERÁN ESCUCHADAS.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p><p class="plata-fuerte">UN ENCUENTRO CON ALGUIEN DEL PASADO TRAERÁ UNA OPORTUNIDAD QUE NO ESPERABAS.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[3]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;">CANCER SCORP PISCIS</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p><p class="plata-fuerte">SUEÑOS MUY VÍVIDOS. TU VOZ INTERIOR MANDA HOY, NO DUDES DE TUS SENSACIONES.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p><p class="plata-fuerte">USA TU AMATISTA PARA PROTEGER TU CAMPO. FILTRA LAS ENERGÍAS EXTERNAS.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;' class='plata-fuerte'>© MMXXVI OPHAY</p>", unsafe_allow_html=True)
