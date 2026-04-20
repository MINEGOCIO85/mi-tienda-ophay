import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ophay Tarot", layout="centered")

# ESTILO LUXURY VERTICAL
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    
    /* Títulos Principales */
    h1 { 
        color: #d4af37 !important; 
        text-align: center; 
        font-family: 'serif'; 
        letter-spacing: 5px;
        font-size: 2.5rem !important;
        margin-bottom: 0px;
    }
    
    .subtitulo {
        color: #d4af37;
        text-align: center;
        letter-spacing: 3px;
        font-size: 0.8rem;
        margin-bottom: 40px;
        opacity: 0.7;
    }

    /* Contenedor de Producto */
    .producto-container {
        text-align: center;
        margin-bottom: 60px;
        border-bottom: 1px solid #1a1a1a;
        padding-bottom: 40px;
    }

    .nombre-producto {
        color: #d4af37;
        font-family: 'serif';
        font-size: 1.8rem;
        letter-spacing: 2px;
        margin-top: 20px;
    }

    .precio {
        color: #ffffff;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .descripcion {
        color: #888888;
        font-style: italic;
        font-size: 1rem;
        max-width: 300px;
        margin: 0 auto 25px auto;
        line-height: 1.5;
    }

    /* Botón tipo "Apple" o Marca de Lujo */
    .stButton>button {
        background-color: transparent !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
        border-radius: 0px !important; /* Cuadrado es más serio y elegante */
        width: 250px;
        height: 50px;
        font-weight: lighter !important;
        letter-spacing: 2px;
        transition: all 0.4s;
    }
    
    .stButton>button:hover {
        background-color: #d4af37 !important;
        color: #000000 !important;
    }

    /* Ajustar imágenes */
    [data-testid="stImage"] img {
        border-radius: 5px;
        filter: grayscale(20%); /* Un toque más artístico */
    }
    </style>
    """, unsafe_allow_html=True)

# CABECERA
st.markdown("<h1>OPHAY</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo'>ALTA CLARIVIDENCIA • BARCELONA</p>", unsafe_allow_html=True)

user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base_url = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# --- PRODUCTO 1 ---
st.image(f"{base_url}/primera%20foto%20isoterica.png", use_container_width=True)
st.markdown("<div class='nombre-producto'>ORÁCULO DEL DESTINO</div>", unsafe_allow_html=True)
st.markdown("<div class='precio'>25 €</div>", unsafe_allow_html=True)
st.markdown("<div class='descripcion'>Desvela los hilos invisibles de tu camino. Una inmersión profunda en tu energía personal.</div>", unsafe_allow_html=True)
st.link_button("AGENDAR SESIÓN", "https://wa.me/34684668398")
st.markdown("<br><br>", unsafe_allow_html=True)

# --- PRODUCTO 2 ---
st.image(f"{base_url}/SEGUNDA%20FOTO%20ESOTERICA.png", use_container_width=True)
st.markdown("<div class='nombre-producto'>MAZO RIDER LUXE</div>", unsafe_allow_html=True)
st.markdown("<div class='precio'>45 €</div>", unsafe_allow_html=True)
st.markdown("<div class='descripcion'>Edición sagrada para conectar con tu intuición a través de un arte sublime.</div>", unsafe_allow_html=True)
st.link_button("ADQUIRIR PIEZA", "https://wa.me/34684668398")
st.markdown("<br><br>", unsafe_allow_html=True)

# --- PRODUCTO 3 ---
st.image(f"{base_url}/Amatista.png", use_container_width=True)
st.markdown("<div class='nombre-producto'>AMATISTA SAGRADA</div>", unsafe_allow_html=True)
st.markdown("<div class='precio'>15 €</div>", unsafe_allow_html=True)
st.markdown("<div class='descripcion'>Gema de transmutación purificada bajo el influjo lunar para protección.</div>", unsafe_allow_html=True)
st.link_button("SOLICITAR", "https://wa.me/34684668398")

# PIE DE PÁGINA
st.markdown("<br><br><p style='text-align: center; color: #333; letter-spacing: 5px;'>MMXXVI</p><br>", unsafe_allow_html=True)
