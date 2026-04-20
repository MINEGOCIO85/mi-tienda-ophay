import streamlit as st

# 1. AJUSTES
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. CSS: PLATA Y ORO EXTREMO
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
        font-weight: 900; font-size: 1.5rem; text-transform: uppercase;
    }

    .box {
        background-color: #000; border: 1px solid #222;
        padding: 20px; border-radius: 15px; border-left: 6px solid #d4af37;
    }
    .h-dia { color: #d4af37; font-size: 0.9rem; letter-spacing: 4px; }
    .precio { color: #d4af37; font-weight: bold; font-size: 1.2rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#444;font-size:0.7rem;'>BCN PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

# 4. TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

c1, c2, c3 = st.columns(3)
with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO</p><p class="precio">25€</p>', unsafe_allow_html=True)
with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE</p><p class="precio">45€</p>', unsafe_allow_html=True)
with c3:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro">AMATISTA</p><p class="precio">15€</p>', unsafe_allow_html=True)

# 5. DESTINO
st.markdown("<br><h2 class='oro'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">ARIES LEO SAGI</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">MARTE IMPULSA TU NEGOCIO. CIERRA TRATOS YA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">SEÑAL CLAVE DOMINGO. ESCUCHA TU INSTINTO.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[1]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">TAURO VIRGO CAPRI</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">FRUTOS ECONÓMICOS. PAGO CONFIRMADO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">LIMPIA TU HOGAR. ATRAE ABUNDANCIA PURA.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[2]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">GEMINIS LIBRA ACUA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">MERCURIO TE DA VOZ. HABLA SIN MIEDO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">ENCUENTRO CLAVE. OPORTUNIDAD DEL PASADO.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[3]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">CANCER SCORP PISCIS</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">SUEÑOS VÍVIDOS. TU VOZ INTERIOR MANDA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">USA TU AMATISTA. FILTRA ENERGÍAS.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;' class='plata-fuerte'>© MMXXVI OPHAY</p>", unsafe_allow_html=True)
