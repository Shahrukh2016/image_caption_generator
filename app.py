from transformers import pipeline
import streamlit as st
from PIL import Image
import time

# Image to text function
def img2txt(image):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(image)[0]["generated_text"]
    return text

# Streamlit app
st.markdown("<h1 style = 'text-align:center'> Image Caption Generator </h1>", unsafe_allow_html=True)
img = st.file_uploader(label="Please upload image:", type=["jpg", "jpeg", "png"], accept_multiple_files=False)
if img:
    # Display progress bar
    progress_bar = st.progress(0)
    for i in range(10):
        time.sleep(0.1)  # Simulate time-consuming task
        progress_bar.progress(i * 10 + 10)

    img_ = Image.open(img)
    st.image(img_)
    caption = img2txt(img_)
    progress_bar.progress(100)  # Ensure the progress bar is filled at the end

    st.markdown(f"<h3 style = 'text-align:center'> Image caption: {caption} </h3>", unsafe_allow_html=True)
