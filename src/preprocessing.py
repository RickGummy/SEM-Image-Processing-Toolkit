import cv2
import numpy as np

def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise FilenotFoundError(f"Image not found at {image_path}")
    return image

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def enhance_contrast(image):
    clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
    return clahe.apply(image)

def apply_gaussian_blur(image, kernel_size = (5, 5), sigma = 0):
    return cv2.GaussianBlur(image, kernel_size, sigma)

def apply_threshold(image, threshold_value = 125):
    _, threshold_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return threshold_image

def preprocess_image(image_path):
    image = load_image(image_path)
    gray_image = convert_to_grayscale(image)
    enhanced_image = enhance_contrast(gray_image)
    blurred_image = apply_gaussian_blur(enhanced_image)
    threshold_image = apply_threshold(blurred_image)
    return threshold_image