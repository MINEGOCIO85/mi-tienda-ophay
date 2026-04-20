import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot | Boutique & Horóscopo", layout="wide")

# ESTILO LUXE VIBRANTE + SECCIÓN HORÓSCOPO
st.markdown("""
    <style>
    .main { background-color: #050505; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    .logo-main {
        background: linear-gradient(to bottom, #fcf6ba 0%, #d4af37 40%, #aa8a2e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        letter-spacing: 10px;
        font-family: 'serif';
        text-align: center;
        font-weight: bold;
        margin: 0;
    }

    .product-card {
        background: #0a0a0a;
        border: 1px solid #221d14;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0px 0px 15px rgba(212,175,55,0.1);
        margin-bottom: 20px;
    }
    
    .horoscopo-header {
        color: #d4af37;
        font-family: 'serif';
        text-align: center;
        font-size: 2rem;
        letter-spacing: 5px;
        margin-top: 50px;
    }

    .horoscopo-texto {
        background: #111;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #d4af37;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #e0e0e0;
    }

    .stButton>button {
        background: linear-gradient(145deg, #d4af37, #b8962e) !important;
        color: #000000 !important;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        border: none !important;
        width: 100%;
        height: 45px;
    }
    
    [data-testid="stImage"] img { border-radius: 5px; border: 1px solid #332b1a; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<div style="text-align:center; padding: 30px 0;"><h1 class="logo-main">OPHAY</h1><p style="color:#d4af37; letter-spacing:5px; font-size:0.8rem; opacity:0.7;">ALTA CLARIVIDENCIA • BARCELONA</p></div>', unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# --- SECCIÓN TIENDA ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/primera%20foto%20isoterica.png", width=200)
    st.markdown('<div style="color:#d4af37; font-size:1.1rem; font-family:serif; margin-top:10px;">ORÁCULO</div><div style="color:white; margin-bottom:15px;">25 €</div>', unsafe_allow_html=True)
    st.link_button("RESERVAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=200)
    st.markdown('<div style="color:#d4af37; font-size:1.1rem; font-family:serif; margin-top:10px;">RIDER LUXE</div><div style="color:white; margin-bottom:15px;">45 €</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(f"{base_url}/Amatista.png", width=200)
    st.markdown('<div style="color:#d4af37; font-size:1.1rem; font-family:serif; margin-top:10px;">AMATISTA</div><div style="color:white; margin-bottom:15px;">15 €</div>', unsafe_allow_html=True)
    st.link_button("COMPRAR", "https://wa.me/34684668398")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN HORÓSCOPO SEMANAL ---
st.markdown("---")
st.markdown('<h2 class="horoscopo-header">✨ TU DESTINO SEMANAL ✨</h2>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>Consulta tu signo gratis. Actualizado por Ophay.</p>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["FUEGO", "TIERRA", "AIRE", "AGUA"])

with tab1: # Aries, Leo, Sagitario
    st.markdown("**Aries (♈):** Esta semana vas a fuego. No dejes que nadie apague tu brillo, pero ojo con las discusiones tontas.")
    st.markdown("**Leo (♌):** Eres el centro de atención. El universo te debe una, y te la va a pagar estos días.")
    st.markdown("**Sagitario (♐):** Una aventura inesperada llama a tu puerta. Di que sí, no seas aburrido/a.")

with tab2: # Tauro, Virgo, Capricornio
    st.markdown("**Tauro (♉):** El dinero se mueve. Revisa bien esos gastos, pero date un capricho pequeño.")
    st.markdown("**Virgo (♍):** Orden en la mente, orden en la vida. Alguien del pasado vuelve, tú decides si abres.")
    st.markdown("**Capricornio (♑):** Tu esfuerzo por fin se nota. Respira, que vas por el buen camino.")

with tab3: # Géminis, Libra, Acuario
    st.markdown("**Géminis (♊):** Tu lengua es un arma esta semana. Úsala para seducir, no para herir.")
    st.markdown("**Libra (♎):** El equilibrio llega tras la tormenta. Una noticia familiar te dará paz.")
    st.markdown("**Acuario (♒):** Tu creatividad está por las nubes. Es el momento de ese proyecto loco.")

with tab4: # Cáncer, Escorpio, Piscis
    st.markdown("**Cáncer (♋):** Saca los pañuelos, pero de alegría. Una reconciliación está muy cerca.")
    st.markdown("**Escorpio (♏):** Tu magnetismo es brutal hoy. Vas a conseguir lo que te propongas.")
    st.markdown("**Piscis (♓):** Escucha tus sueños. Tu intuición está más afilada que nunca, no la ignores.")

st.markdown("<br><p style='text-align:center; color:#444; font-size:0.7rem; letter-spacing:3px;'>PRIVATE COLLECTION • BARCELONA</p>", unsafe_allow_html=True)
