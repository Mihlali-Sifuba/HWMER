import cv2

# Load the image from file
image = cv2.imread('test.jpg')
# Check if the image was successfully loaded
if image is None:
    raise ValueError("Image not found or unable to load.")

# Apply thresholding
# Invert the threshold: set pixels of 255 to 0, and those less than 255 to 255
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# Apply Gaussian Blur
# ksize is the kernel size, must be odd and positive (e.g., (5, 5))
# sigmaX is the standard deviation in the X direction, set to 0 to let OpenCV calculate it based on the kernel size
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
blurred_image = cv2.equalizeHist(blurred_image)

# Apply binary thresholding to the image
_, blurred_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY)

# Define the desired window size
window_width = 450
window_height = 450

# Create a named window
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Blurred Image', cv2.WINDOW_NORMAL)

# Resize the window to the desired size
cv2.resizeWindow('Original Image', window_width, window_height)
cv2.resizeWindow('Blurred Image', window_width, window_height)

# Display the images in the resized window
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

