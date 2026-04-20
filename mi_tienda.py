import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. ESTILO CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@800&display=swap');
    .main { 
        background-color: #0a0a0a; 
        background-image: radial-gradient(#1a1a1a 1px, transparent 1px);
        background-size: 30px 30px;
    }
    [data-testid="stAppViewContainer"] { background-color: #0a0a0a; }
    .oro {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #cfb53b, #fcf6ba, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; text-align: center;
    }
    .plata {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(to bottom, #e2e2e2, #ffffff, #666);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800; text-transform: uppercase;
    }
    .box {
        background-color: #000; border: 1px solid #222;
        padding: 25px; border-radius: 20px; border-left: 4px solid #d4af37;
    }
    .h-dia { 
        color: #d4af37; font-size: 0.8rem; letter-spacing: 5px; 
        border-bottom: 1px solid #1a1a1a; margin: 15px 0 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#444;letter-spacing:5px;'>BARCELONA PRIVATE</p>", unsafe_allow_html=True)

# 4. TIENDA (LÍNEAS CORTAS ANTI-CORTE)
u = "MINEGOCIO85"
r = "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

img1 = f"{b}/primera%20foto%20isoterica.png"
img2 = f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png"
img3 = f"{b}/Amatista.png"

c1, c2, c3 = st.columns(3)
with c1: st.image(img1, caption="ORÁCULO 25€")
with c2: st.image(img2, caption="RIDER LUXE 45€")
with c3: st.image(img3, caption="AMATISTA 15€")

# 5. DESTINO SEMANAL
st.markdown("<br><h2 class='oro'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

# BLOQUE FUEGO
with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">ARIES LEO SAGITARIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">CAMINO ACCIÓN</h3>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.write("**MARTE IMPULSA TU NEGOCIO. CIERRA TRATOS YA.**")
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.write("**SEÑAL CLAVE DOMINGO. ESCUCHA TU INSTINTO.**")
    st.markdown('</div>', unsafe_allow_html=True)

# BLOQUE TIERRA
with t[1]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">TAURO VIRGO CAPRICORNIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">CAMINO COSECHA</h3>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.write("**FRUTOS ECONÓMICOS. PAGO CONFIRMADO.**")
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.write("**LIMPIA TU HOGAR. ATRAE ABUNDANCIA.**")
    st.markdown('</div>', unsafe_allow_html=True)

# BLOQUE AIRE
with t[2]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">GÉMINIS LIBRA ACUARIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">CAMINO VERDAD</h3>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.write("**MERCURIO TE DA VOZ. HABLA SIN MIEDO.**")
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.write("**ENCUENTRO CLAVE CON ALGUIEN PASADO.**")
    st.markdown('</div>', unsafe_allow_html=True)

# BLOQUE AGUA
with t[3]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">CÁNCER ESCORPIO PISCIS</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">CAMINO INSTINTO</h3>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.write("**SUEÑOS VÍVIDOS. TU VOZ INTERIOR MANDA.**")
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.write("**USA TU AMATISTA. FILTRA ENERGÍAS.**")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;' class='plata'>© MMXXVI OPHAY</p>", unsafe_allow_html=True)
