import streamlit as st

# 1. SETUP DE ÉLITE
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. VARIABLES DE TEXTO (PROTEGIDAS)
DESC_ORACULO = "SESIÓN PRIVADA DE 45 MINUTOS. CLARIDAD ABSOLUTA Y GUÍA ESPIRITUAL."
DESC_TAROT = "MAZO PREMIUM CON BORDES DE ORO. CALIDAD DE COLECCIONISTA."
DESC_AMATISTA = "GEODA NATURAL SELECCIONADA. PROTECCIÓN Y TRANSMUTACIÓN PURA."

# 3. CSS FUERZA BRUTA: PLATA CROMADO Y ORO MACIZO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@900&display=swap');
.main { background-color: #000; }
[data-testid="stAppViewContainer"] { background-color: #000; }

/* ORO TITÁNICO */
.oro-bruto {
    font-family: 'Cinzel', serif;
    background: linear-gradient(180deg, #bf953f 0%, #fcf6ba 50%, #aa8232 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    font-weight: 900; text-align: center;
}

/* PLATA FUERTE NIVEL DIOS (CROMADO AGRESIVO) */
.plata-bruta-total {
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 1.8rem;
    background: linear-gradient(to bottom, 
        #ffffff 0%, 
        #a1a1a1 40%, 
        #ffffff 50%, 
        #7e7e7e 60%, 
        #333333 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: uppercase;
    line-height: 1.1;
    letter-spacing: -1px;
    filter: drop-shadow(2px 2px 0px rgba(0,0,0,1)) drop-shadow(0px 0px 15px rgba(255,255,255,0.2));
}

.card-bruta { 
    background: #050505; border: 1px solid #1a1a1a; padding: 25px; 
    border-top: 6px solid #d4af37;
}

.h-dia { 
    color: #d4af37; font-size: 0.95rem; letter-spacing: 7px; 
    font-weight: 900; margin-bottom: 15px; border-bottom: 1px solid #222;
}
</style>
""", unsafe_allow_html=True)

# 4. CABECERA
st.markdown('<h1 class="oro-bruto" style="font-size:6.5rem; margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:18px;font-weight:900;font-size:0.9rem;margin-bottom:60px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 5. TIENDA DE LUJO
col = st.columns(3)
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

with col[0]:
    st.markdown('<div class="card-bruta">', unsafe_allow_html=True)
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro-bruto" style="font-size:1.6rem;">ORÁCULO</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#fff;font-size:0.85rem;text-align:center;font-weight:900;">{DESC_ORACULO}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:2rem;">25€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col[1]:
    st.markdown('<div class="card-bruta">', unsafe_allow_html=True)
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro-bruto" style="font-size:1.6rem;">RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#fff;font-size:0.85rem;text-align:center;font-weight:900;">{DESC_TAROT}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:2rem;">45€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col[2]:
    st.markdown('<div class="card-bruta">', unsafe_allow_html=True)
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro-bruto" style="font-size:1.6rem;">AMATISTA</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#fff;font-size:0.85rem;text-align:center;font-weight:900;">{DESC_AMATISTA}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:2rem;">15€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 6. EL BLOQUE DE PODER: LOS 4 ELEMENTOS
st.markdown("<br><br><h2 class='oro-bruto' style='font-size:4.5rem;'>✨ DESTINO ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

def render_destino(l1, l2, f1, f2):
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="plata-bruta-total">{l1}<br>{l2}</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:35px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="plata-bruta-total">{f1}<br>{f2}</p>', unsafe_allow_html=True)

with t[0]: render_destino("FRUTOS DEL ESFUERZO.", "PAGO CONFIRMADO.", "LIMPIA TU HOGAR.", "ATRAE ABUNDANCIA.")
with t[1]: render_destino("MARTE IMPULSA NEGOCIO.", "CIERRA TRATOS YA.", "DOMINGO SEÑAL CLAVE.", "INSTINTO PURO.")
with t[2]: render_destino("MERCURIO DA PODER.", "HABLA SIN MIEDO.", "OPORTUNIDAD PASADA.", "VUELVE A TI.")
with t[3]: render_destino("SUEÑOS VÍVIDOS.", "TU VOZ MANDA.", "USA TU AMATISTA.", "FILTRA ENERGÍA.")

st.markdown("<br><br><p style='text-align:center;color:#444;font-weight:900;letter-spacing:5px;'>© MMXXVI OPHAY BOUTIQUE • BARCELONA</p>", unsafe_allow_html=True)
