import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="OPHAY ELITE | Barcelona", layout="wide")

# 2. CSS LUXURY TOP
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;600;900&display=swap');

/* Fondo Base */
.main { background-color: #000; color: #fff; }
[data-testid="stAppViewContainer"] { background-color: #000; }

/* Oro Boutique */
.oro-text {
    font-family: 'Cinzel', serif;
    background: linear-gradient(180deg, #bf953f 0%, #fcf6ba 50%, #aa8232 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
    text-align: center;
}

/* Plata Líquida */
.plata-text {
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 1.8rem;
    background: linear-gradient(90deg, #888, #fff, #888);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: uppercase;
    letter-spacing: -1px;
}

/* Tarjetas de Producto Luxury */
.luxury-card {
    background: rgba(10, 10, 10, 0.8);
    border: 1px solid #222;
    padding: 35px;
    border-radius: 2px;
    text-align: center;
    transition: all 0.5s ease;
    min-height: 600px;
}
.luxury-card:hover {
    border-color: #bf953f;
    box-shadow: 0px 0px 30px rgba(191, 149, 63, 0.15);
    transform: translateY(-5px);
}

/* Botón VIP */
.vip-button {
    display: block;
    background: transparent;
    color: #bf953f !important;
    border: 1px solid #bf953f;
    padding: 15px;
    text-decoration: none;
    font-family: 'Montserrat';
    font-weight: 600;
    font-size: 0.75rem;
    letter-spacing: 3px;
    transition: all 0.3s;
    margin-top: 20px;
    text-transform: uppercase;
}
.vip-button:hover {
    background: #bf953f;
    color: #000 !important;
}

.sub-header {
    color: #d4af37;
    text-align: center;
    letter-spacing: 12px;
    font-weight: 300;
    font-size: 0.7rem;
    margin-bottom: 60px;
    font-family: 'Montserrat';
}
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro-text" style="font-size:7rem; margin-bottom:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. PRODUCTOS
u, r = "MINEGOCIO85", "mi-tienda-ophay"
base_url = "https://raw.githubusercontent.com/" + u + "/" + r + "/main/"
cols = st.columns(3)

items = [
    {
        "tit": "ORÁCULO",
        "desc": "CANALIZACIÓN PRIVADA DE 45 MINUTOS. CLARIDAD TOTAL SOBRE TU DESTINO Y DESBLOQUEO DE CAMINOS ESPIRITUALES.",
