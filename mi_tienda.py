import streamlit as st

# 1. AJUSTES DE PÁGINA
st.set_page_config(page_title="OPHAY | Boutique", layout="wide")

# 2. ESTILO CSS "GOLD & DARK"
st.markdown("""
    <style>
    .main { background-color: #0a0a0a; color: #eee; }
    [data-testid="stAppViewContainer"] { background-color: #0a0a0a; }
    .logo {
        font-family: serif; text-align: center; font-size: 3.5rem; letter-spacing: 12px;
        background: linear-gradient(145deg, #fff, #d4af37, #aa8a2e);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; margin: 0;
    }
    .card {
        background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.2);
        padding: 20px; border-radius: 15px; text-align: center;
    }
    .camino-header {
        color: #d4af37; font-size: 1.4rem; font-weight: bold; 
        letter-spacing: 2px; border-bottom: 1px solid #333; padding-bottom: 5px;
    }
    .stTabs [data-baseweb="tab"] { color: #888 !important; font-size: 1.1rem !important; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; border-bottom-color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="logo">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#d4af37;letter-spacing:5px;font-size:0.7rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

# 4. TIENDA
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

# 5. HORÓSCOPO SEMANAL (FORMATO TARJETA)
st.markdown("<br><hr style='border-color:#222;'><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#d4af37;font-family:serif;'>✨ EL CAMINO DE LA SEMANA ✨</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#666;'>20 al 26 de Abril, 2026</p>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t1:
    st.markdown('<p class="camino-header">EL CAMINO DE LA ACCIÓN</p>', unsafe_allow_html=True)
    st.markdown("### Aries • Leo • Sagitario")
    st.success("**DÍA CLAVE: MIÉRCOLES**")
    st.write("🌑 **Lunes-Miércoles:** La energía de Marte te impulsa. Cierra tratos ahora.")
    st.write("🌕 **Jueves-Domingo:** Recibirás una señal clara sobre un tema laboral.")

with t2:
    st.markdown('<p class="camino-header">EL CAMINO DE LA COSECHA</p>', unsafe_allow_html=True)
    st.markdown("### Tauro • Virgo • Capricornio")
    st.success("**DÍA CLAVE: MARTES**")
    st.write("💰 **Lunes-Miércoles:** Momento de recibir frutos. Un pago se confirma.")
    st.write("🏡 **Jueves-Domingo:** Limpia tu espacio para atraer abundancia en mayo.")

with t3:
    st.markdown('<p class="camino-header">EL CAMINO DE LA VERDAD</p>', unsafe_allow_html=True)
    st.markdown("### Géminis • Libra • Acuario")
    st.success("**DÍA CLAVE: SÁBADO**")
    st.write("🗣️ **Lunes-Miércoles:** Mercurio te da elocuencia. Expr
