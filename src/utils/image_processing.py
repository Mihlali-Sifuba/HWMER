from calendar import c
import cv2
import numpy as np
from typing import Tuple, Union


def thicken_character_edge_detection(image: np.ndarray, thickness: int = 2) -> np.ndarray:
    """
    Detect and thicken the edges of characters in a given image.

    Parameters:
    image (np.ndarray): Input image in BGR format.
    thickness (int): Thickness of the edge lines. Default is 2.

    Returns:
    np.ndarray: Image with thickened character edges.
    """
    # Input validation
    if not isinstance(image, np.ndarray):
        raise TypeError("Input image must be a numpy array.")
    # Ensure image has non-zero size
    if image.size == 0:
        raise ValueError("Input image has zero size")
    # Check if image has a valid shape
    if len(image.shape) not in [2, 3] or image.shape[0] <= 0 or image.shape[1] <= 0:
        raise ValueError("Input image must have a valid shape (height, width) or (height, width, channels)")
    # Check for NaN or Inf values in the image
    if np.any(np.isnan(image)) or np.any(np.isinf(image)):
        raise ValueError("Input image contains NaN or Inf values")
    if not isinstance(thickness, int) or thickness < 0:
        raise ValueError("Thickness must be a non-negative integer.")
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, 255, thickness)
        return image
    except cv2.error as e:
        raise RuntimeError(f"OpenCV error: {e}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

def thicken_character_binary_morphology():
    pass
def thicken_character_gaussian_blur(image: np.ndarray, kernel_size: Tuple[int, int], sigmaX: Union[int, float], sigmaY: Union[int, float]=0) -> np.ndarray:
    if image is None:
        raise ValueError("Input image is None")
    
    # Check if image is a numpy array
    if not isinstance(image, np.ndarray):
        raise TypeError("Input image must be a numpy array")
    
    # Ensure image has non-zero size
    if image.size == 0:
        raise ValueError("Input image has zero size")
    
    # Check if image has a valid shape
    if len(image.shape) not in [2, 3] or image.shape[0] <= 0 or image.shape[1] <= 0:
        raise ValueError("Input image must have a valid shape (height, width) or (height, width, channels)")
    
    # Check for NaN or Inf values in the image
    if np.any(np.isnan(image)) or np.any(np.isinf(image)):
        raise ValueError("Input image contains NaN or Inf values")

    if not isinstance(kernel_size, tuple) or len(kernel_size) != 2 or kernel_size[0] <= 0 or kernel_size[1] <= 0:
        raise ValueError("Kernel size must be a tuple of two positive odd integers")

    if not (isinstance(sigmaX, (int, float)) and sigmaX >= 0):
        raise ValueError("sigmaX must be a non-negative number")

    if not (isinstance(sigmaY, (int, float)) and sigmaY >= 0):
        raise ValueError("sigmaY must be a non-negative number")

    # Apply thresholding
    # Invert the threshold: set pixels of 255 to 0, and those less than 255 to 255
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Apply Gaussian Blur
    # ksize is the kernel size, must be odd and positive (e.g., (5, 5))
    # sigmaX is the standard deviation in the X direction, set to 0 to let OpenCV calculate it based on the kernel size
    image = cv2.GaussianBlur(image, kernel_size, sigmaX, None, sigmaY=sigmaY)
    image = cv2.equalizeHist(image)

    # Apply binary thresholding to the image
    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
    # Convert image to uint8 if it's not already
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)
    return image
