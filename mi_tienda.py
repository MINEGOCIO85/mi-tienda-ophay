import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Catálogo Ophay", page_icon="🛍️", layout="centered")

# --- ESTILO PERSONALIZADO CON CSS ---
# Esto replica el diseño de la imagen: fondo gris, títulos negros, botones verdes.
st.markdown("""
    <style>
    /* Fondo de la página entero */
    .stApp {
        background-color: #f0f2f5;
    }
    
    /* Título principal 'OPHAY SILVER' */
    .title-ophay {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #000000;
        text-align: center;
        font-weight: 200; /* Letra fina y elegante */
        font-size: 50px !important;
        padding-bottom: 20px;
    }

    /* Subtítulo de descripción elegante */
    .subtitle-ophay {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #666666;
        text-align: center;
        font-weight: 300;
        font-size: 18px !important;
        margin-top: -20px;
        padding-bottom: 30px;
    }

    /* Nombres de productos y precios */
    h3 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 24px !important;
    }
    
    /* Descripción de productos */
    .product-desc {
        color: #333333;
        font-size: 16px;
        margin-bottom: 20px;
    }

    /* Estilo del botón verde de WhatsApp */
    div.stButton > button:first-child {
        background-color: #25D366; /* Verde WhatsApp */
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        width: 100%;
        transition: background-color 0.3s ease;
    }
    
    /* Efecto al pasar el ratón por encima del botón */
    div.stButton > button:first-child:hover {
        background-color: #128C7E; /* Verde más oscuro */
        border: none;
        color: white;
    }
    
    /* Separador horizontal sutil */
    hr {
        border: 0;
        height: 1px;
        background: #dddddd;
        margin-top: 40px;
        margin-bottom: 40px;
    }
    
    /* Marco para las fotos de producto */
    [data-testid="stImage"] img {
        border: 1px solid #eeeeee;
        border-radius: 5px;
        background-color: white;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<p class="title-ophay">OPHAY SILVER</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-ophay">Experience freedom with our exclusive collection</p>', unsafe_allow_html=True)
st.write("---")

# --- FUNCION PARA MOSTRAR PRODUCTOS (Para no repetir código) ---
def mostrar_producto(id_prod, imagen_url, nombre, precio, descripcion, url_wa):
    col1, col2 = st.columns([1.2, 2]) # Columna de imagen y columna de texto
    
    with col1:
        # Mostramos la imagen del producto
        st.image(imagen_url, use_column_width=True)
        
    with col2:
        # Nombre y precio en negrita
        st.subheader(f"{id_prod}. {nombre} - {precio}")
        
        # Descripción del producto
        st.markdown(f'<p class="product-desc">{descripcion}</p>', unsafe_allow_html=True)
        
        # Botón de WhatsApp (con icono 💬 integrado)
        st.link_button(f"💬 PEDIR POR WHATSAPP", url_wa)

# --- LISTADO DE PRODUCTOS (Replicando la imagen) ---

# 1. DRON EXPLORER
mostrar_producto(
    id_prod="1",
    imagen_url="https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=400",
    nombre="Dron Explorer",
    precio="250€",
    descripcion="Experience freedom with this cinematic drone, designed for stunning aerial photography.",
    url_wa="https://wa.me/34600000000?text=Hola,quiero+informacion+sobre+el+Dron+Explorer"
)

# 2. SMARTWATCH ULTRA
mostrar_producto(
    id_prod="2",
    imagen_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
    nombre="Smartwatch Ultra",
    precio="45€",
    descripcion="Stay connected and track your fitness with this rugged and stylish smartwatch.",
    url_wa="https://wa.me/34600000000?text=Hola,quiero+informacion+sobre+el+Smartwatch+Ultra"
)

# Puedes añadir más productos aquí siguiendo el mismo formato.

st.write("---")
st.caption("OPHAY SILVER © 2024 - Envíos rápidos y pago seguro.")
