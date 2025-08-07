import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from utils import load_default_image, add_noise, upload_image
from wavelet_core import denoise_image_wavelet

st.set_page_config(page_title="Wavelet Image Denoising", layout="wide")

st.title("🧼 Wavelet-Based Image Denoising App")
st.write("Upload a grayscale image or use the default Cameraman image. Gaussian noise will be added, then denoised using wavelet thresholding.")

# Sidebar controls
wavelet = st.sidebar.selectbox("Wavelet Type", ["haar", "db1", "db2", "sym4", "coif1"])
level = st.sidebar.slider("Decomposition Level", 1, 4, 2)
noise_var = st.sidebar.slider("Noise Variance (σ²)", 0.001, 0.1, 0.01, step=0.001)

# Image upload
uploaded = st.file_uploader("Upload a grayscale image (PNG or JPG)", type=["png", "jpg", "jpeg"])
if uploaded:
    img = upload_image(uploaded)
else:
    img = load_default_image()

# Process image
noisy_img = add_noise(img, var=noise_var)
denoised_img = denoise_image_wavelet(noisy_img, wavelet=wavelet, level=level)

# Display
col1, col2, col3 = st.columns(3)
col1.image(img, caption="Original", use_container_width=True, clamp=True)
col2.image(noisy_img, caption="Noisy", use_container_width=True, clamp=True)
col3.image(np.clip(denoised_img, 0, 1), caption="Denoised", use_container_width=True, clamp=True)
