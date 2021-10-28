import streamlit as st
from PIL import Image
from webcam import webcam

from src.demo import detect_age_gender

captured_image = webcam()
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    img = detect_age_gender(captured_image)
    img = Image.fromarray(img)
    st.image(img)
