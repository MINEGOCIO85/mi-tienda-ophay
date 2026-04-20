import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="OPHAY", layout="wide")

# 2. CSS DE ALTA CONEXIÓN VISUAL
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;400;600&display=swap');

.main,[data-testid="stAppViewContainer"]{ background-color: #050505; }

/* Títulos con brillo metálico */
.titulo-joya {
    font-family: 'Cinzel';
    color: #f1c40f;
    text-shadow: 0px 0px 10px rgba(241, 196, 15, 0.3);
    font-weight: 900;
    text-align: center;
    margin-bottom: 0px;
}

/* Descripción con foco visual */
.foco-texto {
    color: #ffffff;
    font-family: 'Montserrat';
    font-size: 0.95rem;
    text-align: center;
    line-height: 1.6;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
}

/* Etiquetas de categoría */
.tag-plata {
    color: #bdc3c7;
    font-family: 'Montserrat';
    font-size: 0.65rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-align: center;
    display: block;
    margin-bottom: 10px;
}

/* Ajuste de imágenes */
[data-testid="stImage"] img {
    border-radius: 10px;
    border: 1px solid rgba(241, 196, 15, 0.2);
}
</style>
""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="titulo-joya" style="font-size:4rem;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p class="tag-plata" style="color:#f1c40f;">Barcelona Private Boutique</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 4. PRODUCTOS CON CONEXIÓN VISUAL
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

c1, c2, c3 = st.columns(3)

with c1:
    st.image(B + "primera%20foto%20isoterica.png")
    st.markdown('<span class="tag-plata">Servicio Exclusivo</span>', unsafe_allow_html=True)
    st.markdown('<h2 class="titulo-joya">ORÁCULO</h2>', unsafe_allow_html=True)
    st.markdown('<div class="foco-texto">Descubra los secretos de su destino con una consulta privada de alta precisión. Sabiduría ancestral para tiempos modernos.</div>', unsafe_allow_html=True)
    st.link_button("AGENDAR SESIÓN", f"{W}Cita_Oraculo")

with c2:
    st.image(B + "SEGUNDA%20FOTO%20ESOTERICA.png")
    st.markdown('<span class="tag-plata">Edición Coleccionista</span>', unsafe_allow_html=True)
    st.markdown('<h2 class="titulo-joya">RIDER LUXE</h2>', unsafe_allow_html=True)
    st.markdown('<div class="foco-texto">El mazo definitivo. Acabados en oro y tacto aterciopelado para una conexión superior con el arte del Tarot.</div>', unsafe_allow_html=True)
    st.link_button("ADQUIRIR AHORA", f"{W}Rider_Gold")

with c3:
    st.image(B + "Amatista.png")
    st.markdown('<span class="tag-plata">Piedra Sagrada</span>', unsafe_allow_html=True)
    st.markdown('<h2 class="titulo-joya">AMATISTA</h2>', unsafe_allow_html=True)
    st.markdown('<div class="foco-texto">Geoda seleccionada a mano por su pureza vibracional. El amuleto definitivo para proteger su santuario personal.</div>', unsafe_allow_html=True)
    st.link_button("SOLICITAR PIEZA", f"{W}Amatista_Luxe")

# 5. DIVISOR DORADO ELEGANTE
st.markdown("<hr style='border: 0; height: 1px; background: linear-gradient(90deg, transparent, #f1c40f, transparent); margin: 50px 0;'>", unsafe_allow_html=True)

# 6. BIENESTAR (DISEÑO MÁS LIMPIO)
st.markdown('<h2 class="titulo-joya">ALQUIMIA DE BIENESTAR</h2>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

r1, r2, r3 = st.columns(3)
with r1:
    st.markdown('<p class="titulo-joya" style="font-size:1.2rem;">🌿 LIMPIEZA</p>', unsafe_allow_html=True)
    st.markdown('<p class="foco-texto" style="font-size:0.8rem;">Queme tres hojas de laurel seco. Limpie su aura y su hogar de sombras del pasado.</p>', unsafe_allow_html=True)

with r2:
    st.markdown('<p class="titulo-joya" style="font-size:1.2rem;">🧂 PROTECCIÓN</p>', unsafe_allow_html=True)
    st.markdown('<p class="foco-texto" style="font-size:0.8rem;">Vaso de cristal, sal marina y 9 días de congelación para neutralizar envidias.</p>', unsafe_allow_html=True)

with r3:
    st.markdown('<p class="titulo-joya" style="font-size:1.2rem;">✨ ABUNDANCIA</p>', unsafe_allow_html=True)
    st.markdown('<p class="foco-texto" style="font-size:0.8rem;">Canela en polvo en el umbral. Deje que el flujo del dinero entre en su vida cada mes.</p>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#333; font-family:Montserrat; font-size:0.6rem;'>© MMXXVI OPHAY BOUTIQUE BARCELONA</p>", unsafe_allow_html=True)
