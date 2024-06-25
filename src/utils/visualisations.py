import matplotlib.pyplot as plt
import numpy as np

def show_pixel_values(image):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(image, cmap='gray')

    # Calculate optimal font size based on image dimensions
    font_size = max(6, min(image.shape[0], image.shape[1]) // 15)  # Adjust the denominator for font size scaling

    # Loop through each pixel in the image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Add text annotation with pixel value
            ax.text(j, i, str(image[i, j]), color='red', ha='center', va='center', fontsize=font_size)

    # Remove axis ticks
    ax.axis("off")

    # Show the plot
    plt.show()

# Example usage:
# Assuming 'image' is your grayscale image array (numpy array)
image = np.random.randint(0, 256, (45, 45))  # Example random grayscale image
image = plt.imread("test.jpg")
show_pixel_values(image)