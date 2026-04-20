import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY", layout="wide")

# 2. ESTILO CSS: ORO Y PLATA IMPACTANTE
st.markdown("""
<style>
.main { background-color: #050505; }
[data-testid="stAppViewContainer"] { background-color: #050505; }
.oro {
    font-family: serif;
    background: linear-gradient(#cfb53b, #fcf6ba, #aa8232);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold; text-align: center;
}
.plata {
    font-family: sans-serif;
    background: linear-gradient(145deg, #fff, #888, #fff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900; font-size: 1.1rem; text-transform: uppercase;
}
.desc { color: #777; font-size: 0.8rem; text-align: center; font-style: italic; }
.box { border-left: 5px solid #d4af37; padding: 15px; background: #000; border-radius: 10px; }
.h { color: #d4af37; font-size: 0.8rem; font-weight: bold; letter-spacing: 2px; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-size:0.7rem;font-weight:900;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA CON DESCRIPCIONES LUJO
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
col = st.columns(3)

with col[0]:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro" style="font-size:1.2rem;">ORÁCULO 25€</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">Seda y revelaciones ancestrales.</p>', unsafe_allow_html=True)
with col[1]:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro" style="font-size:1.2rem;">RIDER LUXE 45€</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">Oro puro y estuche de terciopelo.</p>', unsafe_allow_html=True)
with col[2]:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro" style="font-size:1.2rem;">AMATISTA 15€</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc">Energía y protección natural.</p>', unsafe_allow_html=True)

# 5. DESTINO SEMANAL
st.markdown("<br><h2 class='oro'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="h">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">FRUTOS DE TU ESFUERZO LLEGAN.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">PAGO CONFIRMADO AL FIN.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h" style="margin-top:10px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">LIMPIA TU HOGAR. ATRAE ABUNDANCIA.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[1]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="h">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">MARTE IMPULSA TU NEGOCIO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">CIERRA TRATOS Y MUEVE ECONOMÍA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h" style="margin-top:10px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">DOMINGO SEÑAL CLAVE. INSTINTO.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[2]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="h">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">MERCURIO TE DA LA PALABRA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">HABLA SIN MIEDO, TE ESCUCHARÁN.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h" style="margin-top:10px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">OPORTUNIDAD DEL PASADO LLEGA.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t[3]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<p class="h">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">SUEÑOS VÍVIDOS. TU VOZ MANDA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">NO DUDES DE TU SENSACIÓN.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h" style="margin-top:10px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata">USA AMATISTA PARA PROTEGERTE.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center;color:#444;font-size:0.7rem;'>© MMXXVI OPHAY COLLECTION</p>", unsafe_allow_html=True)
