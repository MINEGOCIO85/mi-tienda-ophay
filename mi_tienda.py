import streamlit as st

# 1. SETTINGS
st.set_page_config(page_title="Ophay Tarot", page_icon="✨")

# 2. CSS (Diseño Oro)
st.markdown("""
<style>
    .stApp { background-color: #080808; color: #e0e0e0; }
    .gold {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: serif; font-weight: bold; font-size: 40px; text-align: center;
    }
    .prod { color: #F7E7CE; font-family: serif; font-size: 24px; }
    div.stButton > button {
        background: linear-gradient(#BF953F, #AA771C) !important;
        color: black !important; font-weight: bold !important; width: 100%;
    }
    img { border: 1px solid #BF953F; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# 3. LOGO
st.markdown('<p class="gold">OPHAY TAROT</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 4. FUNCIÓN RENDER
def item(img, titulo, precio, info):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(img, use_container_width=True)
    with col2:
        st.markdown(f'<p class="prod">{titulo}</p>', unsafe_allow_html=True)
        st.write(info)
        st.subheader(f"{precio} €")
        st.link_button("RESERVAR", "https://wa.me/34600000000")
    st.divider()

# 5. RUTA BASE
url = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main"

# 6. PRODUCTOS (Líneas ultra-cortas para evitar cortes)
item(f"{url}/primera%20foto%20isoterica.png", 
     "LECTURA DESTINO", "25", 
     "Sesión para ver tu futuro.")

item(f"{url}/SEGUNDA%20FOTO%20ESOTERICA.png", 
     "MAZO RIDER", "45", 
     "Mazo premium detalles oro.")

item(f"{url}/amatista.png", 
     "AMATISTA LUNA", "15", 
     "Energía y transmutación.")

# 7. PIE
st.center = st.markdown("<center>OPHAY • 2026</center>", unsafe_allow_html=True)
