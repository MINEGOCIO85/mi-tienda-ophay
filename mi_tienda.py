import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", page_icon="✨", layout="centered")

# 2. ESTILO DE LUJO (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Quicksand:wght@300;400&display=swap');
    
    .stApp { background-color: #080808; color: #e0e0e0; font-family: 'Quicksand', sans-serif; }
    
    .gold-text {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif;
        font-weight: 700;
    }
    
    .header-box { text-align: center; padding: 40px 0; border-bottom: 1px solid rgba(191, 149, 63, 0.2); margin-bottom: 40px; }
    .gold-title { font-size: 50px; letter-spacing: 10px; margin: 0; }
    
    .product-title { 
        font-family: 'Cinzel', serif; 
        color: #F7E7CE; 
        font-size: 26px; 
        margin-bottom: 5px;
    }
    
    div.stButton > button {
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%) !important;
        color: #000000 !important;
        font-family: 'Cinzel', serif !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 4px !important;
        width: 100%;
        padding: 12px;
    }
    
    img { 
        border: 1px solid rgba(191, 149, 63, 0.3); 
        border-radius: 8px; 
        box-shadow: 0px 10px 30px rgba(0,0,0,0.7);
    }

    hr { border: 0; height: 1px; background: linear-gradient(to right, transparent, #BF953F, transparent); margin: 30px 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<div class="header-box"><p class="gold-text gold-title">OPHAY TAROT</p></div>', unsafe_allow_html=True)

# 4. FUNCIÓN RENDERIZADO
def draw_item(url_img, name, price, desc):
    col1, col2 = st.columns([1, 1.1])
    with col1:
        st.image(url_img, use_container_width=True)
    with col2:
        st.markdown(f'<p class="product-title">{name}</p>', unsafe_allow_html=True)
        st.write(f"*{desc}*")
        st.markdown(f'<p style="color:#D4AF37; font-size:24px; font-weight:bold;">{price} €</p>', unsafe_allow_html=True)
        st.link_button(f"RESERVAR", "https://wa.me/34600000000")
    st.markdown("<hr>", unsafe_allow_html=True)

# 5. CONFIGURACIÓN DE RUTAS
user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base = f"https://raw.githubusercontent.com/{user}/{repo}/main"

# 6. PRODUCTOS
draw_item(f"{base}/primera%20foto%20isoterica.png", "LECTURA DEL DESTINO", "25", "Ses
