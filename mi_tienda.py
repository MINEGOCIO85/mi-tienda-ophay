import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury Silver", page_icon="🥈")

# 2. ESTILO (Manteniendo el lujo Silver & Gold)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,700;1,300&family=Playfair+Display:wght@700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    h1 {
        font-family: 'Playfair Display', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        font-size: 55px !important;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #0f172a !important; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .desc {
        font-family: 'Montserrat', sans-serif !important;
        color: #64748b !important;
        font-size: 14px !important;
        font-style: italic;
        line-height: 1.4;
    }

    .precio {
        font-family: 'Montserrat', sans-serif !important;
        color: #1e293b !important;
        font-weight: 700;
        font-size: 18px;
    }
    
    /* Botón Dorado VIP con ajuste para el icono */
    div.stButton > button {
        background: linear-gradient(to bottom, #D4AF37 0%, #B38728 100%);
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
        border-radius: 4px;
        border: none;
        padding: 12px;
        width: 100%;
        transition: 0.4s;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    div.stButton > button:hover {
        background: #25D366; /* Color verde WhatsApp al pasar el ratón */
        color: white !important;
        transform: scale(1.02);
    }

    img {
        border-radius: 4px;
        box-shadow: 5px 5px 20px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("OPHAY SILVER")
st.write("---")

# --- FUNCION PARA MOSTRAR PRODUCTO ---
def mostrar_producto(imagen, titulo, descripcion, precio, link_wa):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(imagen)
    with col2:
        st.subheader(titulo)
        st.markdown(f'<p class="desc">{descripcion}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="precio">{precio}€</p>', unsafe_allow_html=True)
        # Añadimos el icono de WhatsApp directamente en el texto del botón
        st.link_button(f"💬 ADQUIRIR POR WHATSAPP", link_wa)
    st.write("---")

# LISTA DE PRODUCTOS
mostrar_producto(
    "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400",
    "Dron Explorer",
    "Libertad absoluta en el aire con captura de imagen cinematográfica de alta precisión.",
    "250",
    "https://wa.me/34600000000?text=Hola,quiero+el+Dron"
)

mostrar_producto(
    "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
    "Smartwatch Ultra",
    "La perfecta armonía entre el diseño vanguardista y el control total de tu bienestar diario.",
    "45",
    "https://wa.me/34600000000?text=Hola,quiero+el+Smartwatch"
)

mostrar_producto(
    "https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400",
    "Proyector 4K",
    "Transforma cualquier espacio en una experiencia visual inmersiva con nitidez incomparable.",
    "150",
    "https://wa.me/34600000000?text=Hola,quiero+el+Proyector"
)

mostrar_producto(
    "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
    "Auriculares Gamer",
    "Pureza acústica y confort premium diseñados para las sesiones más exigentes.",
    "35",
    "https://wa.me/34600000000?text=Hola,quiero+los+Auriculares"
)

st.caption("OPHAY LUXURY © 2026 - EXCLUSIVE SELECTION")
