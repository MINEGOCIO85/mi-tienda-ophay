import streamlit as st

# 1. Configuración de la página - Toque minimalista
st.set_page_config(page_title="Ophay Luxury Boutique", page_icon="⚖️", layout="centered")

# 2. ESTILO: MINIMALISMO DE LUJO TOTAL
st.markdown("""
    <style>
    /* Importamos fuentes elegantes de Google */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@200;400;600&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

    /* Fondo Blanco Roto Premium */
    .stApp {
        background-color: #fdfdfd;
    }
    
    /* Título principal ORO con fuente Cinzel (Estilo joyería) */
    .title-gold {
        font-family: 'Cinzel', serif !important;
        background: linear-gradient(to right, #B38728, #D4AF37, #AA771C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 400;
        font-size: 48px !important;
        letter-spacing: 10px; /* Mayor espaciado */
        margin-top: 50px;
        margin-bottom: 0px;
    }

    /* Subtítulo de lujo discreto */
    .subtitle-luxury {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        text-align: center;
        letter-spacing: 4px;
        font-size: 11px;
        text-transform: uppercase;
        margin-top: 15px;
        margin-bottom: 60px;
    }

    /* Títulos de productos - Sans Serif Fina y Mayúsculas */
    h3 {
        font-family: 'Inter', sans-serif !important;
        color: #0f172a !important; 
        font-weight: 600 !important;
        letter-spacing: 2px;
        font-size: 18px !important;
        text-transform: uppercase;
        margin-bottom: 15px !important;
    }
    
    /* Descripción del producto - Playfair Display Cursiva (Estilo revista) */
    .desc {
        font-family: 'Playfair Display', serif !important;
        color: #64748b !important;
        font-size: 14px !important;
        font-style: italic;
        line-height: 1.9; /* Más aire entre líneas */
        font-weight: 300;
        margin-bottom: 25px !important;
    }

    /* Precio - Sans Serif Fina */
    .precio {
        font-family: 'Inter', sans-serif !important;
        color: #0f172a !important; 
        font-weight: 400;
        font-size: 20px;
        letter-spacing: 1px;
        margin-bottom: 30px !important;
    }
    
    /* EL BOTÓN "QUIET LUXURY": BLANCO Y NEGRO, BORDES RECTOS */
    div.stButton > button {
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-family: 'Inter', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        font-weight: 400;
        font-size: 12px;
        border-radius: 0px; /* Bordes rectos obligatorios */
        border: 1px solid #e2e8f0 !important;
        padding: 22px;
        width: 100%;
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: none;
    }
    
    /* Efecto al pasar el ratón: Inversión total de color */
    div.stButton > button:hover {
        background-color: #0f172a !important;
        color: #ffffff !important;
        border-color: #0f172a !important;
        letter-spacing: 6px; /* Se expande suavemente */
    }

    /* Contenedor de producto con mucho "aire" y línea separadora fina */
    [data-testid="stHorizontalBlock"] {
        padding: 60px 0px; /* Mucho más espacio vertical */
        border-bottom: 1px solid #f1f5f9;
    }

    /* Estilo para las fotos de producto */
    img {
        border-radius: 0px; /* Sin bordes redondeados */
        filter: grayscale(10%); /* Un toque más artístico */
        transition: all 0.8s ease;
    }

    /* Efecto al pasar el ratón por la imagen */
    img:hover {
        filter: grayscale(0%);
        transform: scale(1.03);
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<p class="title-gold">OPHAY</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-luxury">Silver & Gold Collection</p>', unsafe_allow_html=True)

# --- FUNCIÓN PARA MOSTRAR PRODUCTOS ---
def item(img, nombre, precio, texto, link):
    c1, c2 = st.columns([1, 1.3]) # Proporción para que la imagen no sea gigante
    with c1:
        st.image(img, use_column_width=True)
    with c2:
        st.subheader(nombre)
        st.markdown(f'<p class="desc">{texto}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="precio">{precio}€</p>', unsafe_allow_html=True)
        # El botón de WhatsApp elegante
        st.link_button(f"Consultar Disponibilidad", link)

# --- LISTADO DE PRODUCTOS CON NUEVAS FOTOS MÁS ELEGANTES ---

# 1. AURICULARES GAMER (Ahora con foto Premium)
item("https://images.unsplash.com/photo-1599669454699-248893623440?w=600&q=80", 
     "AURICULARES GAMER ULTRA", "35", 
     "Un santuario de sonido. Pureza acústica superior envuelta en materiales de alta resistencia y confort incomparable.", 
     "https://wa.me/34600000000")

# 2. DRON EXPLORER (Foto lateral elegante)
item("https://images.unsplash.com/photo-1521714161819-15534968fc5f?w=600&q=80", 
     "DRON EXPLORER CINEMATIC", "250", 
     "Una pieza de ingeniería diseñada para aquellos que buscan capturar la esencia del horizonte desde una perspectiva privilegiada.", 
     "https://wa.me/34600000000")

# 3. SMARTWATCH ULTRA (Foto con esfera minimalista)
item("https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=600&q=80", 
     "SMARTWATCH ULTRA PLATINUM", "45", 
     "La sofisticación técnica se encuentra con un diseño atemporal, creando el compañero perfecto para el estilo de vida contemporáneo.", 
     "https://wa.me/34600000000")

# 4. PROYECTOR 4K (Foto limpia y moderna)
item("https://images.unsplash.com/photo-1601053163359-99433433364f?w=600&q=80", 
     "PROYECTOR 4K CINEMA", "150", 
     "Redefina su concepto de cine en casa. Nitidez absoluta y colores vibrantes en una arquitectura minimalista.", 
     "https://wa.me/34600000000")

# --- PIE DE PÁGINA DISCRETO ---
st.markdown("<br><br><center><p style='color:#cbd5e1; font-family:Inter,sans-serif; letter-spacing:3px; font-size:10px;'>OPHAY LUXURY • ESTADO: ONLINE / DISPONIBLE</p></center>", unsafe_allow_html=True)
