import streamlit as st

# 1. AJUSTES TÉCNICOS
st.set_page_config(page_title="OPHAY | Boutique & Destino", layout="wide")

# 2. ESTILO VISUAL "MYSTIC LUXURY"
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #eee; }
    [data-testid="stAppViewContainer"] { background-color: #0d0d0d; }
    .logo-text {
        font-family: serif; text-align: center; font-size: 3.5rem; letter-spacing: 12px;
        background: linear-gradient(145deg, #fff, #d4af37, #aa8a2e);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; margin: 0;
    }
    .card {
        background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.2);
        padding: 20px; border-radius: 15px; text-align: center;
    }
    /* Estilo para que el horóscopo destaque */
    .highlight-camino {
        color: #d4af37; font-weight: bold; font-size: 1.2rem; 
        letter-spacing: 2px; text-transform: uppercase;
    }
    .stTabs [data-baseweb="tab"] { color: #888 !important; font-size: 1.2rem !important; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="logo-text">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#d4af37;letter-spacing:5px;font-size:0.7rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

# 4. PRODUCTOS
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<div style="color:#d4af37;font-weight:bold;margin-top:10px;">ORÁCULO</div><div>25€</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<div style="color:#d4af37;font-weight:bold;margin-top:10px;">RIDER LUXE</div><div>45€</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/Amatista.png")
    st.markdown('<div style="color:#d4af37;font-weight:bold;margin-top:10px;">AMATISTA</div><div>15€</div>', unsafe_allow_html=True)
    st.link_button("COMPRAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. HORÓSCOPO SEMANAL POTENCIADO
st.markdown("<br><hr style='border-color:#333;'><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#d4af37;font-family:serif;letter-spacing:4px;'>✨ PREDICCIONES DEL DESTINO ✨</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#666;'>Semana del 20 al 26 de Abril, 2026</p>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t1:
    st.markdown("<p class='highlight-camino'>♈ ♌ ♐ EL CAMINO DE LA ACCIÓN</p>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    col_a.metric("ESTADO", "Fuerza Marte")
    col_b.metric("DÍA CLAVE", "Miércoles")
    st.write("---")
    st.markdown("🌑 **Lunes a Miércoles:** La energía te impulsa a cerrar ciclos. Cierra tratos ahora.")
    st.markdown("🌕 **Jueves a Domingo:** Recibirás una señal intuitiva clave sobre tu futuro laboral.")

with t2:
    st.markdown("<p class='highlight-camino'>♉ ♍ ♑ EL CAMINO DE LA COSECHA</p>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    col_a.metric("ESTADO", "Abundancia")
    col_b.metric("DÍA CLAVE", "Martes")
    st.write("---")
    st.markdown("💰 **Lunes a Miércoles:** Un pago pendiente se confirma. El universo premia tu orden.")
    st.markdown("🏡 **Jueves a Domingo:** Limpia tu espacio personal para atraer la energía de mayo.")

with t3:
    st.markdown("<p class='highlight-camino'>♊ ♎ ♒ EL CAMINO DE LA VERDAD</p>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    col_a.metric("ESTADO", "Elocuencia")
    col_b.metric("DÍA CLAVE", "Sábado")
    st.write("---")
    st.markdown("🗣️ **Lunes a Miércoles:** Mercurio te da la palabra justa. Habla hoy, no lo dejes pasar.")
    st.markdown("
