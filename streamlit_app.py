import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.set_page_config(
    page_title="Cinema RAJJ",
    page_icon="👋",
)

st.title("Bienvenue au cinéma RAJJ - Élu meilleur cinéma de la Creuse")

st.image('https://t4.ftcdn.net/jpg/04/46/93/93/360_F_446939375_83iP0UYTg5F9vHl6icZwgrEBHXeXMVaU.jpg', caption='Vous ne savez pas quoi regarder ?')

st.write("Merci d'utiliser notre menu de gauche pour accéder aux diverses pages de notre site, merci")
st.sidebar.success("Menu.")
