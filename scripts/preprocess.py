import cv2
import numpy as np
import os

def preprocess_image(image_path):
    """
    Preprocesses an input image: converts to grayscale, resizes, applies Gaussian blur and thresholding.
    
    Args:
    - image_path (str): Path to the image file.

    Returns:
    - image (numpy array): Preprocessed image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
    image = cv2.resize(image, (128, 128))  # Resize for CNN compatibility
    image = cv2.GaussianBlur(image, (3, 3), 0)  # Reduce noise
    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)  # Improve contrast
    image = image / 255.0  # Normalize pixel values

    return image
