import streamlit as st
from PIL import Image
import numpy as np
import rembg
from io import BytesIO

# Streamlit Interface
st.title("ClearCut: Background Eraser")

# Background Removal Section
st.header("Remove Background from Image")

uploaded_image = st.file_uploader("Upload an image for background removal:", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.write("Removing background...")
    input_image = Image.open(uploaded_image)
    img_np = np.array(input_image)

    # Use rembg to remove the background
    img_no_bg = rembg.remove(img_np)
    img_no_bg_pil = Image.fromarray(img_no_bg)

    st.image(img_no_bg_pil, caption='Image with Background Removed', use_column_width=True)

    img_byte_arr = BytesIO()
    img_no_bg_pil.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    st.download_button(
        label="Download Image without Background",
        data=img_byte_arr,
        file_name="image_no_bg.png",
        mime="image/png"
    )
