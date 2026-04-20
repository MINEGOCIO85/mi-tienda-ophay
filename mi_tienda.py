import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY Elite Boutique", layout="wide")

# 2. CSS: ORO, PLATA Y TIPOGRAFÍA DE LUJO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400;900&display=swap');
    
    .main { background-color: #050505; }
    [data-testid="stAppViewContainer"] { background-color: #050505; }
    
    .oro-main {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; text-align: center;
    }

    .oro-destaque {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(to right, #bf953f, #fcf6ba, #aa8232);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; text-align: center;
        letter-spacing: 15px; font-size: 0.9rem;
        text-transform: uppercase; margin-top: -10px; margin-bottom: 40px;
    }
    
    .desc-lujo {
        font-family: 'Montserrat', sans-serif;
        color: #888;
        font-size: 0.85rem;
        text-align: center;
        line-height: 1.6;
        padding: 0 10px;
        font-style: italic;
    }

    .plata-fuerte {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(145deg, #fff 0%, #aaa 50%, #eee 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 900; font-size: 1.5rem; text-transform: uppercase;
    }

    .box {
        background-color: #000; border: 1px solid #222;
        padding: 25px; border-radius: 20px; border-left: 6px solid #d4af37;
    }
    .precio { color: #d4af37; font-weight: bold; font-size: 1.3rem; text-align: center; margin-top: 5px;}
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro-main" style="font-size:4.5rem; margin-bottom:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="oro-destaque">BARCELONA PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. TIENDA CON DESCRIPCIONES DE LUJO
u, r = "MINEGOCIO85", "mi-tienda-ophay"
b = f"https://raw.githubusercontent.com/{u}/{r}/main"

c1, c2, c3 = st.columns(3)

with c1:
    st.image(f"{b}/primera%20foto%20isoterica.png")
    st.markdown('<p class="oro-main" style="font-size:1.4rem; margin-bottom:5px;">ORÁCULO MÍSTICO</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-lujo">Canaliza la sabiduría ancestral con este oráculo de edición limitada. Cartas con acabado seda diseñadas para revelar los secretos del hilo del destino.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">25€</p>', unsafe_allow_html=True)

with c2:
    st.image(f"{b}/SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<p class="oro-main" style="font-size:1.4rem; margin-bottom:5px;">TAROT RIDER LUXE</p>', unsafe_allow_html=True)
    st.markdown('<p class="desc-lujo">La excelencia del Tarot Rider-Waite elevada al lujo. Bordes metalizados en oro y estuche de terciopelo para lecturas de alta vibración.</p>', unsafe_allow_html=True)
    st.markdown('<p class="precio">45€</p>', unsafe_allow_html=True)

with c3:
    st.image(f"{b}/Amatista.png")
    st.markdown('<p class="
