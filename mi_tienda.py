import streamlit as st

# 1. AJUSTES TÉCNICOS
st.set_page_config(page_title="OPHAY | Boutique & Destino", layout="wide")

# 2. ESTILO VISUAL (Gris Oxford y Dorado)
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #eee; }
    [data-testid="stAppViewContainer"] { background-color: #0d0d0d; }
    .logo-text {
        font-family: serif; text-align: center; font-size: 3.2rem; letter-spacing: 12px;
        background: linear-gradient(145deg, #fff, #d4af37, #aa8a2e);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: bold; margin: 0;
    }
    .card {
        background: rgba(255,255,255,0.03); border: 1px solid rgba(212,175,55,0.2);
        padding: 20px; border-radius: 15px; text-align: center;
    }
    .stTabs [data-baseweb="tab"] { color: #666 !important; font-weight: bold; }
    .stTabs [aria-selected="true"] { color: #d4af37 !important; border-bottom-color: #d4af37 !important; }
    .stButton>button {
        background-color: #d4af37 !important; color: #000 !important;
        border-radius: 20px !important; font-weight: bold !important; width: 100%;
    }
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

# 5. HORÓSCOPO SEMANAL (ESTRUCTURA DE SEGURIDAD)
st.markdown("---")
st.markdown("<h2 style='text-align:center;color:#d4af37;font-family:serif;'>✨ EL CAMINO DE LA SEMANA ✨</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#aaa;'>📅 Semana del 20 al 26 de Abril, 2026</p>", unsafe_allow_html=True)

t_fuego, t_tierra, t_aire, t_agua = st.tabs(["🔥 FUEGO", "🌱 TIERRA", "💨 AIRE", "💧 AGUA"])

with t_fuego:
    st.subheader("Aries, Leo, Sagitario")
    st.write("**EL CAMINO DE LA ACCIÓN**")
    st.info("Lunes a Miércoles: Energía de Marte. Cierra tratos pronto. El domingo recibirás una señal clave.")

with t_tierra:
    st.subheader("Tauro, Virgo, Capricornio")
    st.write("**EL CAMINO DE LA COSECHA**")
    st.success("Lunes a Miércoles: Orden financiero. Un pago se confirma. El orden atraerá abundancia.")

with t_aire:
    st.subheader("Géminis, Libra, Acuario")
    st.write("**EL CAMINO DE LA VERDAD**")
    st.write("Lunes a Miércoles: Mercurio te da elocuencia. Habla hoy. Alguien trae una propuesta chula.")

with t_agua:
    st.subheader("Cáncer, Escorpio, Piscis")
    st.write("**EL CAMINO DEL INSTINTO**")
    st.warning("Lunes a Miércoles: Sueños vívidos. Escucha tu voz. Usa tu Amatista para protegerte.")

st.markdown("<br><p style='text-align:center;color:#444;font-size:0.7rem;'>© MMXXVI OPHAY COLLECTION • BARCELONA</p>", unsafe_allow_html=True)
