import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="RAJJ - Cinema",
    page_icon="⭐",
)

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")

st.title("Bienvenue au cinéma RAJJ - Élu meilleur cinéma de la Creuse")

st.image('https://t4.ftcdn.net/jpg/04/46/93/93/360_F_446939375_83iP0UYTg5F9vHl6icZwgrEBHXeXMVaU.jpg', caption='Vous ne savez pas quoi regarder ?')

st.write("Merci d'utiliser notre menu de gauche pour accéder aux diverses pages de notre site.")
st.sidebar.success("Faites votre choix pour naviguer sur le site. ☝️ ")
