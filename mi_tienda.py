import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY | Luxury Esoteric", layout="wide")

# 2. CSS: EFECTOS ORO Y PLATA FUERTES
st.markdown("""
    <style>
    .main { background-color: #050505; color: #FFFFFF; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    /* Efecto Oro OPHAY */
    .oro-text {
        font-family: 'Georgia', serif;
        background: linear-gradient(to bottom, #cfb53b 0%, #fcf6ba 20%, #d4af37 40%, #aa8232 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; text-transform: uppercase;
    }

    /* Efecto Plata OPHAY */
    .plata-text {
        font-family: 'Courier New', monospace;
        background: linear-gradient(to bottom, #e2e2e2 0%, #ffffff 20%, #999999 50%, #666666 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    .card {
        background: rgba(255, 255, 255, 0.02); border: 1px solid #333;
        padding: 15px; border-radius: 10px; text-align: center;
    }

    /* Pestañas personalizadas */
    .stTabs [data-baseweb="tab"] { font-size: 1.2rem !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. LOGO
st.markdown('<h1 style="text-align:center;" class="oro-text">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; letter-spacing:5px;'>BARCELONA PRIVATE</p>", unsafe_allow_html=True)

# 4. TIENDA (Simplificada para evitar fallos)
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c1, c2, c3 = st.columns(3)
with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png", caption="ORÁCULO - 25€")
with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png", caption="RIDER LUXE - 45€")
with c3:
    st.image(f"{b}/Amatista.png", caption="AMATISTA - 15€")

# 5. HORÓSCOPO METALIZADO
st.markdown("<br><h2 style='text-align:center;' class='oro-text'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t1:
    st.markdown('<h2 class="oro-text">ARIES - LEO - SAGITARIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata-text">EL CAMINO DE LA ACCIÓN</h3>', unsafe_allow_html=True)
    st.markdown("#### **LUNES A MIÉRCOLES**")
    st.info("MARTE IMPULSA TU NEGOCIO. CIERRA TRATOS YA.")
    st.markdown("#### **FIN DE SEMANA**")
    st.write("SEÑAL CLAVE EL DOMINGO. ESCUCHA.")

with t2:
    st.markdown('<h2 class="oro-text">TAURO - VIRGO - CAPRICORNIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata-text">EL CAMINO DE LA COSECHA</h3>', unsafe_allow_html=True)
    st.markdown("#### **LUNES A MIÉRCOLES**")
    st.info("FRUTOS ECONÓMICOS. PAGO CONFIRMADO.")
    st.markdown("#### **FIN DE SEMANA**")
    st.write("LIMPIA TU HOGAR. ATRAE ABUNDANCIA.")

with t3:
    st.markdown('<h2 class="oro-text">GÉMINIS - LIBRA - ACUARIO</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata-text">EL CAMINO DE LA VERDAD</h3>', unsafe_allow_html=True)
    st.markdown("#### **LUNES A MIÉRCOLES**")
    st.info("MERCURIO TE DA VOZ. HABLA SIN MIEDO.")
    st.markdown("#### **FIN DE SEMANA**")
    st.write("ENCUENTRO CLAVE CON ALGUIEN NUEVO.")

with t4:
    st.markdown('<h2 class="oro-text">CÁNCER - ESCORPIO - PISCIS</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="plata-text">EL CAMINO DEL INSTINTO</h3>', unsafe_allow_html=True)
    st.markdown("#### **LUNES A MIÉRCOLES**")
    st.info("SUEÑOS VÍVIDOS. TU VOZ INTERIOR MANDA.")
    st.markdown("#### **FIN DE SEMANA**")
    st.write("USA TU AMATISTA. FILTRA ENERGÍAS.")

st.markdown("<br><p style='text-align:center;' class='plata-text'>© MMXXVI OPHAY COLLECTION</p>", unsafe_allow_html=True)
