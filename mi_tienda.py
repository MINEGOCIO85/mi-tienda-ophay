import streamlit as st

st.set_page_config(page_title="Ophay VIP", page_icon="🛍️")

st.title("🚀 MI NUEVA TIENDA OPHAY")
st.markdown("### Catálogo Completo")
st.write("---")

# PRODUCTO 1: DRON (Ahora arriba para forzar la carga)
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://cdn.pixabay.com/photo/2015/12/07/14/18/drone-1080844_640.jpg", caption="Dron Explorer")
with col2:
    st.subheader("1. Dron Explorer - 250€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 2: SMARTWATCH
col3, col4 = st.columns([1, 2])
with col3:
    st.image("https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", caption="Smartwatch Ultra")
with col4:
    st.subheader("2. Smartwatch Ultra - 45€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 3: PROYECTOR
col5, col6 = st.columns([1, 2])
with col5:
    st.image("https://images.unsplash.com/photo-1543269664-56d93c1b41a6?w=400", caption="Proyector 4K")
with col6:
    st.subheader("3. Proyector 4K - 150€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000")

st.write("---")

# PRODUCTO 4: AURICULARES
col7, col8 = st.columns([1, 2])
with col7:
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400", caption="Auriculares Gamer")
with col8:
    st.subheader("4. Auriculares Gamer - 35€")
    st.link_button("💬 PEDIR POR WHATSAPP", "https://wa.me/34600000000")

st.write("---")
st.info("📦 Envíos rápidos y pago seguro.")
