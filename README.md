---
title: Wavelet Denoising of Images - Streamlit GUI
emoji: 🌊
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.28.0
app_file: app.py
pinned: false
license: mit
---

# 🌊 Wavelet Denoising of Images - Streamlit GUI

This app allows you to interactively denoise images using wavelet transform.

### Features
- Use default Cameraman image or upload your own
- Add Gaussian noise with adjustable variance
- Denoise using wavelet thresholding
- Choose wavelet type and decomposition level
- View results side-by-side

### Run Locally
```bash
streamlit run app.py

# 📷 Wavelet Denoising of Images – Streamlit GUI

This app allows you to interactively denoise images using wavelet transform.

### Features
- Use default Cameraman image or upload your own
- Add Gaussian noise with adjustable variance
- Denoise using wavelet thresholding
- Choose wavelet type and decomposition level
- View results side-by-side

### Run Locally

```bash
uv add matplotlib>=3.10.5",
    "numpy>=2.3.2",
    "pywavelets>=1.9.0",
    "scikit-image>=0.25.2",
    "streamlit>=1.48.0",
streamlit run app.py
