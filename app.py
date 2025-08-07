import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image

from utils import load_default_image, add_noise, upload_image
from wavelet_core import denoise_image_wavelet

# Configure the page for Hugging Face Spaces compatibility
st.set_page_config(
    page_title="Wavelet Image Denoising", 
    page_icon="🌊",
    layout="wide"
)

# Main title and description
st.title("🧼 Wavelet-Based Image Denoising App")
st.write("Upload a grayscale image or use the default Cameraman image. Gaussian noise will be added, then denoised using wavelet thresholding.")

# Add information about the app
with st.expander("📖 How to Use This App"):
    st.write("""
    1. **Choose Image**: Upload your own grayscale image or use the default Cameraman image
    2. **Adjust Parameters**: Use the sidebar to modify:
       - Wavelet type (different mathematical bases for decomposition)
       - Decomposition level (how many layers to process)
       - Noise variance (amount of noise to add for demonstration)
    3. **View Results**: Compare original, noisy, and denoised images side by side
    4. **Download**: Use the download button to save the denoised image
    """)

# Sidebar controls with better descriptions
st.sidebar.header("🔧 Denoising Parameters")

wavelet = st.sidebar.selectbox(
    "Wavelet Type", 
    ["haar", "db1", "db2", "sym4", "coif1"],
    help="Different wavelet bases provide different denoising characteristics"
)

level = st.sidebar.slider(
    "Decomposition Level", 
    1, 4, 2,
    help="Higher levels capture more global features but may lose fine details"
)

noise_var = st.sidebar.slider(
    "Noise Variance (σ²)", 
    0.001, 0.1, 0.01, 
    step=0.001,
    help="Amount of Gaussian noise to add (for demonstration purposes)"
)

# Add a separator
st.sidebar.markdown("---")
st.sidebar.markdown("**📊 Image Statistics**")

# Image upload section
st.header("📤 Upload Image")
uploaded = st.file_uploader(
    "Upload a grayscale image (PNG, JPG, JPEG)", 
    type=["png", "jpg", "jpeg"],
    help="For best results, use grayscale images. Color images will be converted to grayscale."
)

# Process image with error handling
try:
    if uploaded:
        img = upload_image(uploaded)
        st.sidebar.success("✅ Custom image loaded")
    else:
        img = load_default_image()
        st.sidebar.info("📷 Using default Cameraman image")
    
    # Display image statistics in sidebar
    st.sidebar.write(f"Image shape: {img.shape}")
    st.sidebar.write(f"Min value: {img.min():.3f}")
    st.sidebar.write(f"Max value: {img.max():.3f}")
    st.sidebar.write(f"Mean value: {img.mean():.3f}")
    
    # Process image
    noisy_img = add_noise(img, var=noise_var)
    denoised_img = denoise_image_wavelet(noisy_img, wavelet=wavelet, level=level)
    
    # Calculate quality metrics
    mse_noisy = np.mean((img - noisy_img) ** 2)
    mse_denoised = np.mean((img - denoised_img) ** 2)
    
    # Display results section
    st.header("🖼️ Results")
    
    # Create three columns for images
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Original")
        # Use width parameter instead of use_container_width for better compatibility
        st.image(img, caption="Original Image", width=None, clamp=True)
        
    with col2:
        st.subheader("Noisy")
        st.image(noisy_img, caption=f"Noisy (σ²={noise_var})", width=None, clamp=True)
        st.write(f"MSE: {mse_noisy:.6f}")
        
    with col3:
        st.subheader("Denoised")
        # Clip values to ensure they're in valid range
        denoised_display = np.clip(denoised_img, 0, 1)
        st.image(denoised_display, caption=f"Denoised ({wavelet}, level {level})", width=None, clamp=True)
        st.write(f"MSE: {mse_denoised:.6f}")
    
    # Quality improvement metrics
    st.header("📈 Denoising Performance")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        improvement = ((mse_noisy - mse_denoised) / mse_noisy) * 100
        st.metric(
            label="MSE Improvement", 
            value=f"{improvement:.2f}%",
            help="Percentage reduction in Mean Squared Error"
        )
    
    with col2:
        psnr_noisy = 10 * np.log10(1.0 / mse_noisy) if mse_noisy > 0 else float('inf')
        psnr_denoised = 10 * np.log10(1.0 / mse_denoised) if mse_denoised > 0 else float('inf')
        st.metric(
            label="PSNR (dB)", 
            value=f"{psnr_denoised:.2f}",
            delta=f"{psnr_denoised - psnr_noisy:.2f}",
            help="Peak Signal-to-Noise Ratio (higher is better)"
        )
    
    with col3:
        noise_reduction = (1 - mse_denoised/mse_noisy) * 100 if mse_noisy > 0 else 0
        st.metric(
            label="Noise Reduction", 
            value=f"{noise_reduction:.2f}%",
            help="Percentage of noise removed"
        )
    
    # Download functionality
    st.header("💾 Download Results")
    
    # Convert denoised image to downloadable format
    def convert_to_downloadable(image_array, filename):
        """Convert numpy array to downloadable image format"""
        # Ensure values are in [0, 255] range for uint8
        img_uint8 = (np.clip(image_array, 0, 1) * 255).astype(np.uint8)
        
        # Convert to PIL Image (without deprecated mode parameter)
        if len(img_uint8.shape) == 2:  # Grayscale
            pil_img = Image.fromarray(img_uint8)  # Pillow auto-detects grayscale
        else:  # RGB (shouldn't happen in this app, but just in case)
            pil_img = Image.fromarray(img_uint8)  # Pillow auto-detects RGB
        
        # Save to bytes buffer
        buf = io.BytesIO()
        pil_img.save(buf, format='PNG')
        buf.seek(0)
        return buf.getvalue()
    
    # Create download buttons
    col1, col2 = st.columns(2)
    
    with col1:
        denoised_bytes = convert_to_downloadable(denoised_display, "denoised_image.png")
        st.download_button(
            label="📥 Download Denoised Image",
            data=denoised_bytes,
            file_name="denoised_image.png",
            mime="image/png",
            help="Download the denoised image as PNG"
        )
    
    with col2:
        noisy_bytes = convert_to_downloadable(noisy_img, "noisy_image.png")
        st.download_button(
            label="📥 Download Noisy Image",
            data=noisy_bytes,
            file_name="noisy_image.png",
            mime="image/png",
            help="Download the noisy image for comparison"
        )
    
    # Technical details section
    with st.expander("🔬 Technical Details"):
        st.write(f"""
        **Wavelet Transform Parameters:**
        - Wavelet Type: {wavelet}
        - Decomposition Level: {level}
        - Noise Variance: {noise_var}
        
        **Image Processing:**
        - Original Image Range: [{img.min():.3f}, {img.max():.3f}]
        - Noisy Image Range: [{noisy_img.min():.3f}, {noisy_img.max():.3f}]
        - Denoised Image Range: [{denoised_img.min():.3f}, {denoised_img.max():.3f}]
        
        **Quality Metrics:**
        - MSE (Original vs Noisy): {mse_noisy:.6f}
        - MSE (Original vs Denoised): {mse_denoised:.6f}
        - PSNR (Noisy): {psnr_noisy:.2f} dB
        - PSNR (Denoised): {psnr_denoised:.2f} dB
        """)

except Exception as e:
    st.error(f"❌ An error occurred: {str(e)}")
    st.write("Please check your image file and try again.")
    
    # Show debug information in development
    if st.checkbox("Show debug information"):
        st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
Built with Streamlit 🚀 | Powered by PyWavelets 🌊
</div>
""", unsafe_allow_html=True)