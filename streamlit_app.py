import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.set_page_config(
    page_title="RAJJ - Cinema",
    page_icon="⭐",
)

st.title("Bienvenue au cinéma RAJJ - Élu meilleur cinéma de la Creuse")

st.image('https://t4.ftcdn.net/jpg/04/46/93/93/360_F_446939375_83iP0UYTg5F9vHl6icZwgrEBHXeXMVaU.jpg', caption='Vous ne savez pas quoi regarder ?')

st.write("Merci d'utiliser notre menu de gauche pour accéder aux diverses pages de notre site.")
st.sidebar.success("Faites votre choix pour naviguer sur le site. ☝️ ")
