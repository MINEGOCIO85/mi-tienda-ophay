import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY Elite", layout="wide")

# 2. CSS: PLATA REFINADA Y ORO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@900&display=swap');
    .main { background-color: #050505; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    .oro {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #cfb53b, #fcf6ba, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; text-align: center;
    }
    
    .plata-fuerte {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(145deg, #fff 0%, #aaa 50%, #eee 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; 
        font-size: 1.1rem; 
        text-transform: uppercase; 
        line-height: 1.4;
    }

    .box { 
        background: #000; 
        border: 1px solid #222; 
        padding: 20px; 
        border-radius: 20px; 
        border-left: 6px solid #d4af37; 
    }
    
    .h-dia { 
        color: #d4af37; 
        font-size: 0.8rem; 
        letter-spacing: 4px; 
        font-weight: bold; 
        margin-bottom: 8px; 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:3.5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:10px;font-weight:900;font-size:0.7rem;">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS (Compacto)
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"
c1, c2, c3 = st.columns(3)
with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro">ORÁCULO 25€</p>', unsafe_allow_html=True)
with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro">RIDER LUXE 45€</p>', unsafe_allow_html=True)
with c3:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="oro">AMATISTA 15€</p>', unsafe_allow_html=True)

# 5. SECCIÓN TIERRA (RESALTADA)
st.markdown("<br><h2 class='oro' style='font-size:2.2rem;'>✨ DESTINO SEMANAL ✨</h2>", unsafe_allow_html=True)
t = st.tabs(["🌱 TIERRA", "🔥 FUEGO", "💨 AIRE", "💧 AGUA"])

with t[0]:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<h2 class="oro" style="text-align:left;font-size:1.5rem;">TAURO • VIRGO • CAPRICORNIO</h2>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia">LUNES A MIÉRCOLES</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">LOS FRUTOS DE TU ESFUERZO LLEGAN AL FIN. UN PAGO ESPERADO SERÁ CONFIRMADO.</p>', unsafe_allow_html=True)
    st.markdown('<p class="h-dia" style="margin-top:15px;">FIN DE SEMANA</p>', unsafe_allow_html=True)
    st.markdown('<p class="plata-fuerte">LIMPIA TU HOGAR DE ENERGÍAS DENSAS. ES EL MOMENTO DE ATRAER ABUNDANCIA.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Breve relleno para los otros tabs para evitar errores de carga
with t[1]: st.write("Consultando el Oráculo de Fuego...")
with t[2]: st.write("Consultando el Oráculo de Aire...")
with t[3]: st.write("Consultando el Oráculo de Agua...")

st.markdown("<br><p style='text-align:center;font-size:0.8rem;' class='plata-fuerte'>© MMXXVI OPHAY</p>", unsafe_allow_html=True)
