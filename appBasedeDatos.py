import streamlit as st
import base64
import os

st.set_page_config(page_title="Academias UEPDC", layout="wide")

def get_img_as_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

def inyectar_css():
    st.markdown("""
        <style>
            /* Ocultar elementos por defecto de Streamlit */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}

            /* Ajustar el contenedor principal */
            .block-container {
                padding-top: 1rem; /* Esto sube el Header (antes tenía mucho espacio) */
                padding-bottom: 0rem;
            }
        </style>
    """, unsafe_allow_html=True)

inyectar_css()

st.switch_page("pages/1_inicio.py")