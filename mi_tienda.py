import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury Boutique", page_icon="💎", layout="centered")

# 2. SISTEMA DE ESTILO "OPHAY LUXE"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@200;400;600&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

    .stApp {
        background-color: #ffffff;
    }
    
    .title-gold {
        font-family: 'Cinzel', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 400;
        font-size: 52px !important;
        letter-spacing: 12px;
        margin-top: 60px;
        margin-bottom: 5px;
    }

    .subtitle-luxury {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        text-align: center;
        letter-spacing: 5px;
        font-size: 10px;
        text-transform: uppercase;
        margin-bottom: 80px;
    }

    h3 {
        font-family: 'Inter', sans-serif !important;
        color: #111827 !important; 
        font-weight: 600 !important;
        letter-spacing: 2px;
        font-size: 16px !important;
        text-transform: uppercase;
        margin-bottom: 10px !important;
    }
    
    .desc {
        font-family: 'Playfair Display', serif !important;
        color: #4b5563 !important;
        font-size: 14px !important;
        font-style: italic;
        line-height: 2;
        font-weight: 300;
        margin-bottom: 20px !important;
    }

    .precio {
        font-family: 'Inter', sans-serif !important;
        color: #111827 !important; 
        font-weight: 400;
        font-size: 19px;
        letter-spacing: 1px;
        margin-bottom: 25px !important;
    }
    
    div.stButton > button {
        background-color: #ffffff !important;
        color: #111827 !important;
        font-family: 'Inter', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        font-weight: 400;
        font-size: 11px;
        border-radius: 0px !important;
        border: 1px solid #e5e7eb !important;
        padding: 20px 40px;
        width: 100%;
        transition: all 0.5s ease;
    }
    
    div.stButton > button:hover {
        background-color: #111827 !important;
        color: #ffffff !important;
        border-color: #111827 !important;
        letter-spacing: 6px;
    }

    [data-testid="stHorizontalBlock"] {
        padding: 80px 0px;
        border-bottom: 1px solid #f3f4f6;
    }

    img {
        transition: all 1s ease;
    }

    img:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="title-gold">OPHAY</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-luxury">Édition Limitée • Silver & Gold</p>', unsafe_allow_html=True)

def producto_lujo(img, nombre, precio, texto, link):
    c1, c2 = st.columns([1, 1.2]) 
    with c1:
        st.image(img, use_column_width=True)
    with c2:
        st.subheader(nombre)
        st.markdown(f'<p class="desc">{texto}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="precio">{precio} €</p>', unsafe_allow_html=True)
        st.link_button(f"SOLICITAR INFORMACIÓN", link)

# PRODUCTOS
producto_lujo(
    "https://images.unsplash.com/photo-1599669454699-248893623440?w=800&q=80", 
    "AURICULARES NOIRE PRESTIGE", 
    "35", 
    "Una oda a la pureza acústica. Ingeniería de precisión envuelta en materiales nobles para una experiencia inmersiva absoluta.", 
    "https://wa.me/34600000000"
)

producto_lujo(
    "https://images.unsplash.com/photo-1521714161819-15534968fc5f?w=800&q=80", 
    "DRON EXPLORER HORIZON", 
    "250", 
    "Capture la esencia del mundo desde una perspectiva privilegiada. El equilibrio perfecto entre aerodinámica y arte visual.", 
    "https://wa.me/34600000000"
)

producto_lujo(
    "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=800&q=80", 
    "SMARTWATCH PLATINUM CORE", 
    "45", 
    "La vanguardia tecnológica se fusiona con la relojería clásica. Un testamento de estilo para el coleccionista moderno.", 
    "https://wa.me/34600000000"
)

# NUEVA FOTO PARA EL PROYECTOR
producto_lujo(
    "https://images.unsplash.com/photo-1535016120720-40c646bebbbb?w=800&q=80", 
    "PROYECTOR LUMIÈRE 4K", 
    "150", 
    "Redefina su santuario privado. Nitidez cinematográfica y diseño minimalista para una inmersión sensorial sin precedentes.", 
    "https://wa.me/34600000000"
)

st.markdown("<br><br><center><p style='color:#94a3b8; font-family:Inter,sans-serif; letter-spacing:5px; font-size:9px;'>OPHAY LUXURY RETAIL • DISPONIBILIDAD EXCLUSIVA</p></center>", unsafe_allow_html=True)
