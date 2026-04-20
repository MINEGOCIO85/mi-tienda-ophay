import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY ELITE", layout="wide")

# 2. ESTILO DE ALTA COSTURA
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;700&display=swap');

.main,[data-testid="stAppViewContainer"]{
    background-color: #0a0a0a;
}

/* Titulares en Oro Real */
.titulo-luxe {
    font-family: 'Cinzel';
    background: linear-gradient(180deg, #d4af37 0%, #fcf6ba 50%, #aa8232 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
    text-align: center;
    margin-bottom: 5px;
    letter-spacing: 2px;
}

/* Descripciones en Blanco Nítido */
.desc-luxe {
    color: #ffffff;
    font-family: 'Montserrat';
    font-size: 0.85rem;
    text-align: center;
    line-height: 1.6;
    padding: 0 10px;
    margin-bottom: 20px;
}

/* Tarjetas de Cristal */
.card-boutique {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    height: 100%;
    transition: 0.3s;
}

.card-boutique:hover {
    border: 1px solid #d4af37;
    background: rgba(255, 255, 255, 0.05);
}

/* Botón Elegante */
.stButton>button {
    background: transparent !important;
    color: #d4af37 !important;
    border: 1px solid #d4af37 !important;
    width: 100%;
    font-family: 'Cinzel' !important;
    letter-spacing: 2px;
    font-weight: 700;
}
.stButton>button:hover {
    background: #d4af37 !important;
    color: #000 !important;
}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="titulo-luxe" style="font-size:4.5rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37; text-align:center; letter-spacing:12px; font-size:0.8rem; margin-top:-20px;">PRIVATE BOUTIQUE • BARCELONA</p>', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# 4. LAS JOYAS DE LA CORONA (PRODUCTOS)
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card-boutique">', unsafe_allow_html=True)
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<h2 class="titulo-luxe" style="font-size:1.8rem;">CONEXIÓN ANCESTRAL</h2>', unsafe_allow_html=True)
    st.markdown('<p class="desc-luxe">Acceda a la sabiduría del destino a través de nuestro Oráculo privado. Una sesión de clarividencia exclusiva diseñada para revelar los hilos invisibles de su futuro.</p>', unsafe_allow_html=True)
    st.link_button("SOLICITAR CITA PRIVADA", f"{W}Reserva_Oraculo")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card-boutique">', unsafe_allow_html=True)
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<h2 class="titulo-luxe" style="font-size:1.8rem;">RIDER LUXE GOLD</h2>', unsafe_allow_html=True)
    st.markdown('<p class="desc-luxe">La máxima expresión del Tarot. Una edición limitada con acabados artesanales para maestros y coleccionistas que buscan la excelencia en cada lectura.</p>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR OBRA MAESTRA", f"{W}Comprar_Rider_Luxe")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="card-boutique">', unsafe_allow_html=True)
    st.image(B + "Amatista.png")
    st.markdown('<h2 class="titulo-luxe" style="font-size:1.8rem;">AMATISTA SAGRADA</h2>', unsafe_allow_html=True)
    st.markdown('<p class="desc-luxe">Pieza única de transmutación energética. Seleccionada bajo criterios astrológicos para proteger su hogar y elevar la vibración de su santuario personal.</p>', unsafe_allow_html=True)
    st.link_button("RESERVAR PIEZA ÚNICA", f"{W}Info_Amatista")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. RESTO DE LA WEB (MANTENIENDO EL ESTILO)
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown('<h2 class="titulo-luxe" style="font-size:
