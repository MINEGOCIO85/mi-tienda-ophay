import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY Boutique", layout="wide")

# 2. CSS DE LUJO
st.markdown("""
    <style>
    .main { background-color: #0a0a0a; color: #eee; }
    [data-testid="stAppViewContainer"] { background-color: #0a0a0a; }
    .logo {
        font-family: serif; text-align: center; font-size: 3rem; letter-spacing: 10px;
        background: linear-gradient(145deg, #fff, #d4af37, #aa8a2e);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; margin: 0;
    }
    .card {
        background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.2);
        padding: 15px; border-radius: 15px; text-align: center;
    }
    .title-h { color: #d4af37; font-size: 1.2rem; font-weight: bold; letter-spacing: 1px; }
    .stTabs [data-baseweb="tab"] { color: #666 !important; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; border-bottom-color: #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="logo">OPHAY</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#d4af37;letter-spacing:4px;font-size:0.7rem;'>BARCELONA • PRIVATE BOUTIQUE</p>", unsafe_allow_html=True)

# 4. TIENDA
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p style="color:#d4af37;margin-top:10px;">ORÁCULO<br>25€</p>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p style="color:#d4af37;margin-top:10px;">RIDER LUXE<br>45€</p>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(f"{b}/Amatista.png")
    st.markdown('<p style="color:#d4af37;margin-top:10px;">AMATISTA<br>15€</p>', unsafe_allow_html=True)
    st.link_button("COMPRAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. HORÓSCOPO (DISEÑO BLINDADO)
st.markdown("<br><hr style='border-color:#222;'><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:#d4af37;font-family:serif;'>✨ EL CAMINO DE LA SEMANA ✨</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#666;'>20 al 26 de Abril, 2026</p>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t1:
    st.markdown('<p class="title-h">EL CAMINO DE LA ACCIÓN</p>', unsafe_allow_html=True)
    st.info("**Aries, Leo, Sagitario**")
    st.write("✨ **Lunes-Miércoles:** Marte te impulsa. Cierra tratos.")
    st.write("✨ **Jueves-Domingo:** Una señal clara llega pronto.")

with t2:
    st.markdown('<p class="title-h">EL CAMINO DE LA COSECHA</p>', unsafe_allow_html=True)
    st.info("**Tauro, Virgo, Capricornio**")
    st.write("✨ **Lunes-Miércoles:** Frutos económicos. Pago confirmado.")
    st.write("✨ **Jueves-Domingo:** Limpia tu hogar y atrae abundancia.")

with t3:
    st.markdown('<p class="title-h">EL CAMINO DE LA VERDAD</p>', unsafe_allow_html=True)
    st.info("**Géminis, Libra, Acuario**")
    st.write("✨ **Lunes-Miércoles:** Mercurio te da elocuencia. Habla.")
    st.write("✨ **Jueves-Domingo:** Encuentro clave con alguien nuevo.")

with t4:
    st.markdown('<p class="title-h">EL CAMINO DEL INSTINTO</p>', unsafe_allow_html=True)
    st.info("**Cáncer, Escorpio, Piscis**")
    st.write("✨ **Lunes-Miércoles:** Sueños vívidos. Escucha tu interior.")
    st.write("✨ **Jueves-Domingo:** Usa tu Amatista. Filtra energías.")

st.markdown("<br><p style='text-align:center;color:#333;font-size:0.7rem;'>© MMXXVI OPHAY COLLECTION • BARCELONA</p>", unsafe_allow_html=True)
