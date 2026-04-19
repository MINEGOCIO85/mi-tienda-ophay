import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Ophay Luxury Boutique", page_icon="⚖️")

# 2. ESTILO: MINIMALISMO DE LUJO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@200;400;600&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

    .stApp {
        background: #fdfdfd; /* Blanco roto premium */
    }
    
    /* Título ORO con fuente Cinzel (Estilo joyería) */
    .title-gold {
        font-family: 'Cinzel', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 400;
        font-size: 48px !important;
        letter-spacing: 8px;
        margin-top: 40px;
        margin-bottom: 0px;
    }

    .subtitle-luxury {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        text-align: center;
        letter-spacing: 3px;
        font-size: 12px;
        text-transform: uppercase;
        margin-top: 10px;
        margin-bottom: 50px;
    }

    h3 {
        font-family: 'Inter', sans-serif !important;
        color: #0f172a !important; 
        font-weight: 600 !important;
        letter-spacing: 1px;
        font-size: 18px !important;
    }
    
    .desc {
        font-family: 'Playfair Display', serif !important;
        color: #64748b !important;
        font-size: 14px !important;
        font-style: italic;
        line-height: 1.8;
        font-weight: 300;
    }

    .precio {
        font-family: 'Inter', sans-serif !important;
        color: #0f172a !important; 
        font-weight: 400;
        font-size: 20px;
        letter-spacing: 1px;
    }
    
    /* EL BOTÓN MÁS ELEGANTE: DISCRETO Y SOFISTICADO */
    div.stButton > button {
        background: #ffffff !important;
        color: #0f172a !important;
        font-family: 'Inter', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: 400;
        border-radius: 0px; /* Bordes rectos = Más lujo */
        border: 1px solid #e2e8f0 !important;
        padding: 20px;
        width: 100%;
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: none;
    }
    
    div.stButton > button:hover {
        background: #0f172a !important;
        color: #ffffff !important;
        border-color: #0f172a !important;
        letter-spacing: 5px; /* Se expande suavemente */
    }

    /* Contenedor de producto con mucho "aire" */
    [data-testid="stHorizontalBlock"] {
        padding: 40px 0px;
        border-bottom: 1px solid #f1f5f9;
    }

    img {
        filter: grayscale(20%); /* Un toque artístico */
        transition: all 0.8s ease;
    }

    img:hover {
        filter: grayscale(0%);
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# CABECERA
st.markdown('<p class="title-gold">OPHAY</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-luxury">Silver & Gold Collection</p>', unsafe_allow_html=True)

def item(img, nombre, precio, texto, link):
    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.image(img)
    with c2:
        st.subheader(nombre)
        st.markdown(f'<p class="desc">{texto}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="precio">{precio}€</p>', unsafe_allow_html=True)
        st.link_button(f"Consultar Disponibilidad", link)

# LISTADO DE PRODUCTOS
item("https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=600", 
     "DRON EXPLORER", "250", 
     "Una pieza de ingeniería diseñada para aquellos que buscan capturar la esencia del horizonte desde una perspectiva privilegiada.", 
     "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600", 
     "SMARTWATCH ULTRA", "45", 
     "La sofisticación técnica se encuentra con un diseño atemporal, creando el compañero perfecto para el estilo de vida contemporáneo.", 
     "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=600", 
     "PROYECTOR 4K", "150", 
     "Redefina su concepto de cine en casa. Nitidez absoluta y colores vibrantes en una arquitectura minimalista.", 
     "https://wa.me/34600000000")

item("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600", 
     "AURICULARES GAMER", "35", 
     "Un santuario de sonido. Pureza acústica superior envuelta en materiales de alta resistencia y confort.", 
     "https://wa.me/34600000000")

st.markdown("<br><center><p style='color:#cbd5e1; font-family:Inter; letter-spacing:2px; font-size:10px;'>ESTADO: ONLINE / DISPONIBLE</p></center>", unsafe_allow_html=True)
