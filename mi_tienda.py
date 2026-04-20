import streamlit as st

# 1. SETUP
st.set_page_config(page_title="OPHAY ELITE | BCN", layout="wide")

# 2. CSS LUXURY REFINADO
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Montserrat:wght@300;600;900&display=swap');
.main {background-color:#000;}
[data-testid="stAppViewContainer"] {background-color:#000;}
.oro {font-family:'Cinzel'; background:linear-gradient(180deg,#bf953f,#fcf6ba,#aa8232); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:900; text-align:center;}
.plata {font-family:'Montserrat'; font-weight:900; font-size:1.4rem; background:linear-gradient(to bottom,#fff,#999,#fff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-transform:uppercase; text-align:center; letter-spacing:1px;}
.card {background:#050505; border:1px solid #1a1a1a; padding:30px; border-top:3px solid #d4af37; text-align:center; min-height:520px; border-radius:4px;}
.desc {color:#999; font-family:'Montserrat'; font-size:0.85rem; line-height:1.6; margin:20px 0; font-weight:300;}
.btn {display:block; border:1px solid #bf953f; color:#bf953f!important; padding:12px; font-weight:900; text-decoration:none; border-radius:2px; font-size:0.75rem; letter-spacing:3px; text-transform:uppercase; transition:0.4s;}
.btn:hover {background:#bf953f; color:#000!important;}
.h-d {color:#d4af37; font-size:0.9rem; letter-spacing:6px; font-weight:900; margin-top:25px; text-align:center; font-family:'Montserrat';}
</style>""", unsafe_allow_html=True)

# 3. CABECERA
st.markdown('<h1 class="oro" style="font-size:5rem;margin:0;">OPHAY</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#d4af37;text-align:center;letter-spacing:15px;font-weight:900;font-size:0.7rem;margin-bottom:60px;">BARCELONA • PRIVATE BOUTIQUE</p>', unsafe_allow_html=True)

# 4. VARIABLES
B = "https://raw.githubusercontent.com/MINEGOCIO85/mi-tienda-ophay/main/"
W = "https://wa.me/34684668398?text="

# 5. TIENDA
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('<div class="card">', unsafe_
