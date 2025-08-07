import numpy as np
import pywt

def estimate_sigma(coeffs):
    detail_coeffs = coeffs[-1][-1]  # Diagonal detail at finest scale
    return np.median(np.abs(detail_coeffs)) / 0.6745

def denoise_image_wavelet(image, wavelet='db2', level=2):
    coeffs = pywt.wavedec2(image, wavelet=wavelet, level=level)
    sigma = estimate_sigma(coeffs)
    uthresh = sigma * np.sqrt(2 * np.log(image.size))

    coeffs_thresh = [coeffs[0]]  # keep approximation
    for detail_level in coeffs[1:]:
        cH, cV, cD = detail_level
        cH = pywt.threshold(cH, uthresh, mode='soft')
        cV = pywt.threshold(cV, uthresh, mode='soft')
        cD = pywt.threshold(cD, uthresh, mode='soft')
        coeffs_thresh.append((cH, cV, cD))

    return pywt.waverec2(coeffs_thresh, wavelet)
