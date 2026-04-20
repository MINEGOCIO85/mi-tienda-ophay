import streamlit as st

# 1. AJUSTES TÉCNICOS
st.set_page_config(page_title="OPHAY | Elite", layout="wide")

# 2. ESTILO CSS: ORO, PLATA Y NEGRO PURO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@800&display=swap');
    .main { background-color: #000000; color: #FFFFFF; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    
    .oro {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #cfb53b 0%, #fcf6ba 30%, #d4af37 50%, #aa8232 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; text-align: center;
    }
    .plata {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(to bottom, #e2e2e2 0%, #ffffff 40%, #999999 60%, #666666 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800; text-transform: uppercase;
    }
    .box {
        background: #0a0a0a; border: 2px solid #1a1a1a;
        padding: 30px; border-radius: 20px; margin-top: 10px;
    }
    .header-dia { color: #d4af37; font-size: 0.8rem; letter-spacing: 4px; border-bottom: 1px solid #222; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem; margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; letter-spacing:8px;'>BARCELONA PRIVATE</p>", unsafe_allow_html=True)

# 4. TIENDA RÁPIDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c1, c2, c3 = st.columns(3)
with c1: st.image(f"{b}/primera%20foto%20isoterica.png", caption="ORÁCULO 25€")
with c2: st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png", caption="RIDER LUXE 45€")
with c3: st.image(f"{b}/Amatista.png", caption="AMATISTA 15€")

# 5. DESTINO SEMANAL
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
tabs = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with tabs[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">ARIES • LEO • SAGITARIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">EL CAMINO DE LA ACCIÓN</h3>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.3rem; font-weight:bold;">MARTE IMPULSA TU NEGOCIO. CIERRA TRATOS YA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.3rem; font-weight:bold;">SEÑAL CLAVE EL DOMINGO. ESCUCHA TU INSTINTO.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">TAURO • VIRGO • CAPRICORNIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">EL CAMINO DE LA COSECHA</h3>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.3rem; font-weight:bold;">FRUTOS ECONÓMICOS. PAGO CONFIRMADO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.3rem; font-weight:bold;">LIMPIA TU HOGAR. ATRAE ABUNDANCIA PURA.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">GÉMINIS • LIBRA • ACUARIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">EL CAMINO DE LA VERDAD</h3>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.3rem; font-weight:bold;">MERCURIO TE DA VOZ. HABLA SIN MIEDO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.3rem; font-weight:bold;">ENCUENTRO CLAVE CON ALGUIEN DEL PASADO.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro">CÁNCER • ESCORPIO • PISCIS</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata">EL CAMINO DEL INSTINTO</h3>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.3rem; font-weight:bold;">SUEÑOS VÍVIDOS. TU VOZ INTERIOR MANDA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:1.3rem; font-weight:bold;">USA TU AMATISTA. FILTRA ENERGÍAS EXTERNAS.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center;' class='plata'>© MMXXVI OPHAY COLLECTION</p>", unsafe_allow_html=True)
