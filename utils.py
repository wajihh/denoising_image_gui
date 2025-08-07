import numpy as np
from skimage import data, img_as_float
from skimage.util import random_noise
from skimage import io

def load_default_image():
    return img_as_float(data.camera())  # 512x512 grayscale image

def add_noise(image, var=0.01):
    return random_noise(image, mode='gaussian', var=var)

def upload_image(uploaded_file):
    from PIL import Image
    import io as sysio
    img = Image.open(sysio.BytesIO(uploaded_file.read())).convert('L')
    return np.array(img) / 255.0
