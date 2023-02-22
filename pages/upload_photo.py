import streamlit as st
from PIL import Image
# pillow is already installed when streamlit is installed
# Image is a class


def convert_display_photo(photo):
    img = Image.open(photo)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")  # "L" - is used to convert the photo in black&white
    # Render (display) the grayscale image
    st.image(gray_img)
    if gray_img:
        st.success("Image uploaded succesfully!")


st.write("You need to upload a photo.")

uploaded_photo = st.file_uploader("Upload a photo")
with st.expander("Choose to take a photo"):  # context manager
    # Start the camera
    camera_photo = st.camera_input("Camera")  # streamlit image type

if uploaded_photo:
    convert_display_photo(uploaded_photo)
elif camera_photo:
    convert_display_photo(camera_photo)