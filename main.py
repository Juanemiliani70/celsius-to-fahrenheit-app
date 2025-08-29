import streamlit as st
from PIL import Image

st.markdown("# Aplicación Web para convertir de Grados °C a °F ")


image = Image.open("img/img_temperatura.jpg")
new_image = image.resize((200, 200))
st.image(new_image)

centigrados = st.number_input(
    "Ingresar temperatura en grados centígrados °C:",
    step=1,
    format="%d"
)

fahrenheit = (centigrados * 1.8) + 32


st.write(f"{centigrados} grados centígrados son: {fahrenheit:.2f} grados Fahrenheit")
