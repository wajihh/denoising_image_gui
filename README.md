---
title: Wavelet Denoising of Images - Streamlit GUI
emoji: 🌊
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.48.0
app_file: app.py
pinned: false
license: mit
---

# 🌊 Wavelet Denoising of Images - Streamlit GUI

This interactive web application allows you to denoise images using advanced wavelet transform techniques. Perfect for demonstrating signal processing concepts and practical image enhancement.

## ✨ Features

- **🖼️ Flexible Image Input**: Use the default Cameraman image or upload your own grayscale images
- **🔊 Noise Simulation**: Add controllable Gaussian noise with adjustable variance for testing
- **🌊 Wavelet Denoising**: Remove noise using wavelet thresholding with multiple wavelet types
- **⚙️ Customizable Parameters**: Choose from different wavelet types (Haar, Daubechies, Symlets, Coiflets) and decomposition levels
- **📊 Quality Metrics**: Real-time MSE and PSNR calculations to measure denoising performance
- **💾 Download Results**: Save processed images directly from the browser
- **📈 Performance Analysis**: Visual comparison of original, noisy, and denoised images

## 🚀 How to Use

1. **Upload Image**: Click the upload button to select your own image, or use the default Cameraman image
2. **Adjust Parameters**: Use the sidebar to modify:
   - Wavelet type (different mathematical bases for decomposition)
   - Decomposition level (1-4 layers of wavelet transform)
   - Noise variance (amount of Gaussian noise to add)
3. **View Results**: Compare original, noisy, and denoised images side-by-side
4. **Analyze Quality**: Check the performance metrics (MSE improvement, PSNR, noise reduction)
5. **Download**: Save the denoised image or noisy version for further use

## 🛠️ Technical Details

### Wavelet Transform
This application uses PyWavelets library to perform discrete wavelet transforms for image denoising. The process involves:

1. **Decomposition**: Breaking down the image into wavelet coefficients at multiple scales
2. **Thresholding**: Removing small coefficients that likely represent noise
3. **Reconstruction**: Rebuilding the image from the cleaned coefficients

### Supported Wavelets
- **Haar**: Simple, good for images with sharp edges
- **Daubechies (db1, db2)**: Better frequency localization
- **Symlets (sym4)**: Nearly symmetric, good for general use
- **Coiflets (coif1)**: Balanced between smoothness and compactness

### Quality Metrics
- **MSE (Mean Squared Error)**: Lower values indicate better denoising
- **PSNR (Peak Signal-to-Noise Ratio)**: Higher values indicate better quality
- **Noise Reduction Percentage**: Shows how much noise was removed

## 🔧 Run Locally

### Prerequisites
- Python 3.8+
- UV package manager (recommended) or pip

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/wajihh/denoising_image_gui.git
cd denoising_image_gui

# Install dependencies with UV
uv add streamlit>=1.48.0
uv add numpy>=2.3.2
uv add pywavelets>=1.9.0
uv add scikit-image>=0.25.2
uv add matplotlib>=3.10.5
uv add pillow>=8.0.0

# Or install with pip
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
denoising_image_gui/
├── app.py              # Main Streamlit application
├── utils.py            # Image loading and preprocessing utilities
├── wavelet_core.py     # Core wavelet denoising algorithms
├── requirements.txt    # Python dependencies
├── pyproject.toml      # UV package configuration
└── README.md          # This file
```

## 🎯 Use Cases

- **Educational**: Demonstrate wavelet transforms and noise removal concepts
- **Research**: Quick prototyping of denoising algorithms
- **Practical**: Clean up noisy photographs or scanned documents
- **Comparison**: Test different wavelet types on your specific images
- **Analysis**: Quantitative evaluation of denoising performance

## 🔬 Algorithm Background

Wavelet denoising works by exploiting the fact that noise is typically distributed across all wavelet coefficients, while the actual image signal is concentrated in a subset of large coefficients. By applying appropriate thresholding, we can remove the noise while preserving the important image features.

The denoising process follows these steps:
1. Apply forward wavelet transform
2. Apply soft or hard thresholding to wavelet coefficients
3. Apply inverse wavelet transform to reconstruct the image

## 📈 Performance Tips

- **Image Size**: Smaller images process faster but may show less detail
- **Decomposition Level**: Higher levels remove more noise but may blur fine details
- **Wavelet Choice**: Experiment with different wavelets for your specific image type
- **Noise Level**: The app works best with moderate noise levels (σ² = 0.01-0.05)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs or suggest features
- Improve the denoising algorithms
- Add new wavelet types
- Enhance the user interface

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io) for the interactive web interface
- Uses [PyWavelets](https://pywavelets.readthedocs.io) for wavelet transforms
- Image processing powered by [scikit-image](https://scikit-image.org) and [NumPy](https://numpy.org)

---

**Try it now!** Upload your noisy images and experience the power of wavelet-based denoising! 🚀