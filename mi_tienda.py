import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY | Elite", layout="wide")

# 2. CSS: FONDO OXFORD Y CAJAS EN RELIEVE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@800&display=swap');
    
    /* Fondo Oxford con textura */
    .main { 
        background-color: #0f0f0f; 
        background-image: radial-gradient(circle, #1a1a1a 1px, #0f0f0f 1px);
        background-size: 40px 40px;
        color: #FFFFFF; 
    }
    [data-testid="stAppViewContainer"] { background-color: #0f0f0f; }
    
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

    /* Caja de Predicción Resaltada */
    .box-resaltada {
        background-color: #000000; 
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 35px; 
        border-radius: 20px; 
        margin-top: 15px;
        box-shadow: 0px 10px 40px rgba(0,0,0,0.8), 0px 0px 20px rgba(212, 175, 55, 0.05);
    }

    .header-dia { 
        color: #d4af37; 
        font-size: 0.85rem; 
        letter-spacing: 5px; 
        border-bottom: 1px solid #222; 
        margin-bottom: 15px; 
        opacity: 0.8;
    }

    .stTabs [data-baseweb="tab"] { color: #555 !important; font-family: 'Cinzel'; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:4rem; margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#444; letter-spacing:8px; font-size:0.7rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

# 4. TIENDA (IMÁGENES)
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c1, c2, c3 = st.columns(3)
with c1: st.image(f"{b}/primera%20foto%20isoterica.png", caption="ORÁCULO 25€")
with c2: st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png", caption="RIDER LUXE 45€")
with c3: st.image(f"{b}/Amatista.png", caption="AMATISTA 15€")

# 5. DESTINO SEMANAL
st.markdown("<br><h2 class='oro' style='font-size:2.5rem;'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
tabs = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

# Función interna simple para evitar errores de sintaxis
def show_prediction(signos, camino, txt1, txt2):
    st.markdown(f'<div class="box-resaltada">', unsafe_allow_html=True)
    st.markdown(f'<h2 class="oro" style="text-align:left; font-size:1.8rem;">{signos}</h2>', unsafe_allow_html=True)
    st.markdown(f'<h3 class="plata" style="font-size:1.1rem; letter-spacing:2px;">{camino}</h3>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:1.25rem; font-weight:bold; color:#fff; line-height:1.5;">{txt1}</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-dia" style="margin-top:25px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:1.25rem; font-weight:bold; color:#fff; line-height:1.5;">{txt2}</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tabs[0]:
    show_prediction("ARIES • LEO • SAGITARIO", "EL CAMINO DE LA ACCIÓN", 
                   "MARTE IMPULSA TU NEGOCIO. CIERRA TRATOS YA.", 
                   "SEÑAL CLAVE EL DOMINGO. ESCUCHA TU INSTINTO.")

with tabs[1]:
    show_prediction("TAURO • VIRGO • CAPRICORNIO", "EL CAMINO DE LA COSECHA", 
                   "FRUTOS ECONÓMICOS. PAGO CONFIRMADO.", 
                   "LIMPIA TU HOGAR. ATRAE ABUNDANCIA PURA.")

with tabs[2]:
    show_prediction("GÉMINIS • LIBRA • ACUARIO", "EL CAMINO DE LA VERDAD", 
                   "MERCURIO TE DA VOZ. HABLA SIN MIEDO.", 
                   "ENCUENTRO CLAVE CON ALGUIEN DEL PASADO.")

with tabs[3]:
    show_prediction("CÁNCER • ESCORPIO • PISCIS",
