import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Bienvenue au cinéma RAJJ - Élu meilleur cinéma de la Creuse")

st.image('https://t4.ftcdn.net/jpg/04/46/93/93/360_F_446939375_83iP0UYTg5F9vHl6icZwgrEBHXeXMVaU.jpg', caption='Vous ne savez pas quoi regarder ?')

st.write("Merci d'utiliser notre menu de gauche pour accéder aux diverses pages de notre site, merci")
st.sidebar.success("Menu.")