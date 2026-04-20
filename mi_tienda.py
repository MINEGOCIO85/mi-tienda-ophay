import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Ophay Tarot | Arte y Mística", page_icon="✨")

# 2. CSS (Diseño Premium)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    .stApp { background-color: #080808; color: #e0e0e0; }
    .gold {
        background: linear-gradient(to right, #BF953F, #FCF6BA, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Cinzel', serif; font-weight: bold; font-size: 45px; text-align: center;
        letter-spacing: 5px; margin-bottom: 0px;
    }
    .prod { color: #F7E7CE; font-family: 'Cinzel', serif; font-size: 26px; letter-spacing: 1px; margin-bottom: 10px; }
    .desc { font-style: italic; color: #b0b0b0; line-height: 1.6; font-size: 15px; }
    
    /* Botones personalizados */
    div.stButton > button {
        background: linear-gradient(135deg, #BF953F, #AA771C) !important;
        color: black !important; font-family: 'Cinzel', serif !important;
        font-weight: bold !important; width: 100%;
        border-radius: 0px !important; border: none !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        filter: brightness(1.2);
        box-shadow: 0px 0px 15px rgba(191, 149, 63, 0.5);
    }
    img { border: 1px solid rgba(191, 149, 63, 0.3); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<p class="gold">OPHAY TAROT</p>', unsafe_allow_html=True)
st.markdown("<center style='color:#666; letter-spacing:3px; font-size:12px;'>ANTIGUOS MISTERIOS PARA TIEMPOS MODERNOS</center><br>", unsafe_allow_html=True)

# 4. FUNCIÓN RENDER CON BOTÓN PERSONALIZADO
def item(img, titulo, precio, info, texto_boton):
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image(img, use_container_width=True)
    with col2:
        st.markdown(f'<p class="prod">{titulo}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="desc">{info}</p>', unsafe_allow_html=True)
        st.markdown(f'<h3 style="color:#D4AF37; margin-bottom:15px;">{precio} €</h3>', unsafe_allow_html=True)
        # El botón ahora recibe un texto diferente para cada producto
        st.link_button(texto_boton, "https://wa.me/34600000000")
    st.markdown("<hr style='border:0.1px solid #333; margin: 30px 0;'>", unsafe_allow_html=True)

# 5. RUTA BASE
url = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main"

# 6. PRODUCTOS CON IDENTIDAD PROPIA

# -- Producto 1
info1 = """
Sumérgete en una sesión de clarividencia profunda donde las cartas actúan como un espejo de tu alma. 
No solo desvelamos el futuro, exploramos los hilos invisibles que tejen tu presente para que 
puedas tomar decisiones con la fuerza del conocimiento ancestral.
"""
item(f"{url}/primera%20foto%20isoterica.png", 
     "ORÁCULO DEL DESTINO", 
     "25", 
     info1, 
     "RESERVAR MI SESIÓN")

# -- Producto 2
info2 = """
Más que un mazo, es una herramienta de poder. Esta edición Rider Luxe presenta acabados 
dorados que resuenan con la energía solar. Cada arcano ha sido diseñado para facilitar 
la intuición, convirtiéndose en el compañero perfecto tanto para maestros como para iniciados.
"""
item(f"{url}/SEGUNDA%20FOTO%20ESOTERICA.png", 
     "MAZO RIDER LUXE", 
     "45", 
     info2, 
     "ADQUIRIR EL MAZO")

# -- Producto 3
info3 = """
Extraída del corazón de la tierra y purificada bajo el influjo de la Luna Llena. 
Esta amatista sagrada es una poderosa aliada para la transmutación energética, 
limpiando el aura y aportando serenidad a tu espacio de meditación o descanso.
"""
item(f"{url}/amatista.png", 
     "AMATISTA SAGRADA", 
     "15", 
     info3, 
     "RECLAMAR MI PIEDRA")

# 7. PIE
st.markdown("<br><center style='color:#333; font-size:12px; letter-spacing:10px;'>OPHAY • MMXXVI</center>", unsafe_allow_html=True)
