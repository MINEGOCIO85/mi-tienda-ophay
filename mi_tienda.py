import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. CSS: ORO PURO Y PLATA METÁLICA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@900&display=swap');
    
    .main { background-color: #050505; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    /* LOGO PRINCIPAL */
    .oro-main {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; text-align: center; font-size: 4.5rem; margin-bottom: 0px;
    }

    /* BARCELONA PRIVATE BOUTIQUE - MÁXIMO DESTACA */
    .oro-destaque {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(to right, #bf953f, #fcf6ba, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; text-align: center;
        letter-spacing: 15px; font-size: 0.9rem;
        text-transform: uppercase; 
        margin-top: -10px; margin-bottom: 40px;
        filter: drop-shadow(0px 2px 2px rgba(0,0,0,0.5));
    }
    
    .plata-fuerte {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(145deg, #fff 0%, #aaa 50%, #eee 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; font-size: 1.5rem; text-transform: uppercase;
    }

    .box {
        background-color: #000; border: 1px solid #222;
        padding: 25px; border-radius: 20px; border-left: 6px solid #d4af37;
    }
    .h-dia { color: #d4af37; font-size: 0.9rem; letter-spacing: 5px; font-weight: bold; }
    .precio { color: #d4af37; font-weight: bold; font-size: 1.2rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA IMPACTANTE
st.markdown('<h1 class="oro-main">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro-destaque">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

c1, c2, c3 = st.columns(3)
with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro-main" style="font-size:1.2rem;">ORÁCULO</p><p class="precio">25€</p>', unsafe_allow_html=True)
with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro-main" style="font-size:1.2rem;">RIDER LUXE</p><p class="precio">45€</p>', unsafe_allow_html=True)
with c3:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro-main" style="font-size:1.2rem;">AMATISTA</p><p class="precio">15€</p>', unsafe_allow_html=True)

# 5. DESTINO
st.markdown("<br><h2 class='oro-main' style='font-size:2.5rem;'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro-main" style="text-align:left; font-size:1.8rem;">ARIES LEO SAGI</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">MARTE IMPULSA TU NEGOCIO. CIERRA TRATOS YA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">SEÑAL CLAVE DOMINGO. ESCUCHA TU INSTINTO.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[1]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro-main" style="text-align:left; font-size:1.8rem;">TAURO VIRGO CAPRI</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">FRUTOS ECONÓMICOS. PAGO CONFIRMADO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">LIMPIA TU HOGAR. ATRAE ABUNDANCIA PURA.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[2]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro-main" style="text-align:left; font-size:1.8rem;">GEMINIS LIBRA ACUA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">MERCURIO TE DA VOZ. HABLA SIN MIEDO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">ENCUENTRO CLAVE. OPORTUNIDAD DEL PASADO.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[3]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro-main" style="text-align:left; font-size:1.8rem;">CANCER SCORP PISCIS</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">SUEÑOS VÍVIDOS. TU VOZ INTERIOR MANDA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">USA TU AMATISTA. FILTRA ENERGÍAS.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;' class='plata-fuerte'>© MMXXVI OPHAY</p>", unsafe_allow_html=True)
