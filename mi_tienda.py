import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay", layout="centered")

# ESTILO "BOUTIQUE MINIMAL"
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    
    /* Título minimalista */
    h1 { 
        color: #d4af37 !important; 
        text-align: center; 
        font-family: 'serif'; 
        letter-spacing: 8px;
        font-size: 1.5rem !important;
        font-weight: 100;
        margin-top: 50px;
    }
    
    /* Imágenes pequeñas y centradas */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        padding: 20px 0;
    }
    [data-testid="stImage"] img {
        border: 1px solid #1a1a1a;
    }

    /* Textos finos */
    .nombre-item {
        color: #ffffff;
        text-align: center;
        font-family: 'serif';
        font-size: 0.9rem;
        letter-spacing: 3px;
        margin-bottom: 5px;
    }

    .precio-item {
        color: #d4af37;
        text-align: center;
        font-size: 0.8rem;
        letter-spacing: 1px;
        margin-bottom: 20px;
    }

    /* Botón Minimalista (Solo borde) */
    .stButton>button {
        background-color: transparent !important;
        color: #ffffff !important;
        border: 0.5px solid #333333 !important;
        border-radius: 0px !important;
        width: 180px;
        height: 35px;
        font-size: 0.7rem !important;
        letter-spacing: 2px;
        margin: 0 auto;
        display: block;
        transition: all 0.6s;
    }
    
    .stButton>button:hover {
        border-color: #d4af37 !important;
        color: #d4af37 !important;
    }

    hr { border-top: 1px solid #111; margin: 40px 0; }
    </style>
    """, unsafe_allow_html=True)

# LOGO
st.markdown("<h1>OPHAY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444; font-size: 0.6rem; letter-spacing: 4px; margin-bottom: 60px;'>BARCELONA</p>", unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# PRODUCTO 1
st.image(f"{base_url}/primera%20foto%20isoterica.png", width=180)
st.markdown("<div class='nombre-item'>ORÁCULO</div>", unsafe_allow_html=True)
st.markdown("<div class='precio-item'>25.00€</div>", unsafe_allow_html=True)
st.link_button("RESERVAR", "https://wa.me/34684668398")

st.markdown("<hr>", unsafe_allow_html=True)

# PRODUCTO 2
st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", width=180)
st.markdown("<div class='nombre-item'>RIDER LUXE</div>", unsafe_allow_html=True)
st.markdown("<div class='precio-item'>45.00€</div>", unsafe_allow_html=True)
st.link_button("ADQUIRIR", "https://wa.me/34684668398")

st.markdown("<hr>", unsafe_allow_html=True)

# PRODUCTO 3
st.image(f"{base_url}/Amatista.png", width=180)
st.markdown("<div class='nombre-item'>AMATISTA</div>", unsafe_allow_html=True)
st.markdown("<div class='precio-item'>15.00€</div>", unsafe_allow_html=True)
st.link_button("SOLICITAR", "https://wa.me/34684668398")

# FINAL
st.markdown("<br><br><p style='text-align: center; color: #222; font-size: 0.5rem; letter-spacing: 3px;'>PRIVATE BOUTIQUE</p><br>", unsafe_allow_html=True)
