import streamlit as st
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Ophay Tarot", page_icon="🌙", layout="centered")

# 2. ESTILO ORO METÁLICO (CSS)
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

# 4. FUNCIÓN PARA DIBUJAR PRODUCTOS
def draw_item(img_path, name, price, desc):
    c1, c2 = st.columns([1, 1.2])
    with c1:
        # Intentamos cargar la imagen. Si falla el nombre con espacios, probamos variantes.
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        elif os.path.exists("Amatista.jpg"):
            st.image("Amatista.jpg", use_container_width=True)
        else:
            st.warning("Cargando energía...") # Mensaje místico mientras conecta
            
    with c2:
        st.markdown(f'<p class="product-title">{name}</p>', unsafe_allow_html=True)
        st.write(f"_{desc}_")
        st.markdown(f'<p style="color:#D4AF37; font-size:24px; font-weight:bold;">{price} €</p>', unsafe_allow_html=True)
        st.link_button("RESERVAR", "https://wa.me/34600000000")
    st.write("<br><hr style='border:0.1px solid rgba(191,149,63,0.2)'><br>", unsafe_allow_html=True)

# 5. LISTADO DE PRODUCTOS (Nombres de archivos exactos)
draw_item("primera foto isoterica.png", "LECTURA DEL DESTINO", "25", "Sesión profunda para desvelar tus hilos.")
draw_item("SEGUNDA FOTO ESOTERICA.jpg", "MAZO RIDER LUXE", "45", "Edición premium con detalles en oro.")
draw_item("3 FOTO ESOTERICA.jpg", "AMATISTA SAGRADA", "15", "Piedra de poder bajo la luna llena.")

# 6. FOOTER
st.markdown("<center><p style='color:#333; letter-spacing:10px; font-size:10px;'>OPHAY • MMXXVI</p></center>", unsafe_allow_html=True)
