import streamlit as st

# 1. SETUP DE ALTA GAMA
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. VARIABLES DE TEXTO (PROTEGIDAS CONTRA ERRORES)
DESC_ORACULO = "SESIÓN PRIVADA DE 45 MINUTOS. CLARIDAD ABSOLUTA Y GUÍA ESPIRITUAL."
DESC_TAROT = "MAZO PREMIUM CON BORDES DE ORO. CALIDAD DE COLECCIONISTA."
DESC_AMATISTA = "GEODA NATURAL SELECCIONADA. PROTECCIÓN Y TRANSMUTACIÓN PURA."

# 3. CSS FUERZA BRUTA + PLATA DINÁMICO
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

/* PLATA FUERTE TIPO ACERO REAL */
.plata-bruta {
    font-family: 'Montserrat'; 
    font-weight: 900; 
    font-size: 1.4rem; 
    background: linear-gradient(90deg, #888 0%, #fff 45%, #eee 55%, #666 100%);
    -webkit-background-clip: text; 
    -webkit-text-fill-color: transparent;
    text-transform: uppercase; 
    line-height: 1.1;
    filter: drop-shadow(0px 2px 4px rgba(255,255,255,0.1));
}

.card-bruta { 
    background: #050505; border: 1px solid #222; padding: 25px; 
    border-top: 5px solid #d4af37;
}

.h-dia { color: #d4af37; font-size: 0.9rem; letter-spacing: 6px; font-weight: 900; margin-bottom: 5px;}
</style>
""", unsafe_allow_html=True)

# 4. CABECERA
st.markdown('<h1 class="oro-bruto" style="font-size:6rem; margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:15px;font-weight:900;font-size:0.9rem;margin-bottom:60px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 5. TIENDA (PRODUCTOS)
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
col = st.columns(3)

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

# 6. DESTINO SEMANAL (LOS 4 ELEMENTOS)
st.markdown("<br><br><h2 class='oro-bruto' style='font-size:3.5rem;'>✨ DESTINO ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p><p class="plata-bruta">FRUTOS ECONÓMICOS. PAGO CONFIRMADO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p><p class="plata-bruta">LIMPIA TU HOGAR. ATRAE ABUNDANCIA PURA.</p>', unsafe_allow_html=True)

with t[1]:
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p><p class="plata-bruta">MARTE IMPULSA TU NEGOCIO. CIERRA TRATOS YA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p><p class="plata-bruta">DOMINGO SEÑAL CLAVE. ESCUCHA EL INSTINTO.</p>', unsafe_allow_html=True)

with t[2]:
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p><p class="plata-bruta">MERCURIO TE DA LA PALABRA. HABLA SIN MIEDO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p><p class="plata-bruta">UNA OPORTUNIDAD DEL PASADO APARECE.</p>', unsafe_allow_html=True)

with t[3]:
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p><p class="plata-bruta">SUEÑOS VÍVIDOS. TU VOZ INTERIOR MANDA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:20px;">FIN DE SEMANA</p><p class="plata-bruta">USA TU AMATISTA PARA FILTRAR ENERGÍAS.</p>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center;color:#444;font-weight:900;'>© MMXXVI OPHAY BOUTIQUE • BCN</p>", unsafe_allow_html=True)
