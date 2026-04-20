import streamlit as st
import urllib.parse

# 1. SETUP DE ÉLITE
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. CONFIGURACIÓN DE WHATSAPP
TELEFONO = "34600000000" # <--- CAMBIA ESTO POR TU NÚMERO REAL

def crear_link(producto):
    mensaje = urllib.parse.quote(f"Hola OPHAY, me interesa el {producto}. ¿Me das más información?")
    return f"https://wa.me/{TELEFONO}?text={mensaje}"

# 3. VARIABLES DE TEXTO
DESC_ORACULO = "SESIÓN PRIVADA DE 45 MINUTOS. CLARIDAD ABSOLUTA Y GUÍA ESPIRITUAL."
DESC_TAROT = "MAZO PREMIUM CON BORDES DE ORO. CALIDAD DE COLECCIONISTA."
DESC_AMATISTA = "GEODA NATURAL SELECCIONADA. PROTECCIÓN Y TRANSMUTACIÓN PURA."

# 4. CSS FUERZA BRUTA + BOTONES ORO
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@900&family=Montserrat:wght@900&display=swap');
.main { background-color: #000; }
[data-testid="stAppViewContainer"] { background-color: #000; }

.oro-bruto {
    font-family: 'Cinzel', serif;
    background: linear-gradient(180deg, #bf953f, #fcf6ba, #aa8232);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    font-weight: 900; text-align: center;
}

.plata-bruta-total {
    font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 1.8rem;
    background: linear-gradient(to bottom, #fff 0%, #a1a1a1 40%, #fff 50%, #7e7e7e 60%, #333 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-transform: uppercase; line-height: 1.1; filter: drop-shadow(2px 2px 0px #000);
}

.btn-whatsapp {
    display: block;
    background: linear-gradient(180deg, #bf953f, #aa8232);
    color: #000 !important;
    text-align: center;
    padding: 12px;
    text-decoration: none;
    font-family: 'Montserrat';
    font-weight: 900;
    border-radius: 5px;
    margin-top: 15px;
    text-transform: uppercase;
    font-size: 0.8rem;
}

.card-bruta { 
    background: #050505; border: 1px solid #1a1a1a; padding: 25px; border-top: 6px solid #d4af37;
}

.h-dia { color: #d4af37; font-size: 0.95rem; letter-spacing: 7px; font-weight: 900; margin-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

# 5. CABECERA
st.markdown('<h1 class="oro-bruto" style="font-size:6.5rem; margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.
