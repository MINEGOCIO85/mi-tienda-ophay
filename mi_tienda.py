import streamlit as st

st.set_page_config(page_title="Ophay VIP", page_icon="🛍️")

st.title("🚀 MI NUEVA TIENDA OPHAY")
st.markdown("### Selecciona tu producto y contacta por WhatsApp")
st.write("---")

# PRODUCTO 1: Smartwatch
col1, col2 = st.columns([1, 2])
with col1:
    # Foto de Smartwatch
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", caption="Smartwatch Ultra")
with col2:
    st.subheader("1. Smartwatch Ultra - 45€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000?text=Hola,quiero+el+Smartwatch")

st.write("---")

# PRODUCTO 2: Proyector
col3, col4 = st.columns([1, 2])
with col3:
    # Foto de Proyector/Cine
    st.image("https://images.unsplash.com/photo-1517604412417-af03037501ed?w=400", caption="Proyector 4K")
with col4:
    st.subheader("2. Proyector 4K - 150€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000?text=Hola,quiero+el+Proyector")

st.write("---")

# PRODUCTO 3: Dron
col5, col6 = st.columns([1, 2])
with col5:
    # Foto de Dron
    st.image("https://images.unsplash.com/photo-1524143924409-e7bd48a60004?w=400", caption="Dron Explorer")
with col6:
    st.subheader("3. Dron Explorer - 250€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000?text=Hola,quiero+el+Dron")

st.write("---")

# PRODUCTO 4: Auriculares
col7, col8 = st.columns([1, 2])
with col7:
    # Foto de Auriculares
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", caption="Auriculares Gamer")
with col8:
    st.subheader("4. Auriculares Gamer - 35€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000?text=Hola,quiero+los+Auriculares")

st.write("---")
st.info("📦 Envíos rápidos y pago seguro.")
