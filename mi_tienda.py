import streamlit as st

# 1. SETUP DE PÁGINA
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. DEFINICIÓN DE VARIABLES (Para evitar NameError)
DESC_ORACULO = "Sesión privada de 45 minutos. Inmersión profunda, claridad y guía espiritual personalizada."
DESC_TAROT = "Mazo premium con bordes de oro. La herramienta definitiva para el buscador experto."
DESC_AMATISTA = "Geoda seleccionada a mano. Transmuta la energía y protege tu aura de vibraciones densas."

# 3. CSS ESTILO BOUTIQUE (ORO, PLATA Y NEGRO)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400;900&display=swap');
.main { background-color: #050505; }
[data-testid="stAppViewContainer"] { background-color: #050505; }
.oro-dios {
    font-family: 'Cinzel', serif;
    background: linear-gradient(90deg, #bf953f, #fcf6ba, #aa8232);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    font-weight: 900; text-align: center;
}
.plata-god {
    font-family: 'Montserrat'; font-weight: 900; font-size: 1.1rem;
    background: linear-gradient(145deg, #ffffff, #888888, #ffffff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-transform: uppercase;
}
.card { 
    background: #000; border: 1px solid #1a1a1a; padding: 20px; 
    border-radius: 15px; border-bottom: 4px solid #d4af37; 
}
.h-dia { color: #d4af37; font-size: 0.85rem; letter-spacing: 5px; font-weight: 900; }
</style>
""", unsafe_allow_html=True)

# 4. CABECERA
st.markdown('<h1 class="oro-dios" style="font-size:4rem; margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:12px;font-weight:900;font-size:0.8rem;margin-bottom:40px;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 5. SECCIÓN TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro-dios" style="font-size:1.2rem;">ORÁCULO MÍSTICO</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#888;font-size:0.8rem;text-align:center;">{DESC_ORACULO}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:1.5rem;">25€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro-dios" style="font-size:1.2rem;">TAROT RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#888;font-size:0.8rem;text-align:center;">{DESC_TAROT}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:1.5rem;">45€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro-dios" style="font-size:1.2rem;">AMATISTA SAGRADA</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#888;font-size:0.8rem;text-align:center;">{DESC_AMATISTA}</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#d4af37;text-align:center;font-weight:900;font-size:1.5rem;">15€</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 6. DESTINO SEMANAL
st.markdown("<br><h2 class='oro-dios' style='font-size:2.5rem;'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-god">LOS FRUTOS DE TU ESFUERZO LLEGAN AL FIN. PAGO CONFIRMADO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:10px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-god">LIMPIA TU HOGAR DE ENERGÍAS DENSAS. ATRAE ABUNDANCIA.</p>', unsafe_allow_html=True)

with t[1]:
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-god">MARTE IMPULSA TU NEGOCIO. MOMENTO DE CERRAR TRATOS.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:10px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-god">DOMINGO SEÑAL CLAVE. ESCUCHA TU INSTINTO.</p>', unsafe_allow_html=True)

with t[2]:
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-god">MERCURIO TE DA LA PALABRA JUSTA. HABLA SIN MIEDO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:10px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-god">OPORTUNIDAD DEL PASADO APARECE CUANDO MENOS LO ESPERAS.</p>', unsafe_allow_html=True)
