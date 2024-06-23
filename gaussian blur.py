import cv2

# Load the image from file
image = cv2.imread('test1.jpg')
# Check if the image was successfully loaded
if image is None:
    raise ValueError("Image not found or unable to load.")

# Apply Gaussian Blur
# ksize is the kernel size, must be odd and positive (e.g., (5, 5))
# sigmaX is the standard deviation in the X direction, set to 0 to let OpenCV calculate it based on the kernel size
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
# Define the output filename
output_filename = 'output_image.jpg'

# Save the image
success = cv2.imwrite(output_filename, blurred_image)
#blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
# Invert the threshold: set pixels of 255 to 0, and those less than 255 to 255
#_, blurred_image = cv2.threshold(blurred_image, 254, 255, cv2.THRESH_BINARY_INV)

# Define the desired window size
window_width = 330
window_height = 420

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

