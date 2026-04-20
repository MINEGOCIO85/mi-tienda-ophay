import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO DE LUJO (Oro y Noche)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    .stApp { background-color: #050505; color: #ffffff; }
    .gold-text {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif; font-weight: 700;
    }
    .header-box { text-align: center; padding: 40px 0; border-bottom: 1px solid rgba(191, 149, 63, 0.4); margin-bottom: 40px; }
    .gold-title { font-size: 50px; letter-spacing: 15px; margin: 0; }
    .product-title { font-family: 'Cinzel', serif; color: #F7E7CE; font-size: 26px; margin-top: 10px; }
    
    div.stButton > button {
        background: linear-gradient(135deg, #BF953F 0%, #FCF6BA 50%, #AA771C 100%) !important;
        color: #0a0a0c !important;
        font-family: 'Cinzel', serif !important; font-weight: bold !important;
        border: none !important; border-radius: 0px !important; width: 100%; padding: 15px;
    }
    img { border: 1px solid rgba(191, 149, 63, 0.3); border-radius: 4px; box-shadow: 0px 10px 20px rgba(0,0,0,0.8); }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<div class="header-box"><p class="gold-text gold-title">OPHAY TAROT</p></div>', unsafe_allow_html=True)

# 4. FUNCIÓN RENDERIZADO
def draw_item(url_img, name, price, desc):
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.image(url_img, use_container_width=True)
    with c2:
        st.markdown(f'<p class="product-title">{name}</p>', unsafe_allow_html=True)
        st.write(f"_{desc}_")
        st.markdown(f'<p style="color:#D4AF37; font-size:24px; font-weight:bold;">{price} €</p>', unsafe_allow_html=True)
        st.link_button("RESERVAR", "https://wa.me/34600000000")
    st.write("<br><hr style='border:0.1px solid rgba(191,149,63,0.2)'><br>", unsafe_allow_html=True)

# 5. LISTADO CON ENLACES DIRECTOS (Sustituye 'MINEGOCIO85' si tu usuario es otro)
user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# Aquí usamos %20 para que los espacios en blanco no rompan el link
draw_item(f"{base}/primera%20foto%20isoterica.png", "LECTURA DEL DESTINO", "25", "Sesión profunda para desvelar tu futuro.")
draw_item(f"{base}/SEGUNDA%20FOTO%20ESOTERICA.png", "MAZO RIDER LUXE", "45", "Edición premium con detalles oro.")
draw_item(f"{base}/amatista.jpg", "AMATISTA SAGRADA", "15", "Energía pura bajo la luna llena.")

# 6. PIE DE PÁGINA
st.markdown("<center><p style='color:#333; letter-spacing:10px; font-size:10px;'>OPHAY • MMXXVI</p></center>", unsafe_allow_html=True)
