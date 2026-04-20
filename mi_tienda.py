import streamlit as st

# 1. AJUSTES
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. ESTILO CSS "ORO & OXFORD"
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
    .box-zod {
        background-color: #000; border: 1px solid #222;
        padding: 30px; border-radius: 20px; border-left: 5px solid #d4af37;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.8);
    }
    .h-dia { 
        color: #d4af37; font-size: 0.85rem; letter-spacing: 4px; 
        border-bottom: 1px solid #1a1a1a; margin: 20px 0 10px 0;
    }
    .precio { color: #d4af37; font-weight: bold; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#444;letter-spacing:6px;'>BARCELONA PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

# 4. TIENDA CON PRECIOS Y DESCRIPCIÓN
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

c1, c2, c3 = st.columns(3)
with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<div style="text-align:center;"><p class="oro">ORÁCULO MÍSTICO</p><p class="precio">25€</p></div>', unsafe_allow_html=True)
with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<div style="text-align:center;"><p class="oro">TAROT RIDER LUXE</p><p class="precio">45€</p></div>', unsafe_allow_html=True)
with c3:
    st.image(f"{b}/Amatista.png")
    st.markdown('<div style="text-align:center;"><p class="oro">PIEDRA AMATISTA</p><p class="precio">15€</p></div>', unsafe_allow_html=True)

# 5. DESTINO SEMANAL COMPLETO
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<div class="box-zod">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;">ARIES • LEO • SAGITARIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">EL CAMINO DE LA ACCIÓN</h3>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.write("### MARTE IMPULSA TU NEGOCIO. ES MOMENTO DE CERRAR TRATOS Y MOVER ENERGÍA.")
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.write("### SEÑAL CLAVE EL DOMINGO. ESCUCHA TU INSTINTO ANTES DE ACTUAR.")
    st.markdown('</div>', unsafe_allow_html=True)

with t[1]:
    st.markdown('<div class="box-zod">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;">TAURO • VIRGO • CAPRICORNIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">EL CAMINO DE LA COSECHA</h3>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.write("### FRUTOS ECONÓMICOS LLEGAN A TI. UN PAGO PENDIENTE SERÁ CONFIRMADO.")
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.write("### LIMPIA TU HOGAR DE ENERGÍAS DENSAS. ATRAE LA ABUNDANCIA PURA.")
    st.markdown('</div>', unsafe_allow_html=True)

with t[2]:
    st.markdown('<div class="box-zod">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;">GÉMINIS • LIBRA • ACUARIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">EL CAMINO DE LA VERDAD</h3>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.write("### MERCURIO TE DA LA PALABRA JUSTA. HABLA SIN MIEDO, TE ESCUCHARÁN.")
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.write("### UN ENCUENTRO CLAVE CON ALGUIEN DEL PASADO TRAERÁ UNA OPORTUNIDAD.")
    st.markdown('</div>', unsafe_allow_html=True)

with t[3]:
    st.markdown('<div class="box-zod">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;">CÁNCER • ESCORPIO • PISCIS</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">EL CAMINO DEL INSTINTO</h3>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.write("### SUEÑOS MUY VÍVIDOS. TU VOZ INTERIOR MANDA, NO DUDES DE ELLA.")
    st.markdown('<p class="h-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.write("### USA TU AMATISTA PARA PROTEGERTE. FILTRA LAS ENERGÍAS EXTERNAS.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;' class='plata'>© MMXXVI OPHAY COLLECTION • BCN</p>", unsafe_allow_html=True)
