import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Ophay Tarot | Boutique Mística", page_icon="✨", layout="centered")

# 2. ESTILO DE LUJO REFINADO (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Quicksand:wght@300;400&display=swap');
    
    .stApp { background-color: #080808; color: #e0e0e0; font-family: 'Quicksand', sans-serif; }
    
    /* Título con gradiente metálico y resplandor */
    .gold-text {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #B38728, #FBF5B7, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif;
        font-weight: 700;
        text-shadow: 0px 0px 15px rgba(191, 149, 63, 0.3);
    }
    
    .header-box { text-align: center; padding: 60px 0; border-bottom: 1px solid rgba(191, 149, 63, 0.2); margin-bottom: 50px; }
    .gold-title { font-size: 55px; letter-spacing: 12px; margin: 0; }
    
    /* Títulos de productos */
    .product-title { 
        font-family: 'Cinzel', serif; 
        color: #F7E7CE; 
        font-size: 28px; 
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    
    /* Botones de Reserva Estilo Premium */
    div.stButton > button {
        background: linear-gradient(135deg, #BF953F 0%, #AA771C 100%) !important;
        color: #000000 !important;
        font-family: 'Cinzel', serif !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 4px !important;
        width: 100%;
        padding: 12px;
        transition: all 0.3s ease;
        letter-spacing: 1px;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 5px 15px rgba(191, 149, 63, 0.4) !important;
        background: linear-gradient(135deg, #FCF6BA 0%, #BF953F 100%) !important;
    }

    /* Estilo de imágenes */
    img { 
        border: 1px solid rgba(191, 149, 63, 0.4); 
        border-radius: 8px; 
        box-shadow: 0px 15px 35px rgba(0,0,0,0.9);
        transition: transform 0.3s ease;
    }
    img:hover { transform: scale(1.02); }

    hr { border: 0; height: 1px; background: linear-gradient(to right, transparent, #BF953F, transparent); margin: 40px 0; }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<div class="header-box"><p class="gold-text gold-title">OPHAY TAROT</p><p style="color:#888; letter-spacing:5px; font-size:12px; margin-top:10px;">MAGIA • DESTINO • ENERGÍA</p></div>', unsafe_allow_html=True)

# 4. FUNCIÓN RENDERIZADO MEJORADA
def draw_item(url_img, name, price, desc):
    col1, col2 = st.columns([1, 1.1], gap="large")
    with col1:
        st.image(url_img, use_container_width=True)
    with col2:
        st.markdown(f'<p class="product-title">{name}</p>', unsafe_allow_html=True)
        st.write(f"*{desc}*")
        st.markdown(f'<p style="color:#D4AF37; font-size:26px; font-weight:bold; margin: 15px 0;">{price} €</p>', unsafe_allow_html=True)
        st.link_button(f"SOLICITAR {name}", "https://wa.me/34600000000") # Pon aquí tu número real
    st.markdown("<hr>", unsafe_allow_html=True)

# 5. LISTADO DE PRODUCTOS (Configurado según tus archivos de GitHub)
user = "MINEGOCIO85"
repo = "mi-tienda-ophay"
base = f"https://raw.githubusercontent.com/{user}/{repo}/main"

draw_item(f"{base}/primera%20foto%20isoterica.png", "LECTURA DEL DESTINO", "25", "Una sesión profunda y clarificadora para desvelar los hilos ocultos de tu camino futuro.")
draw_item(f"{base}/SEGUNDA%20FOTO%20ESOTERICA.png", "MAZO RIDER LUXE", "45", "Mazo de Tarot edición premium con acabados artísticos y simbología sagrada reforzada.")
draw_item(f"{base}/amatista.png", "AMATISTA SAGRADA", "15", "Piedra de transmutación cargada bajo la luz de la luna llena para armonizar tu espacio.")

# 6. PIE DE PÁGINA
st.markdown("""
    <br><br>
    <center>
        <p style='color:#555; letter-spacing
